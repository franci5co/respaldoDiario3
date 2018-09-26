#/usr/bin/python
import ftplib
import time
from respaldoDiario_config import *

session = ftplib.FTP('104.248.214.110','ftpbackup','backupaservices')
file = open('final.txt','a')
#file.write( '\r\n' + time.strftime("%D-%b-%d %H:%M:%S")+"\r\n")
file.write ( '\n' + time.strftime("%d-%b-%Y %H:%M:%S")+"\n")
file.close()
file = open('final.txt','r')
session.storbinary('STOR ' + sid+'.txt', file)
file.close()
session.quit()
