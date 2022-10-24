import pandas as pd


class Data_Cv:

    def __init__(self):
        pass

    def getInfoCsv(self):
        datos = pd.read_csv(r'resources\amazon_data.csv')
        return datos
