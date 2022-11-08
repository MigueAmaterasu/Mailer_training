import pysftp
import fnmatch
import os


# It connects to a database, creates a cursor, and then executes a query.


class Sftp_Download:

    def __init__(self):
        self.remote_path="/pub/example"
        self.local_path="download_files"
        #file_extension=".png"
        self.cnopts=pysftp.CnOpts()
        self.cnopts.hostkeys=None

    def downloadFile(self):
        with pysftp.Connection( host="test.rebex.net",password="password",username="demo", cnopts=self.cnopts, port=22) as sftp:
        #for filename in sftp.listdir(remote_path):
        #    print(filename)
        #    if fnmatch.fnmatch(filename,"*"+file_extension):
           sftp.get(os.path.join(self.remote_path,"imap-console-client.png"),localpath=self.local_path+"/"+"imagen.png")
           sftp.close()
        print("archivo descargado")
        

