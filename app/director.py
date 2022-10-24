from resources.data_cv import Data_Cv
from resources.data_bd import Data_Bd
from app.mailer import suma
from app.mergedf import VerifyData

import pandas as pd


class GoProcess:
    def __init__(self):

        pass

    def getDataCv(self):
        Data_Cv().getInfoCsv()

    def getDataDb(self):
        Data_Bd().get_InfoDb()

    def getDataFailet(self):

        VerifyData().findData(Data_Cv().getInfoCsv(),Data_Bd().get_InfoDb())
