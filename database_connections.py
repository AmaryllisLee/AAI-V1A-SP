import psycopg2
from pymongo import MongoClient

#Connectie met Mongodb
def con_mongo_db(dbname):
    client = MongoClient()
    db = client[dbname]
    return db

#Connectie met SQL
def con_sql(dbname, dbuser, dbpw):
    conn = psycopg2.connect(dbname=dbname, user=dbuser, pw= dbpw)
    return conn

