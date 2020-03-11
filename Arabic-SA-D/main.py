import regexarabic as ra
import craweltweet as ct


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
    # Function to extract data based on top trend on each gulf states on one DataFrame
    ct.clean_ALL['clean_tweet_SA'] = ct.df_SA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_SA'].to_csv('files\clean_SA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_AE'] = ct.df_AE['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_AE'].to_csv('files\clean_AE.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_OM'] = ct.df_OM['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_OM'].to_csv('files\clean_OM.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_QA'] = ct.df_QA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_QA'].to_csv('files\clean_QA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_BH'] = ct.df_BH['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_BH'].to_csv('files\clean_BH.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_KW'] = ct.df_KW['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_KW'].to_csv('files\clean_KW.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    clean()

   # ---
