# DataScienceTrumpTweets

Data Sources
============
We collect tweets of Donald Trump from two different sources.

1. [The Trump Twitter Archive](http://www.trumptwitterarchive.com/about)
2. [Trump Tweets repository from Kaggle](https://www.kaggle.com/austinreese/trump-tweets)

## Getting the Data from trumptwitterarchive

We can get the data of the trump twitter archive by downloading it from their
[github page](https://github.com/bpb27/trump_tweet_data_archive). What we get
are a bunch of files in the .json format. The first thing we do is converting 
these files into .csv files. This is done in the python script [convertJSONtoCSV.py](./convertJSONtoCSV.py).

