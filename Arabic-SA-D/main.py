import regexarabic as ra
import craweltweet as ct
import getsentiment as gs

import os

dirName = f'../Arabic-SA-D/files'
if not os.path.exists(dirName):
    # To check if
    # - directory is created or not
    # if not will created automatically
    os.makedirs(dirName, exist_ok=True)


# --------------------------------------import from craweltweet---------------------------------------------------------
def main():
    # function to extract trends from each gulf state
    ct.trending(file_name_trend_SA="files\TRENDS_SA", file_name_trend_AE="files\TRENDS_AE",
                file_name_trend_OM="files\TRENDS_OM", file_name_trend_QA="files\TRENDS_QA",
                file_name_trend_BH="files\TRENDS_BH", file_name_trend_KW="files\TRENDS_KW", )

    # function to extract (data based on top trend) from each gulf state
    ct.data_trend(file_name_data_sa="files\DATA_SA", file_name_data_ae="files\DATA_AE",
                  file_name_data_om="files\DATA_OM", file_name_data_qa="files\DATA_QA",
                  file_name_data_bh="files\DATA_BH", file_name_data_kw="files\DATA_KW", )


# --------------------------------------import from regexarabic---------------------------------------------------------
def clean():
    # Function to clean data
    ct.clean_SA['clean_tweet_SA'] = ct.df_SA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_SA.to_csv('files\clean_SA.csv', encoding='utf-16', sep='\t', index=False)
    print('\nDone clean SA')

    ct.clean_AE['clean_tweet_AE'] = ct.df_AE['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_AE.to_csv('files\clean_AE.csv', encoding='utf-16', sep='\t', index=False)
    print('Done clean AE')

    ct.clean_OM['clean_tweet_OM'] = ct.df_OM['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_OM.to_csv('files\clean_OM.csv', encoding='utf-16', sep='\t', index=False)
    print('Done clean OM')

    ct.clean_QA['clean_tweet_QA'] = ct.df_QA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_QA.to_csv('files\clean_QA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done clean QA')

    ct.clean_BH['clean_tweet_BH'] = ct.df_BH['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_BH.to_csv('files\clean_BH.csv', encoding='utf-16', sep='\t', index=False)
    print('Done clean BH')

    ct.clean_KW['clean_tweet_KW'] = ct.df_KW['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_KW.to_csv('files\clean_KW.csv', encoding='utf-16', sep='\t', index=False)
    print('Done clean KW')
    print()


# ---------------------------------------import from getsentiment-------------------------------------------------------

def sentiment_Analyze():
    # Function to get sentiment data
    ct.clean_SA['sentiment_SA'] = ct.clean_SA['clean_tweet_SA'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_SA.to_csv('files\clean_SA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done classify SA')

    ct.clean_AE['sentiment_AE'] = ct.clean_AE['clean_tweet_AE'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_AE.to_csv('files\clean_AE.csv', encoding='utf-16', sep='\t', index=False)
    print('Done classify AE')

    ct.clean_OM['sentiment_OM'] = ct.clean_OM['clean_tweet_OM'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_OM.to_csv('files\clean_OM.csv', encoding='utf-16', sep='\t', index=False)
    print('Done classify OM')

    ct.clean_QA['sentiment_QA'] = ct.clean_QA['clean_tweet_QA'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_QA.to_csv('files\clean_QA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done classify QA')

    ct.clean_BH['sentiment_BH'] = ct.clean_BH['clean_tweet_BH'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_BH.to_csv('files\clean_BH.csv', encoding='utf-16', sep='\t', index=False)
    print('Done classify BH')

    ct.clean_KW['sentiment_KW'] = ct.clean_KW['clean_tweet_KW'].apply(lambda x: gs.analyze_sentiment(x))
    ct.clean_KW.to_csv('files\clean_KW.csv', encoding='utf-16', sep='\t', index=False)
    print("Done classify KW")
    print('Done analyze')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    clean()
    sentiment_Analyze()
