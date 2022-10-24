from ast import Lambda
from csv import writer
from datetime import datetime
import pandas as pd
import xlsxwriter


class VerifyData:

    def __init__(self):
        pass

    def findData(self, d1, d2):

        df3 = d1.merge(d2, how='outer', indicator=True)
        df3.loc[lambda x: x['_merge'] == 'both']
        result_data = df3[(df3['_merge'] != 'both')].drop('_merge', axis=1)

        result = pd.DataFrame(result_data)
        result.to_csv('reporte_incidencias.csv')

        # ----------------------------------------------------------------------------------

        # cree un escritor de Pandas Excel usando XlsxWriter como el escritor del motor

        ejecucion = datetime.now()
        ejecucion_f = ejecucion.strftime('%d/%m/%Y %H:%M:%S')

        # page 1 to excel
        number = f' Se encontraron el numero {len(result)} de datos incongruentes'
        second = f'fecha: {ejecucion_f}'

        # page 2 to excel
        data = result.tail(4)

        df1 = pd.DataFrame({'dataset': [number, second]})
        df2 = pd.DataFrame(data)

        # cree un escritor de Pandas Excel usando XlsxWriter como el escritor del motor
        libro = pd. ExcelWriter(' dataframes.xlsx ', motor=' xlsxwriter ')

        # escribe cada DataFrame en una hoja específica
        df1. to_excel(libro, sheet_name=' primer conjunto de datos ')
        #df2. to_excel(libro, sheet_name=' segundo conjunto de datos ')

        # cierre el escritor de Pandas Excel y genere el archivo de Excel
        libro.save()
