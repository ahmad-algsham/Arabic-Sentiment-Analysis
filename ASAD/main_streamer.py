from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from textblob_ar import TextBlob

import kays_twitter
import regexarabic as ra
import functions as ff
import gulfstates as gs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        # self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(kays_twitter.consumer_key, kays_twitter.consumer_secret)
        auth.set_access_token(kays_twitter.access_key, kays_twitter.access_secret)
        return auth


class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        argword = ra.remove(tweet)
        argword = ra.harakat(argword)
        argword = ra.WordsFiltires(argword)
        # print(argword)
        return argword
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'natural'
        else:
            return 'negative'

    def tweets_to_data_frame(self, result_SA):
        df_SA = gs.get_saudi_arabia(result_SA)

        return df_SA


if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()

    result_SA = api.trends_place(23424938)

    df_SA = tweet_analyzer.tweets_to_data_frame(result_SA)
    df_SA['sentiment'] = df_SA['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
    df_SA.to_csv('data_SA.csv', encoding='utf-16', sep='\t', index=False)


    print(df_SA.head(10))


    # TODO learn about matplotlib


    # twitter_client = TwitterClient()
    # print(twitter_client.get_user_timeline_tweets(1, result_SA))
