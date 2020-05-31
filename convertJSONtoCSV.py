import json
import csv
import os

dataPath = "data/trumptwitterarchive/"

jsonFileList = os.listdir(dataPath)

jsonData = []

for i in jsonFileList:
    if i.endswith(".json"):
        with open(dataPath + i, 'r') as json_file:
            jsonData += json.load(json_file)

with open(dataPath + 'trumptwitterarchive.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile)
    for column in jsonData:
        jsonwriter.writerow([
            column["source"],
            column["id_str"],
            column["text"],
            column["created_at"],
            column["retweet_count"],
            column["in_reply_to_user_id_str"],
            column["favorite_count"],
            column["is_retweet"]
            ])
