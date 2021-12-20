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

#this functions check if we make migration first 
#check if authentication_user table is created
def checkUserTableExists():
    mydb=connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database = os.environ.get('DB_NAME')
        )
    cursor =mydb.cursor()
    cursor.execute("""
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = "authentication_user"
    """)
    if cursor.fetchone() != None:
        return True
    return False
    
#this function create default admin user with this account
#email =admin@gmail.com , password =adminn
def CreateDefaultAdminUser():
    query = (
            "INSERT IGNORE INTO authentication_user("
            "id,"
            "password,"
            "is_superuser,"
            "created_at,"
            "updated_at,"
            "nationalID,"
            "username,"
            "firstname,"
            "lastname,"
            "email,"
            "is_staff,"
            "is_active,"
            "phoneNumber)"
            "VALUES"
            "("
            "'1977139bb3ed4b5cbba4137646c68351',"
            "'pbkdf2_sha256$320000$O5B2mPKJeVHTXoQtpLjyCA$dhurPOrerTChIsSq6fy4npGu2JNoebL7cH2uYQuGbR8=',"
            "'1',"
            "now(),"
            "now(),"
            "'11111111111111',"
            "'admin',"
            "'admin',"
            "'admin',"
            "'admin@gmail.com',"
            "'1',"
            "'1',"
            "'01111111111')"
        )   
    mydb=connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database = os.environ.get('DB_NAME')
        )
    cursor =mydb.cursor()
    cursor.execute(query)
    mydb.commit()

CreateDB()
if checkUserTableExists():
    CreateDefaultAdminUser()