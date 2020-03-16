from textblob_ar import TextBlob


# analysis the sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'natural'
    else:
        return 'negative'


hi = "دري ليش فهم غلط"
print(analyze_sentiment(hi))

