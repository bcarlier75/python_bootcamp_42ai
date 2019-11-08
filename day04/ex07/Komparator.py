import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def compare_histograms(self, categorical_var: str, numerical_var: str):
        nb = len(self.df[categorical_var].drop_duplicates())

        f, ax = plt.subplots(1, nb + 1, figsize=(9, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            ax[i].set_title(f'Histogram for {categorical_var} with value {elem}')
            sns.distplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(),
                         kde=False, rug=False, ax=ax[i], hist=True,
                         hist_kws={"alpha": 1, "color": "dodgerblue"})
        # bonus, last histogram plot is the overlapping of all preceding histograms
        for elem in self.df[categorical_var].drop_duplicates():
            ax[nb].set_title(f'Histogram for {categorical_var} with value {elem}')
            sns.distplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(),
                         kde=False, rug=False, ax=ax[nb], hist=True,
                         hist_kws={"alpha": 0.5})
        plt.show()

    def density(self, categorical_var: str, numerical_var: str):
        plt.figure(figsize=(6, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            sns.kdeplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem)
        plt.title(f'Density for {categorical_var}')
        plt.show()

    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        nb = len(self.df[categorical_var].drop_duplicates())
        f, ax = plt.subplots(1, nb, figsize=(9, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            ax[i].set_title(f'Boxplot for {categorical_var} with value {elem}')
            sns.boxplot(x=self.df[numerical_var][self.df[categorical_var] == elem].dropna(),
                        ax=ax[i], color='dodgerblue')
        plt.show()


# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../resources/athlete_events.csv')
# kp = Komparator(data)
# kp.compare_box_plots("Sex", "Height")
# kp.density("Sex", "Height")
# kp.compare_histograms("Sex", "Height")
