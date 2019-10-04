from googleapiclient.discovery import build
import time
import sqlite3
from pymongo import MongoClient
import secrets


def get_videos_FromSearch(youtube, keyword, order):
    search_response = youtube.search().list(
        q=keyword,
        type="video",
        part="id, snippet",
        maxResults=50,
        order=order
    ).execute()

    return search_response.get("items", [])

countComments = 0


def get_Comments_FromVideo(youtube, video, entity, db):

    tempComments = []
    time.sleep(1.0)
    c = 0
    try:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video,
            textFormat="plainText",
            maxResults=100
        ).execute()

        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]

            c = c + 1
            #Check if comment has been stored before
            if db.rawComments.find({"id": comment["id"]}).count() == 0:
                db.rawComments.insert_one({
                    "id": comment["id"],
                    "time": comment["snippet"]["publishedAt"],
                    "message": comment["snippet"]["textOriginal"],
                    "entity": entity,
                    "source": "youtube"
                })

    except:
        print("Comments Disabled for video ")

    return c

def extractFromYoutube(all_entities, db):
    DEVELOPER_KEY = secrets.YOUTUBE_DEVELOPER_KEY
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


    '''db.postsData.delete_many({"source": "youtube"})
    db.rawComments.delete_many({"source": "youtube"})'''


    print("Browsing videos by searching entities...")
    for entity in all_entities:
        print(entity[0])
        countComments = 0
        #get latest videos of an entity
        videos = get_videos_FromSearch(youtube, entity[0], "date")

        for video in videos:
            if video["id"]["kind"] == "youtube#video":
                videoId = video["id"]["videoId"]
                #Check if video has been stored before
                if db.postsData.find({"id": videoId}).count() == 0:
                    db.postsData.insert_one({
                        "id": videoId,
                        "time": video["snippet"]["publishedAt"],
                        "message": video["snippet"]["title"],
                        "entity": entity[0],
                        "source": "youtube",
                        "page" : "0"
                    })

                countComments = countComments + get_Comments_FromVideo(youtube, videoId, entity[0], db)

        print(countComments)

    # print(videos)

