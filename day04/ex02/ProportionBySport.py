import pandas as pd


def __proportionbysport__(df: pd.DataFrame, year: int, sport: str, gender: str) -> float:
    df_one_sport = df[(df['Sex'] == gender) & (df['Year'] == year) & (df['Sport'] == sport)]\
        .drop_duplicates(subset='Name', keep='first')
    df_all_sport = df[(df['Sex'] == gender) & (df['Year'] == year)]\
        .drop_duplicates(subset='Name', keep='first')
    return df_one_sport['Sport'].count() / df_all_sport['Sport'].count()


from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(__proportionbysport__(data, 2004, 'Tennis', 'F'))
