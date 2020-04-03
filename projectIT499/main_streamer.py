from tweepy import API
from tweepy import OAuthHandler
from textblob_ar import TextBlob

from projectIT499 import kays_twitter, regexarabic as ra, gulfstates as gs, functions as ff

import time


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_saudi_arabia(self):
        result_SA = api.trends_place(23424938)
        file_SA = 'TRENDS_SA'
        df_SA = gs.get_data_to_frame(result_SA, file_SA)

        return df_SA

    def get_kuwait(self):
        result_KW = api.trends_place(23424870)
        file_KW = 'TRENDS_KW'
        df_KW = gs.get_data_to_frame(result_KW, file_KW)

        return df_KW

    def get_bahrain(self):
        result_BH = api.trends_place(23424753)
        file_BH = 'TRENDS_BH'
        df_BH = gs.get_data_to_frame(result_BH, file_BH)

        return df_BH

    def get_qatar(self):
        result_QA = api.trends_place(23424930)
        file_QA = 'TRENDS_QA'
        df_QA = gs.get_data_to_frame(result_QA, file_QA)

        return df_QA

    def get_united_arab_emirates(self):
        result_AE = api.trends_place(23424738)
        file_AE = 'TRENDS_AE'
        df_AE = gs.get_data_to_frame(result_AE, file_AE)

        return df_AE

    def get_oman(self):
        result_OM = api.trends_place(23424898)
        file_OM = 'TRENDS_OM'
        df_OM = gs.get_data_to_frame(result_OM, file_OM)

        return df_OM


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
        argword = ra.WordsFiltires(argword)
        argword = ra.harakat(argword)
        return argword

    def analyze_sentiment(self, tweet):

        try:
            analysis = TextBlob(self.clean_tweet(tweet))
            time.sleep(0.2)
            if analysis.sentiment.polarity > 0:
                return 'positive'
            elif analysis.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'

        except BaseException as e:
            print("Error analyze_sentiment %s" % str(e))
        pass


if __name__ == '__main__':
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()

    while True:
        try:
            # extract tweets from top trend in Saudi Arabia
            df_SA = twitter_client.get_saudi_arabia()
            print('Start sa sentiment')
            df_SA['sentiment'] = df_SA['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_SA = df_SA.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_SA.to_csv('data_SA.csv', encoding='utf-16', sep='\t', index=False)
            print(df_SA.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)  # Google Translate API also has a default limit  100,000 characters per 100 second.
        except BaseException as e:
            print("Error get_saudi_arabia %s" % str(e))
            time.sleep(1)
            pass

        try:
            # extract tweets from top trend in Kuwait
            df_KW = twitter_client.get_kuwait()
            print("Start kw sentiment")
            df_KW['sentiment'] = df_KW['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_KW = df_KW.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_KW.to_csv('data_KW.csv', encoding='utf-16', sep='\t', index=False)
            print(df_KW.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)  # Google Translate API also has a default limit  100,000 characters per 100 second.
        except BaseException as e:
            print("Error get_kuwait %s" % str(e))
            time.sleep(1)
            pass

        try:
            # extract tweets from top trend in Bahrain
            df_BH = twitter_client.get_bahrain()
            print('Start bh sentiment')
            df_BH['sentiment_BH'] = df_BH['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_BH = df_BH.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_BH.to_csv('data_BH.csv', encoding='utf-16', sep='\t', index=False)
            print(df_BH.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)  # Google Translate API also has a default limit  100,000 characters per 100 second.
        except BaseException as e:
            print("Error get_bahrain %s" % str(e))
            time.sleep(1)
            pass

        try:
            # extract tweets from top trend in Qatar
            df_QA = twitter_client.get_qatar()
            print('Start qa sentiment')
            df_QA['sentiment'] = df_QA['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_QA = df_QA.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_QA.to_csv('data_QA.csv', encoding='utf-16', sep='\t', index=False)
            print(df_QA.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)  # Google Translate API also has a default limit  100,000 characters per 100 second.
        except BaseException as e:
            print("Error get_qatar %s" % str(e))
            time.sleep(1)
            pass

        try:
            # extract tweets from top trend in United Arab Emirates
            df_AE = twitter_client.get_united_arab_emirates()
            print('Start ae sentiment')
            df_AE['sentiment'] = df_AE['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_AE = df_AE.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_AE.to_csv('data_AE.csv', encoding='utf-16', sep='\t', index=False)
            print(df_AE.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)  # Google Translate API also has a default limit  100,000 characters per 100 second.
        except BaseException as e:
            print("Error get_united_arab_emirates %s" % str(e))
            time.sleep(1)
            pass

        try:
            # extract tweets from top trend in Oman
            df_OM = twitter_client.get_oman()
            print('Start om sentiment')
            df_OM['sentiment'] = df_OM['Tweets'].apply(lambda x: tweet_analyzer.analyze_sentiment(x))
            df_OM = df_OM.dropna(subset=['sentiment'])  # drop row if return sentiment nan
            df_OM.to_csv('data_OM.csv', encoding='utf-16', sep='\t', index=False)
            print(df_OM.tail())
            print('waiting for avoid rate limit')
            time.sleep(300)
            # Google Translate API also has a default limit  2 million characters per day.
        except BaseException as e:
            print("Error get_oman %s" % str(e))
            time.sleep(1)
            pass

        print('Done for now')
        print('redo the process')

        ff.marge()
        print('Done combine')
        time.sleep(100)

    # TODO learn about matplotlib
