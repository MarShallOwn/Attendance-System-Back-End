from mysql import connector
import os

#create our database automatically without the need of manually do it in mysql
def CreateDB():
    try:
        mydb=connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
        )
        cursor =mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ATMS")
    except:
        raise ConnectionError
CreateDB()