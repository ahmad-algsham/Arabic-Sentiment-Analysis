import regexarabic as ra
import craweltweet as ct


# --------------------------------------import from craweltweet---------------------------------------------------------
def main():
    # function to extract trends from each gulf state
    ct.trending(file_name_trend_SA="TRENDS_SA", file_name_trend_AE="TRENDS_AE", file_name_trend_OM="TRENDS_OM",
                file_name_trend_QA="TRENDS_QA", file_name_trend_BH="TRENDS_BH", file_name_trend_KW="TRENDS_KW", )

    # function to extract (data based on top trend) from each gulf state
    ct.data_trend(file_name_data_sa="DATA_SA", file_name_data_ae="DATA_AE", file_name_data_om="DATA_OM",
                  file_name_data_qa="DATA_QA", file_name_data_bh="DATA_BH", file_name_data_kw="DATA_KW", )


# --------------------------------------import from regexarabic---------------------------------------------------------
def clean():
    # Function to extract data based on top trend on each gulf states on one DataFrame
    ct.clean_ALL['clean_tweet_SA'] = ct.df_SA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_SA'].to_csv('clean_SA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_AE'] = ct.df_AE['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_AE'].to_csv('clean_AE.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_OM'] = ct.df_OM['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_OM'].to_csv('clean_OM.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_QA'] = ct.df_QA['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_QA'].to_csv('clean_QA.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_BH'] = ct.df_BH['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_BH'].to_csv('clean_BH.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')

    ct.clean_ALL['clean_tweet_KW'] = ct.df_KW['Tweets'].apply(lambda x: ra.remove(ra.harakat(ra.WordsFiltires(x))))
    ct.clean_ALL['clean_tweet_KW'].to_csv('clean_KW.csv', encoding='utf-16', sep='\t', index=False)
    print('Done')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    clean()
