

# to get full_text from tweet or retweet
def GetFullTeet(tweet):
    try:
        return tweet.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return tweet.full_text
