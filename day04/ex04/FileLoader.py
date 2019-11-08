import os
import pandas as pd


class FileLoader:
    def load(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            df = pd.read_csv(path)
            print(f'Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}')
        else:
            df = None
        return df

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))

# fl = FileLoader()
# dataframe = fl.load('../resources/athlete_events.csv')
# fl.display(dataframe, 5)
