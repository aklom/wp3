from pymongo import MongoClient

import  csv,  math, nltk, os



##################################################################################
#                                                                                #
#         Attribute a score to a comment based on matching its words             #
#               with the dictionary                                              #
#                                                                                #
##################################################################################

def sentimentScore(words, dictionary):

    scoreComment = tokenCount = 0

    for word in words:
        for token in dictionary:
            if checkSimilarity(word, token[0]):
                if token[1] != "":
                    scoreComment = scoreComment + int(token[1])
                    tokenCount = tokenCount + 1
                    break
    if tokenCount != 0:
        scoreComment = scoreComment / tokenCount

    return scoreComment


##################################################################################
#                                                                                #
#         Check if to words correspond to the same word using edit distance      #
#         spell checking                                                         #
#                                                                                #
##################################################################################

def checkSimilarity(word1, word2):
    return nltk.edit_distance(word1, word2) < 2

##################################################################################

def analyze(entity):
    print("Connecting to MongoDB ...")
    client = MongoClient('localhost:27017')
    db = client.database

    # Extract all the comments talking about the chosen entity from the clean comments database
    cleanComments = db.cleanComments.find({"entity": entity})


    ##################################################################################

    commentsCounter = 0
    youtubeCounter = 0
    facebookCounter = 0
    positiveCounter = 0
    negativeCounter = 0

    numberOfMentionsPerDay = {}
    level = {-5: 0, -4: 0, -3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    if os.path.exists('negative.csv'):
        os.remove('negative.csv')
    if os.path.exists('positive.csv'):
        os.remove('positive.csv')

    with open('negative.csv', 'w', newline='') as negativeFile, open('positive.csv', 'w', newline='') as positiveFile:
        negativeWriter = csv.writer(negativeFile, delimiter=',')
        positiveWriter = csv.writer(positiveFile, delimiter=',')
        i= 0
        for comment in cleanComments:
            print(i)
            i = i + 1

            scoreComment = comment["score"]

            # Storing comments by polarity
            if (scoreComment < 0):
                negativeCounter = negativeCounter + 1
                print(scoreComment)
                equivRawComment = db.rawComments.find({"id": comment["id"]})
                for comment in equivRawComment:
                    negativeWriter.writerow([comment["message"] + " <------------>  Score: " + str(scoreComment)+ '##########################' + comment["source"]])
                    negativeWriter.writerow("")



            if (scoreComment > 0):
                positiveCounter = positiveCounter + 1
                print(scoreComment)

                equivRawComment = db.rawComments.find({"id": comment["id"]})
                for comment in equivRawComment:
                    positiveWriter.writerow([comment["message"] + " <------------>  Score: " + str(scoreComment) + '##########################' + comment["source"]])
                    positiveWriter.writerow("")

            # Number of mentions per day and per source
            postedTime = comment["time"]
            postedTime = postedTime[:10]
            if comment["source"] == "facebook":
                x = 0
            elif comment["source"] == "youtube":
                x = 1

            if (postedTime,x) in numberOfMentionsPerDay :
                numberOfMentionsPerDay[(postedTime,x)] = numberOfMentionsPerDay[(postedTime,x)] + 1
            else:
                numberOfMentionsPerDay.update({(postedTime,x): 1})

            # Number of comments per level of polarity
            level[math.ceil(scoreComment)] = level[math.ceil(scoreComment)] + 1

            # Number of comments per data source
            if comment["source"] == "facebook":
                facebookCounter = facebookCounter + 1
            elif comment["source"] == "youtube":
                youtubeCounter = youtubeCounter + 1

            # Total Number of comments
            commentsCounter = commentsCounter + 1

    print("Total number of comments: %s", commentsCounter)
    print()

    print("Number of Youtube comments: %s", youtubeCounter)
    print("Number of Facebook comments: %s", facebookCounter)
    print()

    print("Number of Positive Comments: %s", positiveCounter)
    print("Number of Negative Comments: %s", negativeCounter)
    print()

    i = 0
    rows = []
    sortedMentions = sorted(numberOfMentionsPerDay.items(), reverse=True)
    map = {}
    for item in sortedMentions:
        map.update({item[0][0]: (0, 0)})

    for item in sortedMentions:
        facebook = map[item[0][0]][0]
        youtube = map[item[0][0]][1]
        if item[0][1] == 0:
            facebook = item[1]
        else:
            youtube = item[1]
        map.update({item[0][0]: (facebook, youtube)})

    for item in map.items():
        print(item)
        rows.append([item[0], item[1][0], item[1][1]])
        i = i + 1
        if i > 20:
            break

    rows = list(reversed(rows))

    return {"counter": commentsCounter,"youtube": youtubeCounter, "facebook": facebookCounter,
            "positive": positiveCounter, "negative": negativeCounter,
            "neg5": level[-5], "neg4": level[-4], "neg3": level[-3], "neg2": level[-2], "neg1": level[-1] ,
            "pos5": level[5], "pos4": level[4], "pos3": level[3], "pos2": level[2], "pos1": level[1] ,
            "rows": rows
            }

