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
    for row in jsonData:
        jsonwriter.writerow([
            row["source"],
            row["id_str"],
            row["text"],
            row["created_at"],
            row["retweet_count"],
            row["in_reply_to_user_id_str"],
            row["favorite_count"],
            row["is_retweet"]
            ])
