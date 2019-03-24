from pymongo import MongoClient
import psycopg2


#Koppeling maken met SQL database
def sql_connect(sql_db, us,pw):
    'Connect to SQl db'
    connection = psycopg2.connect(dbname=sql_db, user='postgres', password='amaryllis')
    return connection


#Koppeling maken met MOngodb database
def mongodb_connect(mongo_db, collection):
    'Connect to Mongodb db'
    mongoclient = MongoClient()
    mongodb = mongoclient['{}'].format(mongo_db)
    collection_connected = mongodb['{}'].format(collection)
    return collection_connected

