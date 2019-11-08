import pandas as pd


def howmanymedalsbycountry(df: pd.DataFrame, country: str) -> dict:
    my_dict = {}
    df_bis = df[(df['Team'] == country) & (df['Event'].str.contains('Team'))][['Year', 'Medal']]
    for year in df_bis['Year'].drop_duplicates().sort_values():
        my_dict[year] = {'G': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Gold')].count(),
                         'S': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Silver')].count(),
                         'B': df_bis['Medal'][(df_bis['Year'] == year) & (df_bis['Medal'] == 'Bronze')].count()}
    return my_dict


# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../resources/athlete_events.csv')
# print(howmanymedalsbycountry(data, 'France'))
