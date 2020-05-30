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
        # TODO: write wanted columns to csv file
        jsonwriter.writerow([row['source'], row['id_str'], row['retweet_count'], row['text']])
