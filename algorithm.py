from database_connections import con_sql

#Populaire producten
def popular_products(dbname, dbuser,dbpw):
    popular_list = []
    conn = con_sql(dbname, dbuser,dbpw)
    cur= conn.cursor()
    pop_query = """
    SELECT orders.product_id FROM sessions
    INNER JOIN orders ON sessions.session_id = orders.session_id
    WHERE sessions.session_start > CURRENT_DATE - INTERVAL '3 months'
    GROUP BY orders.product_id ORDER BY COUNT(*) DESC LIMIT 100
    """
    cur.execute(pop_query)
    for list in cur.fetchall() :
        popular_list.append(list[0])
    cur.close()
    conn.close()
    return popular_list

def similar_products(dbname, dbuser, dbpw,product_id):
    similar_list = []
    conn = con_sql(dbname, dbuser, dbpw)
    cur = conn.cursor()
    sim_query = """
    SELECT category,sub_category,sub_sub_category FROM products WHERE product_id = '{}'
    """.format(product_id)
    cur.execute(sim_query)
    fetched =cur.fetchall()
    for i in fetched :
        category = fetched[0]
        sub_category = fetched[1]
        sub_sub_category = fetched[2]
    sim_productid = """
    SELECT product_id FROM products WHERE category= '{}'
    AND sub_category= '{}'
    AND sub_sub_category='{}'
    LIMIT 10
    """.format(category, sub_category, sub_sub_category)
    cur.execute(sim_productid)
    f_productid= cur.fetchall()
    for i in f_productid:
        similar_list.append(i)
    return similar_list



