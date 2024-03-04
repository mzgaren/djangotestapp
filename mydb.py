import mysql.connector

database = mysql.connector.connect(host='localhost', user='sqldba', passwd='HP1nv3nt@2209')

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE dcrm")

print("ALL GOOD ! ")
