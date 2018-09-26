#!/usr/bin/env python
# Ejemplo de log de respaldo exitoso
# 2018-05-11T19:02:24-03:00  P003305 1635137cde0 INFO  BACKUP SAVE DATA finished successfully

# RESUELTO Falta resolver problema cuando hay mas de un respaldo por dia, exitoso o con error.
# Falta eliminar hora de respaldo en caso de que no haya

from __future__ import with_statement

from respaldoDiario_config import *
import datetime
import os


def buscaBackup(dia, respaldo, cont_exito, cont_error):
    for line in f:
        if hoy in line and "BACKUP" in line and "ERROR" in line:
            respaldo = True
            error = True
            fecha = line[:10]
            hora = line[11:19]
            final.write(cliente + "\n")
            final.write(sid + "\n")
            final.write(hostname + "\n")
            final.write(fecha + "\n")
            final.write(hora + "\n")
            final.write("NO\n")
            log.write(line)
            cont_error += 1
        if hoy in line and "BACKUP" in line and "successfully" in line:
            log.write(line)
            respaldo = True
            error = False
            fecha = line[:10]
            hora = line[11:19]
            final.write(cliente + "\n")
            final.write(sid + "\n")
            final.write(hostname + "\n")
            final.write(fecha + "\n")
            final.write(hora + "\n")
            final.write("YES\n")
            cont_exito += 1
    return cont_exito + cont_error


respaldo = False
error = False
# print hostname
# print sid
# print backup_log_path
# print cliente
cont_error = 0
cont_exito = 0
f = open(backup_log_path, "r")
log = open("/root/logBK.log", "a")
final = open("final.txt", "w")
cont = 0

hoy = (datetime.date.today())
hoy = hoy.strftime("%Y-%m-%d")

ayer = (datetime.date.today() - datetime.timedelta(1))
ayer = ayer.strftime("%Y-%m-%d")

sumaRespaldos = buscaBackup(hoy, respaldo, cont_exito, cont_error)

if respaldo == False:

    #        final.write( cliente + "\n")
    #		 final.write( sid + "\n")
    #        final.write( hostname +  "\n")
    #        final.write(hoy +"\n")
    #        final.write( time.strftime("%H:%M:%S")+"\n")
    #        final.write("NADA\n")
    # mensaje += "No hay respaldo del " + hoy
    buscaBackup(ayer, respaldo, cont_exito, cont_error)
    if respaldo == False:
        final.write(cliente + "\n")
        final.write(sid + "\n")
        final.write(hostname + "\n")
        final.write("+2 dias sin bk\n")
        final.write("---\n")
        final.write("NADA\n")

    # error = True
    # mensaje += "Respaldo realizado correctamente\n" + logOK

f.close()
log.close()
# df_output = [s.split() for s in os.popen("df -h | grep backup").read().splitlines()]
df_output = os.popen("df -h | grep backup").read().split()
if len(df_output[4]) < 4:
    final.write(df_output[4][:2])
else:
    final.write(df_output[4][:3])
final.close()
# print "chao"
# if error:
# print cont_exito
# print cont_error
if sumaRespaldos > 1:
    os.popen("tail -7 final.txt > temp")
    os.popen("cat temp > final.txt")

# vim:set ft=python :
