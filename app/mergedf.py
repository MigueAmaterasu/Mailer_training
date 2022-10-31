from ast import Lambda
from csv import writer
from datetime import date, datetime
import pandas as pd
from pandas import ExcelWriter
from psycopg2 import Date


class VerifyData:

    def __init__(self):
        pass

    def findData(self, d1, d2):

        df3 = d1.merge(d2, how='outer', indicator=True)
        df3.loc[lambda x: x['_merge'] == 'both']
        result_data = df3[(df3['_merge'] != 'both')].drop('_merge', axis=1)

        ejecucion = datetime.now()
        ejecucion_f = ejecucion.strftime('%d/%m/%Y %H:%M:%S')
        today = ejecucion.strftime('%Y%m%d')

        if (len(result_data) == 0):
    
            TOTAL = pd.DataFrame({"Informacion de datos": 
                ("No se encontraron datos diferentes", "En los dos dataframes")})
            TOTAL.to_csv(f'report/csv/{today}.csv')

            page1 = pd.DataFrame({"Numero de registros":
                (f' Se encontraron el numero 0 de datos incongruentes', 
                f' Se encontraron el numero {len(result_data)} de datos incongruentes')})
            page2 = pd.DataFrame({"Informacion de datos": 
                ("No se encontraron datos diferentes", "En los dos dataframes")})
            
            with ExcelWriter(f'report/excel/{today}.xlsx') as writer:
                page1.to_excel(writer, 'PAGE 1', index=False)
                page2.to_excel(writer, 'PAGE 2', index=False)
                
        else:
            result_data.to_csv(f'report/csv/{today}.csv')
            page1 = pd.DataFrame({"Numero de registros": (
                f' Se encontraron el numero {len(result_data)} de datos incongruentes', f'fecha: {ejecucion_f}')})
            page2 = pd.DataFrame(result_data.tail(2000))

            with ExcelWriter(f'report/excel/{today}.xlsx') as writer:
                page1.to_excel(writer, 'PAGE 1', index=False)
                page2.to_excel(writer, 'PAGE 2', index=False)
