import pandas as pd


class VerifyData:

    def __init__(self):
        pass

    def findData(self, d1, d2):
        df3 = d1.merge(
            d2, how='outer', indicator=True).loc[lambda x: x['_merge'] == 'left_only']
        #d2.merge(d1, how='outer', indicator=True).loc[lambda x:x['_merge'] == 'right_only']
        df3.to_csv('Incidencias.csv')
        print(len(df3))
