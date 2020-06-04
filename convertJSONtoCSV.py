import json
import csv
import os

DATAPATH = "data/trumptwitterarchive/"

jsonFileList = os.listdir(DATAPATH)

jsonData = []

for i in jsonFileList:
    if i.endswith(".json"):
        with open(DATAPATH + i, 'r') as json_file:
            jsonData += json.load(json_file)

with open(DATAPATH + 'trumptwitterarchive.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile)

    # write data
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
