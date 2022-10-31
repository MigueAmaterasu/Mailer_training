import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date, datetime
import os


class Email:
    def __init__(self):
        pass

    def sendEmail(self):
        msg = MIMEMultipart()
        msg['Subject'] = "REPORTE DE INCIDENCIAS GRUPO TI MEXICO"
        body = """
                    Buen dia, se adjunta reporte de discrepancias del documento proveniente del equipo de ventas y los datos\nfaltantes\nGracias\nIng.luis carlos cabañas cruz
                """
        msg.attach(MIMEText(body, 'plain'))

        ejecucion = datetime.now()
        today = ejecucion.strftime('%Y%m%d')

        files_verify = [os.path.isfile(f'report\csv\{today}.csv'), os.path.isfile(
            f'report\excel\{today}.xlsx')]
        file_data = [f'report\csv\{today}.csv', f'report\excel\{today}.xlsx']


        for file in range(len(files_verify)):
            for document in range(len(file_data)):
                if file == True:
                    nombre_archivo = file_data[document]
                    part = file_data[document].split(sep='\\')
                
                    adjunto = open(nombre_archivo, "rb")
                    parte = MIMEBase('application', 'octet-stream')
                    parte.set_payload((adjunto).read())
                    encoders.encode_base64(parte)
                    parte.add_header('Content-Disposition',"attachment;filename= %s" % str(part[2]))
                    msg.attach(parte)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("luiscabanas919@gmail.com", "sgsyjifzrxjiipim")
        texto = msg.as_string()
        server.sendmail("luiscabanas919@gmail.com", "luiscabanas919@gmail.com", texto)
        server.quit()

