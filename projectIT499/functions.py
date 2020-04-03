"""
    Here have three thing:
1- function for extended tweet
2- function for check spam
3- function for combine file
"""
spam = open('spam_lexicon.txt', encoding='utf-8').read().split('\n')
spam = [word for word in spam if word.strip()]


# to get full_text from tweet or retweet
def GetFullTeet(tweet):
    try:
        return tweet.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return tweet.full_text


# To check if tweet have spam return 'spam' if not return tweet.
def has_spam(tweet):
    for word in spam:
        if word in tweet:
            # print('is spam')
            tweet = 'spam'
            return tweet  #
    # print('is not spam')
    return tweet

# to combine all data in one csv file
import pandas as pd
from glob import glob


def marge():
    stock_files = sorted(glob('data_*.csv'))  # to stock all file together
    print(stock_files)  # print file name in list format

    # read all the file and marge it together
    margeCSV = pd.concat((pd.read_csv(file, encoding='utf-16', sep='\t') for file in stock_files),
                         ignore_index=True, sort=True, axis=1)
    print(margeCSV)  # print data frame

    colnames = ["Tweets_AE", "sentiment_AE", "Tweets_BH", "sentiment_BH", "Tweets_KW", "sentiment_KW",
                "Tweets_OM", "sentiment_OM", "Tweets_QA", "sentiment_QA", "Tweets_SA", "sentiment_SA"]

    margeCSV.columns = colnames
    margeCSV.to_csv('marged.csv', encoding='utf-16', sep='\t', index=False)  # save in one file
