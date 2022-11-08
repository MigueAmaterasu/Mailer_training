import pandas as pd
import os
import sys

class Data_Cv:

    def __init__(self):
        pass

    def getInfoCsv(self):

        if os.path.isfile('download_files\Bakery.csv') == True:
            datos = pd.read_csv(r'download_files\Bakery.csv')
            return datos
        else:
            print("NOT FOUND")
            sys.exit()  