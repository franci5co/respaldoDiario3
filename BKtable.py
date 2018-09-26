#!/usr/bin/python
import os

def html_table(lol,html):
    print >> html,  '  <tr>'
    for sublist in lol:
        #print lol
        #print >> html,  sublist.strip() + lol[5]
        if sublist.strip() == "YES" :
            print >> html,  '    <td>' + '<span class="dot3"></span>' + '</td>'
        elif sublist.strip() == "NO" :
            print >> html,  '    <td>' + '<span class="dot"></span>' + '</td>'
        elif sublist.strip() == "NADA" :
            print >> html,  '    <td>' + '<span class="dot2"></span>' + '</td>'
        elif sublist.strip() == lol[5].strip() :
            #print 'entre'
            #print lol[5]
            if int(sublist.strip()) > 85:
                print >> html,  '    <td><p style="color:red">' + sublist.strip() + '</p></td>'
            else :
                print >> html,  '    <td><p style="color:black">' + sublist.strip() + '</p></td>'
        else:
            print >> html,  '    <td>' + sublist.strip() + '</td>'
    print >> html,  '  </tr>'

    f.close()
    return ""
	
#path = "D:\\BACKUP\\"
path = "/home/ftpbackup/"
#path2 = "C:\\python27\\tab.html"
path2 = "/var/www/html/tab.html"
html = open(path2,"w")

print >> html,'<head>'
print >> html, '  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">'
print >> html, '  <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>'
print >> html, '  <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>'
print >> html, '    <script type="text/javascript">'
print >> html, '      $(document).ready( function () {'
print >> html, '        $(\'#table_id\').DataTable();'
print >> html, '      } );'
print >> html, '    </script>'
print >> html, '</head>'
print >> html, '<style>'
print >> html,  'table {'
print >> html,  '    width:100%;'
print >> html,  '}'
print >> html,  'table, th, td {'
print >> html,  '   border: 1px solid black;'
print >> html,  '    border-collapse: collapse;'
print >> html,  '}'
print >> html,  'th, td {'
print >> html,  '    padding: 15px;'
print >> html,  '    text-align: center;'
print >> html,  '}'
print >> html,  'table tr:nth-child(even) {'
print >> html,  '    background-color: #eee;'
print >> html,  '}'
print >> html,  'table tr:nth-child(odd) {'
print >> html,  '   background-color: #fff;'
print >> html,  '}'
print >> html,  'table th {'
print >> html,  '   background-color: black;'
print >> html,  '    color: white;'
print >> html,  '}'
print >> html,  '.dot3 {'
print >> html,  '  height: 25px;'
print >> html,  '  width: 25px;'
print >> html,  '  background-color: #008000;'
print >> html,  '  border-radius: 50%;'
print >> html,  '  display: inline-block;'
print >> html,  '}'
print >> html,  '.dot {'
print >> html,  '  height: 25px;'
print >> html,  '  width: 25px;'
print >> html,  '  background-color: #FF0000;'
print >> html,  '  border-radius: 50%;'
print >> html,  '  display: inline-block;'
print >> html,  '}'
print >> html,  '.dot2 {'
print >> html,  '  height: 25px;'
print >> html,  '  width: 25px;'
print >> html,  '  background-color: #808080;'
print >> html,  '  border-radius: 50%;'
print >> html,  '  display: inline-block;'
print >> html,  '}'
print >> html,  '</style>'
print >> html,  '<body>'
print >> html,  '<table id="table_id" class="display">'
print >> html,  '  <thead>'
print >> html,  '    <th>Cliente</th>'
print >> html,  '    <th>SID</th>'
print >> html,  '    <th>Hostname</th>'
print >> html,  '    <th>Fecha Bkup</th>'
print >> html,  '    <th>Hora Bkup</th>'
print >> html,  '    <th>Resultado Bkup</th>'
print >> html,  '    <th>% Disco Usado</th>'
print >> html,  '    <th>Ultima Actualizacion</th>'
print >> html,  '  </thead>'  
print >> html,  ' <tbody>'
for filename in os.listdir(path):
    #print filename
    #print path
#def proc_file(archivo):
    if not filename.startswith('.'):
        f = open(path + filename,"r")
#for line in f:
        lol = f.readlines()
        #print lol
        html_table(lol,html)
print >> html,  ' </tbody>'
print >> html,  '</table>'
print >> html,  '</body>'
