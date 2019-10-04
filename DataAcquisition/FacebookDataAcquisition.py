import requests
import sqlite3, csv, nltk
import os.path

from pymongo import MongoClient
import secrets

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

entities_file_path = os.path.join(BASE_DIR, "entity-equivalents.csv")

def checkSimilarity(word1, word2):
    return nltk.edit_distance(word1, word2) < 2


errors = []

def extractFromFacebook(all_pages, all_entities, curr_entities, db, dbpages):
    base_url = "https://graph.facebook.com/v2.12/"

    limit = 'limit=100'
    access_token = "access_token={}".format(secrets.FACEBOOK_TOKEN)

    page_part = "/posts"
    post_part = "/comments"

    categories = ['politics', 'art', 'entertainment', 'business', 'sport']

    # get entities equivalent words (arabic and latin letters)
    curr_entities_equiv = {}
    with open(entities_file_path, 'r', newline='') as equivalentsFile:
        equivalentsReader = csv.reader(equivalentsFile, delimiter=',')
        for row in equivalentsReader:
            for entity in curr_entities:
                if (entity[0] in row[0]) or (row[0] in entity[0]):
                    curr_entities_equiv.update({row[0]: row[0:len(row)]})



    print("Parsing pages...")

    for page in all_pages:

        print('\n')

        res_posts = requests.get(base_url + page[0] + page_part + '?' + limit + '&' + access_token)

        posts = res_posts.json()

        entity_page = page[5]

        #curr_entities = entities related to a category
        if page[3].upper() == 'MISC':
            curr_entities = all_entities
        else:
            for category in categories:
                if category.upper() in page[3].upper():
                    curr_cursor = dbpages.cursor()
                    curr_entities = curr_cursor.execute('SELECT * from entities where category=?', (category,)).fetchall()
                    break


        print("Page " + page[0] + " | related entity: " + entity_page)

        if not "data" in posts:
            errors.append(page[0])
            continue

        for post in posts["data"]:

            if 'message' in post:
                msg = post["message"]
            else:
                continue

            entity_post = 'None'
            if entity_page != 'None' and entity_page != 'none':
                entity_post = entity_page
            else:
                for ent in curr_entities_equiv.items():
                    for equiv in ent[1]:
                        if equiv in msg and entity_post == "None" and len(equiv) > 3:
                            entity_post = ent[0]

            #Check if post has been stored before
            if  db.postsData.find({"id": post["id"]}).count() == 0:
                db.postsData.insert_one({
                    "id": post["id"],
                    "time": post["created_time"],
                    "message": msg,
                    "entity": entity_post,
                    "page": page[0],
                    "source": "facebook"
                })
            else:
                continue

            #print(" -- Post " + post["id"])

            res_comments = requests.get(base_url + post["id"] + post_part + '?' + access_token)
            comments = res_comments.json()

            countComments = 0
            for comment in comments["data"]:
                cmt = ""
                if 'message' in comment:
                    cmt = comment["message"]
                entity_mentionned = ""
                if entity_post != 'None':
                    entity_mentionned = entity_post
                else:
                    splitted = cmt.split()
                    for ent in curr_entities_equiv.items():
                        for equiv in ent[1]:
                            if equiv in cmt and entity_mentionned != "" and len(equiv) > 3:
                                entity_mentionned = ent[0]
                                
                #Check if comment has been stored before
                if db.rawComments.find({"id": comment["id"]}).count() == 0 and entity_mentionned != "":
                    db.rawComments.insert_one({
                        "id": comment["id"],
                        "time": comment["created_time"],
                        "message": cmt,
                        "entity": entity_mentionned,
                        "source": "facebook",
                        "page": page[0]
                    })
                    countComments = countComments + 1

            #print(countComments)


    print(errors)