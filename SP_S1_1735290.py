import pymongo
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pymongo import MongoClient
import pprint

#Connect to Mongodb databse
def connection():
    'connect to Mongo db '
    client = MongoClient()
    db = client.database_shopping_minds
    return db


#----------------------------------------------------------------------------------------
def table_product(db_name):
    'create tables in Postgresql'
    con = psycopg2.connect(dbname=db_name, user='postgres',password='amaryllis')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE Products('
                    'product_id int, '
                    'brand varchar(255) ,'
                    'category varchar(255),'
                    'gender varchar(255),'
                    'price  decimal(10,2),'
                    'has_sale  bool,'
                    'PRIMARY KEY(product_id))')
        print('worked')
    except:
        pass
    cur.close()
    con.close()

def table_klant(db_name):
    'create table Klant in Postgres'
    con = psycopg2.connect(dbname=db_name, user='postgres', password='amaryllis')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE Klant('
                        'klant_id int, '
                        'segment varchar(255) ,'
                        'has_mail bool,'
                        'session_start date, '
                        'session_ends date,'
                        'PRIMARY KEY (klant_id))')
    except:
        pass
    cur.close()
    con.close()

def transfer_product(db_name):
    'Transfer from mongo db in to Table product '
    db = connection()
    products = db['products']
    lst_1 = []

    for x in products.find({},{'brand':1,'category':1,'gender':1, 'price.selling_price':1}):
        lst_1.append(x)
        print(x)

    klant = db['sessions']

    for i in klant.find({}, {'has_sale':1}):
        lst_1.append(i)
        print(lst_1)

    con = psycopg2.connect(dbname=db_name, user='postgres', password='amaryllis')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        for atr in lst_1:
            print(atr)
            cur.execute('Insert into Product(object_id, brand, category,gender, price, has_sale) '
                'VALUES (\'{},{},{},{},{},{}\')'.format(atr['_id'],atr['brand'],atr['category'],atr['gender'],atr['price']['selling_price'],atr['has_sale']))
            print('it worked')
    except:
        print('Keep trying')
    cur.close()
    con.close()

def transfer_klant(db_name):
    'Transfer from mongo db in to Table klant '
    db = connection('database_shopping_minds')
    visitors = db  ['visitors']
    lst_2 = []

    for item in visitors.find({},{'recommendations.segment' : 1,'meta.has_mail':1}):
        lst_2.append(item)

    klant = db['sessions']

    for iets in klant.find({}, {'user_agent.session_start':1,'user_agent.session_end':1 }):
        lst_2.append(iets)

    con = psycopg2.connect(dbname=db_name, user='postgres', password='amaryllis')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        for atrib in lst_2:
            cur.execute('Insert into Klant(klant_id, segment, has_mail, session_start, session_ends) '
                'VALUES (\'{},{},{},{},{}\')'.format(atrib['_id'],atrib['reommendations']['segment'],atrib['meta']['has_mail'],atrib['session_start'],atrib['session_end']))
        print('it worked')
    except:
        print('Keep trying')
    cur.close()
    con.close()
#----------------------------------------------------
connection()
sql_db = 'transfer_db'
table_product(sql_db)
table_klant(sql_db)
transfer_product(sql_db)
transfer_klant(sql_db)
