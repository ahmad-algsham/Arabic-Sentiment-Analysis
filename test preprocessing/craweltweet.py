import pandas as pd
import tweepy
from tweepy import api, API

# import the keys(consumer and access)
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api: API = tweepy.API(auth)

# create empty DataFrame to insert (trends) from each gulf state.
trend_df_sa = pd.DataFrame()
trend_df_ae = pd.DataFrame()
trend_df_om = pd.DataFrame()
trend_df_qa = pd.DataFrame()
trend_df_bh = pd.DataFrame()
trend_df_kw = pd.DataFrame()

# create empty DataFrame to insert (data based on top trend) from each gulf state.
df_SA = pd.DataFrame()
df_AE = pd.DataFrame()
df_OM = pd.DataFrame()
df_QA = pd.DataFrame()
df_BH = pd.DataFrame()
df_KW = pd.DataFrame()

# connect to country id.
result_SA = api.trends_place(23424938)
result_AE = api.trends_place(23424738)
result_OM = api.trends_place(23424898)
result_QA = api.trends_place(23424930)
result_BH = api.trends_place(23424753)
result_KW = api.trends_place(23424870)

# create empty dataFrame to save all clean data gulf state in single DataFrame
clean_ALL = pd.DataFrame()

# function to extract trends from each gulf state
def trending(file_name_trend_SA, file_name_trend_AE, file_name_trend_OM,
             file_name_trend_QA, file_name_trend_BH, file_name_trend_KW):
    i = 0

    # trend from Saudi Arabia
    print("Trend in Saudi Arabia: ")
    for trend in result_SA[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_sa.loc[i, 'SA'] = trend['name']
        trend_df_sa.to_csv('{}.csv'.format(file_name_trend_SA), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    # trend from United Arab Emirates
    print("trend in United Arab Emirates: ")
    for trend in result_AE[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_ae.loc[i, 'AE'] = trend['name']
        trend_df_ae.to_csv('{}.csv'.format(file_name_trend_AE), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    # trend from Oman
    print("trend in Oman: ")
    for trend in result_OM[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_om.loc[i, 'OM'] = trend['name']
        trend_df_om.to_csv('{}.csv'.format(file_name_trend_OM), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    # trend from Qatar
    print("trend in Qatar: ")
    for trend in result_QA[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_qa.loc[i, 'QA'] = trend['name']
        trend_df_qa.to_csv('{}.csv'.format(file_name_trend_QA), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    # trend from Bahrain
    print("trend in Bahrain: ")
    for trend in result_BH[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_bh.loc[i, 'BH'] = trend['name']
        trend_df_bh.to_csv('{}.csv'.format(file_name_trend_BH), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass

    # trend from Kuwait
    print("trend in Kuwait: ")
    for trend in result_KW[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')
        trend_df_kw.loc[i, 'KW'] = trend['name']
        trend_df_kw.to_csv('{}.csv'.format(file_name_trend_KW), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 5:
            break
        else:
            pass


# to get full_text from tweet or retweet
def GetFullTeet(tweet):
    try:
        return tweet.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return tweet.full_text


# function to extract (data based on top trend) from each gulf state
def data_trend(file_name_data_sa,
               # file_name_data_ae, file_name_data_om,
               # file_name_data_qa, file_name_data_bh, file_name_data_kw,
               ):

    i = 0
    # extract tweet from top trend in Saudi Arabia
    for trend in result_SA[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in SA: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_SA.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_SA.loc[i, 'User'] = tweet.user.name
        df_SA.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_SA.loc[i, 'User_followers'] = tweet.user.followers_count
        df_SA.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_SA.loc[i, 'User_location'] = tweet.user.location
        df_SA.loc[i, 'rt_count'] = tweet.retweet_count
        df_SA.loc[i, 'tweet_data'] = tweet.created_at
        df_SA.to_csv('{}.csv'.format(file_name_data_sa), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

    # extract tweet from top trend in United Arab Emirates
    i = 0
    for trend in result_AE[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in AE: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_AE.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_AE.loc[i, 'User'] = tweet.user.name
        df_AE.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_AE.loc[i, 'User_followers'] = tweet.user.followers_count
        df_AE.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_AE.loc[i, 'User_location'] = tweet.user.location
        df_AE.loc[i, 'rt_count'] = tweet.retweet_count
        df_AE.loc[i, 'tweet_data'] = tweet.created_at
        df_AE.to_csv('{}.csv'.format(file_name_data_ae), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

    # extract tweet from top trend in Oman
    i = 0
    for trend in result_OM[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in OM: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_OM.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_OM.loc[i, 'User'] = tweet.user.name
        df_OM.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_OM.loc[i, 'User_followers'] = tweet.user.followers_count
        df_OM.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_OM.loc[i, 'User_location'] = tweet.user.location
        df_OM.loc[i, 'rt_count'] = tweet.retweet_count
        df_OM.loc[i, 'tweet_data'] = tweet.created_at
        df_OM.to_csv('{}.csv'.format(file_name_data_om), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

    # extract tweet from top trend in Qatar
    i = 0
    for trend in result_QA[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in QA: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_QA.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_QA.loc[i, 'User'] = tweet.user.name
        df_QA.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_QA.loc[i, 'User_followers'] = tweet.user.followers_count
        df_QA.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_QA.loc[i, 'User_location'] = tweet.user.location
        df_QA.loc[i, 'rt_count'] = tweet.retweet_count
        df_QA.loc[i, 'tweet_data'] = tweet.created_at
        df_QA.to_csv('{}.csv'.format(file_name_data_qa), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

    # extract tweet from top trend in Bahrain
    i = 0
    for trend in result_BH[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in BH: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_BH.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_BH.loc[i, 'User'] = tweet.user.name
        df_BH.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_BH.loc[i, 'User_followers'] = tweet.user.followers_count
        df_BH.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_BH.loc[i, 'User_location'] = tweet.user.location
        df_BH.loc[i, 'rt_count'] = tweet.retweet_count
        df_BH.loc[i, 'tweet_data'] = tweet.created_at
        df_BH.to_csv('{}.csv'.format(file_name_data_bh), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

    # extract tweet from top trend in Kuwait
    i = 0
    for trend in result_KW[0]["trends"][:1]: data = trend["name"]
    print("Top trend is in KW: ", data)
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='ar', tweet_mode='extended').items():
        print(i, end='\r')
        df_KW.loc[i, 'Tweets'] = GetFullTeet(tweet)
        df_KW.loc[i, 'User'] = tweet.user.name
        df_KW.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df_KW.loc[i, 'User_followers'] = tweet.user.followers_count
        df_KW.loc[i, 'User_friends_count'] = tweet.user.friends_count
        df_KW.loc[i, 'User_location'] = tweet.user.location
        df_KW.loc[i, 'rt_count'] = tweet.retweet_count
        df_KW.loc[i, 'tweet_data'] = tweet.created_at
        df_KW.to_csv('{}.csv'.format(file_name_data_kw), encoding='utf-16', sep='\t', index=False)
        i += 1
        if i == 10:
            break
        else:
            pass

