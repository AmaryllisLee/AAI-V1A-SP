from flask import Flask, send_from_directory, jsonify, redirect
from products import getPopularProducts
from database_connections import con_mongo_db,con_sql
from list_product_ids import homepage,productpage

app = Flask(__name__)


@app.route('/')
def home():
    return redirect("/index.html", code=302)


@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)


@app.route('/popularproducts')
def popularproducts():
    return jsonify(homepage(conn,mongo_db))

@app.route('/similarproducts')
def popularproducts():
    return jsonify(productpage(conn,mongo_db))



if __name__ == '__main__':
    mongo_db = con_mongo_db('voordeelshop')
    conn = con_sql('voordeelshop','postgres','amaryllis')
    app.run()#start applicatie
