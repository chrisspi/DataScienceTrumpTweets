import time
import GetOldTweets3 as got
import csv
from datetime import date, timedelta

DATAPATH = "data/"
MAXTWEETS = 10
MAXDATE = date.fromisoformat('2020-04-15')
DELTADAYS = 360

startDate = date.fromisoformat('2009-04-05')
endDate = startDate + timedelta(days=DELTADAYS)

tweetCriteria = got.manager.TweetCriteria().setUsername('realDonaldTrump')\
                                           .setSince(startDate.isoformat())\
                                           .setUntil(endDate.isoformat())

with open(DATAPATH + 'qualityCheckData.csv', 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)

    # write header
    tweetwriter.writerow([
        "id",
        "id_str",
        "text",
        "created_at",
        "retweet_count",
        "favorite_count",
        ])

    # write data
    while endDate < MAXDATE:

        print("Getting tweets from " , startDate.isoformat() , " until ", endDate.isoformat())
        tweetList = got.manager.TweetManager.getTweets(tweetCriteria)
        print("Tweets downloaded...")
        print("Writing to file.")

        for tweet in reversed(tweetList):

            tweetwriter.writerow([
                tweet.id,
                tweet.permalink,
                tweet.text,
                tweet.date,
                tweet.retweets,
                tweet.favorites
                ])

        print("Calculate new startDate and endDate")
        startDate = endDate + timedelta(days=1)
        endDate = startDate + timedelta(days=DELTADAYS)

        tweetCriteria = got.manager.TweetCriteria().setUsername('realDonaldTrump')\
                                                .setSince(startDate.isoformat())\
                                                .setUntil(endDate.isoformat())

        print("Time to sleep for 15 minutes.")
        time.sleep(60 * 15)
    
    # write the last portion of tweets
    endDate = MAXDATE

    tweetCriteria = got.manager.TweetCriteria().setUsername('realDonaldTrump')\
                                            .setSince(startDate.isoformat())\
                                            .setUntil(endDate.isoformat())
    tweetList = got.manager.TweetManager.getTweets(tweetCriteria)
    print("Getting last tweets !!!: ")

    for tweet in reversed(tweetList):

        tweetwriter.writerow([
            tweet.id,
            tweet.permalink,
            tweet.text,
            tweet.date,
            tweet.retweets,
            tweet.favorites
            ])

    print("FINISHED! Bye.")

# for tweet in tweets:
#     print(tweet.id, tweet.username, tweet.date, tweet.retweets, tweet.favorites)