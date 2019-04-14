from algorithm import popular_products, similar_products
from producteig_mongo_db import get_product_details

def homepage(conn, mongo_db):
    id_list = popular_products(conn)
    return get_product_details(mongo_db,id_list,True,6)

def productpage(conn, mongo_db):
    id_list = similar_products(conn)
    return get_product_details(mongo_db,id_list,True,6)
