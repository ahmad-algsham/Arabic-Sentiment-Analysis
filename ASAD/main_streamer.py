from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import kays_twitter
import pandas as pd
import numpy as np


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user
    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_lsit(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# # # # TWITTER AUTHENTICATION # # # #
class TwitterAuthenticator():
    """
    class for authentications TWITTER API
    """
    def authenticate_twitter_app(self):
        auth = OAuthHandler(kays_twitter.consumer_key, kays_twitter.consumer_secret)
        auth.set_access_token(kays_twitter.access_key, kays_twitter.access_secret)
        return auth


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    class for streaming and processing live tweet
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_lsit):
        # this handles Twitter authentication and the connection to the Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=hash_tag_lsit)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """"
    This a basic listener class that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data):
        try:
            print(raw_data)
            with open(self.fetched_tweets_filename, 'a', encoding='utf-8') as tf:
                tf.write(raw_data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # Return False on_data method in case rate limit occurs.
            return False
        print(status_code)


class TweetAnalyzer():
    """
    Functionality for analysis and categorizing content from tweets.
    """
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df


if __name__ == "__main__":

    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screan_name="News_Ejazah", count=10)




















    # hash_tag_lsit = ['#فيروس_كورونا', '#علمتني_كورونا']
    # fetched_tweets_filename = 'tweets.txt'
    #
    # twitter_client = TwitterClient('News_Ejazah')
    # print(twitter_client.get_user_timeline_tweets(1))
    # print(twitter_client.get_friend_lsit(1))
    # print(twitter_client.get_home_timeline_tweets(1))
    #
    # # twitter_Streamer = TwitterStreamer()
    # # twitter_Streamer.stream_tweets(fetched_tweets_filename, hash_tag_lsit)
