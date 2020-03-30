import pandas as pd
from tweepy import Cursor
from tweepy import api, API
import tweepy

from projectIT499 import kays_twitter, functions as ff

auth = tweepy.OAuthHandler(kays_twitter.consumer_key, kays_twitter.consumer_secret)
auth.set_access_token(kays_twitter.access_key, kays_twitter.access_secret)
api: API = API(auth)


def get_data_to_frame(result_location, file_name_trend):
    df = pd.DataFrame()
    trend_df = pd.DataFrame()
    i = 0

    # extract top trend
    for trend in result_location[0]["trends"][:5]:
        print(i, end='\r')
        trend_df.loc[i, file_name_trend] = trend['name']
        trend_df.to_csv('{}.csv'.format(file_name_trend), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    data_name = trend_df.iloc[0]
    print("TOP", data_name)
    datalist = trend_df[file_name_trend].to_list()
    data = datalist[0]

    # extract tweet from top trend
    for tweet in Cursor(api.search, q=data, wait_on_rate_limit=True, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df.loc[i, 'Tweets'] = ff.has_spam(ff.GetFullTeet(tweet))
        i += 1
        if i == 360:   # to avoid rate limit we set at 360 where is (280 * 360 = 100,800 character)
            break
        else:
            pass

    spamfilter = (df['Tweets'] != 'spam')  # to filter spam tweets
    return df[spamfilter]
