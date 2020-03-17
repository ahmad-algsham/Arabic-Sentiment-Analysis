import functions as ff
import pandas as pd
from tweepy import Cursor
from tweepy import api, API
import tweepy

import kays_twitter

auth = tweepy.OAuthHandler(kays_twitter.consumer_key, kays_twitter.consumer_secret)
auth.set_access_token(kays_twitter.access_key, kays_twitter.access_secret)
api: API = API(auth)

def get_saudi_arabia(result_SA):

    result_SA = result_SA
    df_SA = pd.DataFrame()
    i = 0
    # extract tweet from top trend in Saudi Arabia
    for trend in result_SA[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in SA: ", data)

    for tweet in Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_SA.loc[i, 'Tweets'] = ff.GetFullTeet(tweet)
        df_SA.to_csv('{}.csv'.format('DD_SA'), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 20:
            break
        else:
            pass
    return df_SA
