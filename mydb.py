import mysql.connector

database = mysql.connector.connect(
    host = 'localhost'
    user = 'root'
    passwd = 'HP1nv3nt'

)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE dcrm")

print("ALL GOOD ! ")
