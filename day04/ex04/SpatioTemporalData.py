import pandas as pd


class SpatioTemporalData:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def when(self, location) -> list:
        return list(self.dataframe[self.dataframe['City'] == location]['Year'].drop_duplicates())

    def where(self, date):
        return list(self.dataframe[self.dataframe['Year'] == date]['City'].drop_duplicates())


# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../resources/athlete_events.csv')
# sp = SpatioTemporalData(data)
# print(sp.where(1896))
# print(sp.where(2016))
# print(sp.when('Athina'))
# print(sp.when('Paris'))
