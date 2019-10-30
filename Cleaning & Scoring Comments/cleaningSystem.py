from pymongo import MongoClient
import re, string, nltk, csv

print("Connecting to MongoDB ...")
client = MongoClient('localhost:27017')
db = client.database


rawComments = db.rawComments.find()

#########################################################################
#                                                                       #
#      Cleaning words functions used in the cleanComment() function     #
#                                                                       #
#########################################################################

def translate_numbers(word):
    # add check to not replace intentionally given numbers e.g datatime. 
    # if the word has alphabetic characters then execute replace
    # else the word is meant to have numericals and pass
    if [i for i in word if i.isalpha()]:   
        replace_map = {'2': "a", 
                       '3': "a", 
                       '5': "kh",
                        '7': 'h',
                        '8': "gh",
                        '9': "k"
                       }
        translated_word = ""
        for c in word:  
            if c in replace_map.keys(): 
                translated_word += replace_map[c]
            else: 
                translated_word += c 
       
    return translated_word

def remove_redundant_letters(word):
    return re.sub(r'(.)\1+', r'\1', word)



#####################################################################################
#                                                                                   #
#         cleanComment(comment) is used to normalize the words of a comment         #
#      and to make the results of string matching more accurate and precise.        #
#                                                                                   #
#####################################################################################

def cleanComment(comment):

    tokens = comment.split()

    #ignoring case by converting the words to lowercase letters
    tokens = [word.lower() for word in tokens]

    # translate arabic phonetic numbers used in tunisian dialect  (for example: '7' --> 'h', '5' --> "kh")
    tokens = [translate_numbers(w) for w in tokens]

    #remove punctuation
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]

    #remove redundant letters (for example: "mahleeeeeh" --> "mahleh")
    tokens = [remove_redundant_letters(w) for w in tokens]

    #remove short words of length <=2 because in general they are insignificant and will slow down the process
    tokens = [word for word in tokens if len(word) > 2]

    cleancomment = " ".join(tokens)

    return cleancomment

###################################################################
#                                                                 #
#                    Scoring Sytem                                #
#                                                                 #
###################################################################
def checkSimilarity(word1, word2):
    return nltk.edit_distance(word1, word2) < 2
        #return nltk.edit_distance(word1, word2) / min(len(word1),len(word2))  < 0.3


def sentimentScore(words, dictionary):
    scoreComment = tokenCount = 0
    
    for word, token in zip(words, dictionary): 
        if checkSimilarity(word, token[0]):
            if token[1] != "":
                scoreComment = scoreComment + int(token[1])
                tokenCount = tokenCount + 1
                break
    if tokenCount != 0:
        scoreComment = scoreComment / tokenCount

    return scoreComment


#########################################################################
#                                                                       #
#      Clean the raw comments extracted from the data acquisition       #
#      system.                                                          #
#                                                                       #
#########################################################################

 # Load the dictionary
dictionary = []
with open('cleanDictionary.csv', 'r', newline='') as dictionaryFile:
    dictionaryReader = csv.reader(dictionaryFile, delimiter=',')
    i = 0
    for row in dictionaryReader:
        if (row[1] == 0):
            continue
        dictionary.append([row[0], row[1]])


print("Cleaning comments")
#db.cleanComments.delete_many()
for comment in rawComments:
    existant = db.cleanComments.find({"id": comment["id"]}).count()
    if existant:
        continue

    cleancomment = cleanComment(comment["message"])


    words = cleancomment.split()

    score = sentimentScore(words, dictionary)

    page = ""
    if 'page' in comment:
        page = comment["page"]
    db.cleanComments.insert_one({
        "_id": comment["_id"],
        "id": comment["id"],
        "time": comment["time"],
        "message": cleancomment,
        "entity": comment["entity"],
        "source": comment["source"],
        "page": page,
        "score": score
    })

    #print(comment["entity"])

