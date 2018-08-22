#!/usr/bin/env python

import json
import urllib.request
import pymongo


def find():
    print("find , reporting for duty")

    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)
    except Exception as e:
        print("Unexpected error: ", type(e), e)
    for doc in cursor:
        print(doc)


# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories
find()
