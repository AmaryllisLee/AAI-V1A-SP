from typing import List, Any
from koppeling_databases import sql_connect, mongodb_connect
import psycopg2

#Connection with Mongodb database
mongo_db,collection  = 'database_shopping_minds','product'

#-------------------------------------------------------------------------------------
def getPopularProducts(db_name, us,pw,table, g):
     'Haal bepaalde fields '
     con = 'recommendable == true' #vb conditionals
     limit=3
     id_pp = sql(db_name, us,pw,g, table, con, limit)
     return lst_mongo(id_pp,mongo_db,collection)

def getSimilarproducts(db_name, us,pw,table, g):
    'Haal bepaalde fields'
    con = 'price=179'
    limit = 3
    id_sp = sql(db_name, us,pw,g, table, con, limit)
    return lst_mongo(id_sp, mongo_db, collection)


def getPersonalProducts(session):
    print("Recommendations for session: {}".format(session['_id']))

    return [
        {"_id": "23978", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-men-men-beast-deospray-150ml"},
        {"_id": "22309", "brand": "Agfa", "category": "Elektronica & media", "deeplink": "https://www.opisopvoordeelshop.nl/afgaphoto-alkaline-power-batterijen-aa-4-stuks"}
    ]


#----------------------------------------------------------------------
# Function for lijst van de product uit SQL
def sql(db_name, us,pw, g, table, condition, limit):
    'Lijst van ids weergeven met bepaalde conditionals'
    con = sql_connect(db_name,us,pw)   #Connect with the SQL db
    query = 'Select {} from {} where {} limit {}'.format(g,table, condition,limit)#Query that get 3 of the product id\'s that is tue with the condition'
    cur = con.cursor()
    cur.execute(query)
    cur.close()
    con.commit()
    return


def lst_mongo(s, mongo_db, collection):
    'Field in mongo van de ids in lst_sql in een lijst zetten'
    collection= mongodb_connect(mongo_db, collection) # connect to mongodb db
    mongo_lst = []
    for i in s:
        for x in collection({},{'{}':1,'category':1, 'price.selling_price':1, 'deeplink':1}).format(i):
            mongo_lst.append(x)
        return mongo_lst

print(getPopularProducts())