import requests
import sqlite3, csv, nltk
import os.path
from pymongo import MongoClient

from FacebookDataAcquisition import extractFromFacebook
from YoutubeDataAcquisition import extractFromYoutube

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Connecting to MongoDB ...")
client = MongoClient('localhost:27017')
db = client.database

'''db.postsData.delete_many({"source": "facebook"})
db.commentsData.delete_many({"source": "facebook"})'''

print("Connecting to Sqlite ...")
db_path = os.path.join(BASE_DIR, "testpages.db")
dbpages = sqlite3.connect(db_path)

cursor_pages = dbpages.cursor()
cursor_pages.execute('SELECT * FROM facebookPages')
all_pages = cursor_pages.fetchall()

cursor_entities = dbpages.cursor()
cursor_entities.execute('SELECT * from entities')
curr_entities = all_entities = cursor_entities.fetchall()

print("Extracting from Facebook...")
extractFromFacebook(all_pages, all_entities, curr_entities, db, dbpages)

print("Extracting from Youtube...")
extractFromYoutube(all_entities, db)