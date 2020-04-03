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
    2- digits and links
    3- emoji
    4- non ararbic words
    5- Punctuation
    6- White spaces

    :param argword:
    :return:
          """

    argword = ' '.join(re.sub(r'[@#][\w+.-]+'  # To remove @ and # 
                              r'|(\d+)|'  # To remove numbers
                              r'(https?:\/\/.*[\r\n]*)'  # To remove links
                              r'|([A-Za-z]+)'
                              , ' ', argword).split())
    argword = ' '.join(re.sub(r'(\w+_\w+)', ' ', argword).split())
    argword = ' '.join(re.sub(r'[؟]|[،]|[©]', ' ', argword).split())

    argword = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons   [ 😀-🙏 🌀-🗿 🚀-🛿 🇠-🇿 ✂-➰ Ⓜ-🉑 ]+
                         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                         u"\U0001F680-\U0001F6FF"  # transport & map symbols
                         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                         u"\U00002702-\U000027B0"
                         u"\U000024C2-\U0001F251"
                         u"\U0001f926-\U0001f937"
                         u"\U00010000-\U0010ffff"
                         u"\u200d"
                         u"\u2640-\u2642"
                         u"\u2600-\u2B55"
                         u"\u23cf"
                         u"\u23e9"
                         u"\u231a"
                         u"\u3030"
                         u"\ufe0f"
                         u"\u2069"
                         u"\u2066"
                         u"\u200c"
                         u"\u2068"
                         u"\u2067" "]+", flags=re.UNICODE).sub(r'', argword)

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
    har = ' '.join(re.sub('[ٍ|َ|ُ|ِ|ّ|ْ|ً]', ' ', har).split())
    har = ''.join(i for i, _ in itertools.groupby(har))  # Remove consecutive duplicate
    har = ' '.join(re.sub(r'(?<![\w\-])\w(?![\w\-])', ' ', har).split())  # delete any single char

    return har


def WordsFiltires(tokenstem):
    """
    This function is to remove
    1- remove stop words
    2- stemmer

    :param tokenstem:
    :return WordsFiltires:
    """
    stopWords = set(stopwords.words('arabic'))
    stemmed_word = []
    WordsFiltires = []
    words = word_tokenize(tokenstem)
    st = ISRIStemmer()

    # stop words with stemming
    for word in words:
        if word in stopWords:
            continue
        stemmed_word.append(st.stem(word))
        WordsFiltires = ' '.join(stemmed_word)

    return WordsFiltires

    # only stop words
    # for w in words:
    #     if w not in stopWords:
    #         WordsFiltires.append(w)
    #
    # # print(' '.join(WordsFiltires))
    # wf = ' '.join(WordsFiltires)
    # return wf

    # large data set for stop words
    # File = open('list.txt', encoding='utf-8')
    # # print(File.read())
    # stopWordslist = word_tokenize(File.read())
    #
    # # WordsFiltires = []
    #
    # words = word_tokenize(tokenstem)
    #
    # for w in words:
    #     if w not in stopWords:
    #         if w not in stopWordslist:
    #             WordsFiltires.append(w)
    #         # WordsFiltires.append(w)
    # wf = ' '.join(WordsFiltires)
    # return wf
