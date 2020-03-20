import itertools
import re
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer

"""

This function is to normalize the arabic tweet
That have two functions remove and harakat

"""


def remove(argword):
    """
    This function is to remove
    1- (@)mention and (#)hashtag
    2- links
    3- convert to lowercase
    4- Punctuation
    5- White spaces
    6- consecutive duplicate

    :param argword:
    :return:
          """

    argword = ' '.join(re.sub(r'[@#][\w+.-]+'  # To remove @ and # 
                              r'|(\d+)|'  # To remove numbers
                              r'(https?:\/\/.*[\r\n]*)'  # To remove links
                              r'|([A-Za-z]+)'
                              , ' ', argword).split())
    argword = ' '.join(re.sub(r'(\w+_\w+)', '', argword).split())

    argword = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                         u"\U0001F680-\U0001F6FF"  # transport & map symbols
                         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                         u"\U00002702-\U000027B0"
                         u"\U000024C2-\U0001F251" "]+", flags=re.UNICODE).sub(r'', argword)
    argword = ' '.join(re.sub(r'(?<![\w\-])\w(?![\w\-])', '', argword).split())  # delete any single char

    # argword = re.sub('SPAM', '', argword)
    argword = argword.translate(str.maketrans("", "", string.punctuation))  # Punctuation removal
    argword = argword.strip()  # White spaces removal

    return argword


def harakat(har):
    """
    This function is to remove
    1- Variations of letter alif
    2- Variations of letter waw
    3- Add nuktas to tama'buta
    4- Diacritics
    5- consecutive duplicate

    :param har:
    :return har:
    """

    har = ' '.join(re.sub('[آ|أ|إ|آ]', 'ا', har).split())
    har = ' '.join(re.sub('[ؤ]', 'و', har).split())
    har = ' '.join(re.sub('[ه]$', 'ة', har).split())
    har = ' '.join(re.sub('[ى]', 'ي', har).split())
    har = ' '.join(re.sub('[ٍ|َ|ُ|ِ|ّ|ْ|ً]', '', har).split())
    har = ''.join(i for i, _ in itertools.groupby(har))  # Remove consecutive duplicate

    return har


def WordsFiltires(tokenstem):
    """

    :param tokenstem:
    :return WordsFiltires:
    """
    stopWords = set(stopwords.words('arabic'))
    stemmed_word = []
    WordsFiltires = []
    words = word_tokenize(tokenstem)
    st = ISRIStemmer()

    for word in words:
        if word in stopWords:
            continue
        stemmed_word.append(st.stem(word))
        WordsFiltires = ' '.join(stemmed_word)

    return WordsFiltires


# text = "اححححب خالد &ب تت الس 90ة ب🤷🏻‍♀️​  # #نات بغت_تلنت   "
# print(harakat(remove(text)))