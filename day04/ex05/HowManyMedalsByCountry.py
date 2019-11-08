import pandas as pd


def howmanymedalsbycountry(df: pd.DataFrame, country: str) -> dict:
    my_dict = {}
    df_bis = df[df['Team'] == country][['Year', 'Medal', 'Event']]
    for year in df_bis['Year'].drop_duplicates().sort_values():
        # return one medal for one event
        my_dict[year] = {'G': df_bis[['Medal', 'Event']][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Gold')].
            drop_duplicates(subset='Event')['Medal'].count(),
                         'S': df_bis[['Medal', 'Event']][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Silver')].
            drop_duplicates(subset='Event')['Medal'].count(),
                         'B': df_bis[['Medal', 'Event']][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Bronze')].
            drop_duplicates(subset='Event')['Medal'].count()}
        # return one medal for one athlete
        # my_dict[year] = {'G': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Gold')].count(),
        #                  'S': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Silver')].count(),
        #                  'B': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Bronze')].count()}
    return my_dict


# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../resources/athlete_events.csv')
# print(howmanymedalsbycountry(data, 'France'))
