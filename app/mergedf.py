from ast import Lambda
from csv import writer
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter


class VerifyData:

    def __init__(self):
        pass

    def findData(self, d1, d2):

        df3 = d1.merge(d2, how='outer', indicator=True)
        df3.loc[lambda x: x['_merge'] == 'both']
        result_data = df3[(df3['_merge'] != 'both')].drop('_merge', axis=1)

        result = pd.DataFrame(result_data)

        ejecucion = datetime.now()
        ejecucion_f = ejecucion.strftime('%d/%m/%Y %H:%M:%S')

        # page 1 to excel
        number = f' Se encontraron el numero {len(result)} de datos incongruentes'
        number2 = f' Se encontraron el numero 0 de datos incongruentes'
        second = f'fecha: {ejecucion_f}'

        if (len(result) == 0):
            TOTAL = pd.DataFrame({"Informacion de datos": (
                "No se encontraron datos diferentes", "En los dos dataframes")})
            TOTAL.to_csv('reporte_incidencias.csv')

            page1 = pd.DataFrame({"Numero de registros": (number2, second)})
            page2 = pd.DataFrame({"Informacion de datos": (
                "No se encontraron datos diferentes", "En los dos dataframes")})

            with ExcelWriter('prueba.xlsx') as writer:
                page1.to_excel(writer, 'PAGE 1', index=False)
                page2.to_excel(writer, 'PAGE 2', index=False)
        else:

            result.to_csv('reporte_incidencias.csv')

            page1 = pd.DataFrame({"Numero de registros": (number, second)})
            page2 = pd.DataFrame(result.tail(2000))

            with ExcelWriter('reporte_incidencias.xlsx') as writer:
                page1.to_excel(writer, 'PAGE 1', index=False)
                page2.to_excel(writer, 'PAGE 2', index=False)
