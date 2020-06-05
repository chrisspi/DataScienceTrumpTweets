# DataScienceTrumpTweets

Data Sources
============
We collect tweets of Donald Trump from two different sources.

1. [The Trump Twitter Archive](http://www.trumptwitterarchive.com/about)
    Format: source, id_str, text, created_at, retweet_count, in_reply_to_user_id_str, favorite_count, is_retweet
2. [Trump Tweets repository from Kaggle](https://www.kaggle.com/austinreese/trump-tweets)
    Format: id, link, content, date, retweets, favorites, mentions, hashtags

## Getting the Data from trumptwitterarchive

We can get the data of the trump twitter archive by downloading it from their
[github page](https://github.com/bpb27/trump_tweet_data_archive). What we get
are a bunch of files in the .json format. The first thing we do is converting 
these files into .csv files. This is done in the python script [convertJSONtoCSV.py](./convertJSONtoCSV.py).

