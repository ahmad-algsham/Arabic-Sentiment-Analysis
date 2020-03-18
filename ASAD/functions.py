
spam = open('spam_lexicon.txt', encoding='utf-8').read().split('\n')
spam = [word for word in spam if word.strip()]


# to get full_text from tweet or retweet
def GetFullTeet(tweet):
    try:
        return tweet.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return tweet.full_text


def has_spam(tweet):
    for word in spam:
        if word in tweet:
            print('is spam')
            tweet = 'spam'
            return tweet
    print('is not spam')
    return tweet
