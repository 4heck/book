from app import app
from models import Ad
from models import Customer
from models import Town
from models import Book
from flask import jsonify
from flask import request
from app import db
import json

#api's for ad
@app.route('/api/ad', methods=['GET'])
def api_ad_get():
    ads = Ad.query.all()
    ads_json = [{"id": ad.id, "customer": ad.customer, "book": ad.book, "price": ad.price, "locality": ad.locality}
                  for ad in ads]
    return jsonify(ads_json)

@app.route('/api/ad/<id>', methods=['GET'])
def api_ad_get_id(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    ad_json = {"id": ad.id, "customer": ad.customer, "book": ad.book, "price": ad.price, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/ad', methods=['POST'])
def api_ad_insert():
    new_ad = request.get_json()
    ad = Ad(id=new_ad['id'], customer=new_ad['customer'], book=new_ad['book'], price=new_ad['price'], locality=new_ad['locality'])
    db.session.add(ad)
    db.session.commit()
    ad_json = {"id": ad.id, "customer": ad.customer, "book": ad.book, "price": ad.price, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/ad/<id>', methods=['DELETE'])
def api_ad_delete(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    db.session.delete(ad)
    db.session.commit()
    return jsonify()

@app.route('/api/ad/<id>', methods=['PUT'])
def api_ad_update(id):
    updated_ad = request.get_json()
    ads_to_update = Ad.query.filter_by(id=id)
    data = json.loads(request.get_data())
    ad_to_update = ads_to_update[0]
    ad_to_update = db.session.query(Ad).filter_by(id = id).first()
    ad_to_update.customer = data['customer']
    ad_to_update.book = data['book']
    ad_to_update.price = data['price']
    ad_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(ad_to_update.to_dict())

#api's for customer
@app.route('/api/customer', methods=['GET'])
def api_customer_get():
    customers = Customer.query.all()
    customers_json = [{"id": customer.id, "name": customer.name}
                  for customer in customers]
    return jsonify(customers_json)

@app.route('/api/customer/<id>', methods=['GET'])
def api_customer_get_id(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer', methods=['POST'])
def api_customer_insert():
    new_customer = request.get_json()
    customer = Customer(id=new_customer['id'], name=new_customer['name'])
    db.session.add(customer)
    db.session.commit()
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer/<id>', methods=['DELETE'])
def api_customer_delete(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    db.session.delete(customer)
    db.session.commit()
    return jsonify()

@app.route('/api/customer/<id>', methods=['PUT'])
def api_customer_update(id):
    updated_customer = request.get_json()
    customers_to_update = Customer.query.filter_by(id=id)
    data = json.loads(request.get_data())
    customer_to_update = customers_to_update[0]
    customer_to_update = db.session.query(Customer).filter_by(id = id).first()
    customer_to_update.name = data['name']
    db.session.commit()
    return jsonify(customer_to_update.to_dict())

#api's for book
@app.route('/api/book', methods=['GET'])
def api_book_get():
    books = Book.query.all()
    books_json = [{"id": book.id, "name": book.name}
                  for book in books]
    return jsonify(books_json)

@app.route('/api/book/<id>', methods=['GET'])
def api_book_get_id(id):
    books = Book.query.filter_by(id=id)
    if not books:
        abort(404)
    book = books[0]
    book_json = {"id": book.id, "name": book.name}
    return jsonify(book_json)

@app.route('/api/book', methods=['POST'])
def api_book_insert():
    new_book = request.get_json()
    book = Book(id=new_book['id'], name=new_book['name'])
    db.session.add(book)
    db.session.commit()
    book_json = {"id": book.id, "name": book.name}
    return jsonify(book_json)

@app.route('/api/book/<id>', methods=['DELETE'])
def api_book_delete(id):
    books = Book.query.filter_by(id=id)
    if not books:
        abort(404)
    book = books[0]
    db.session.delete(book)
    db.session.commit()
    return jsonify()

@app.route('/api/book/<id>', methods=['PUT'])
def api_book_update(id):
    updated_book = request.get_json()
    books_to_update = Book.query.filter_by(id=id)
    data = json.loads(request.get_data())
    book_to_update = books_to_update[0]
    book_to_update = db.session.query(Book).filter_by(id = id).first()
    book_to_update.name = data['name']
    db.session.commit()
    return jsonify(book_to_update.to_dict())

#api's for town
@app.route('/api/town', methods=['GET'])
def api_town_get():
    towns = Town.query.all()
    towns_json = [{"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
                  for town in towns]
    return jsonify(towns_json)

@app.route('/api/town/<id>', methods=['GET'])
def api_town_get_id(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town', methods=['POST'])
def api_town_insert():
    new_town = request.get_json()
    town = Town(id=new_town['id'], region=new_town['region'], area=new_town['area'], locality=new_town['locality'])
    db.session.add(town)
    db.session.commit()
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town/<id>', methods=['DELETE'])
def api_town_delete(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    db.session.delete(town)
    db.session.commit()
    return jsonify()

@app.route('/api/town/<id>', methods=['PUT'])
def api_town_update(id):
    updated_town = request.get_json()
    towns_to_update = Town.query.filter_by(id=id)
    data = json.loads(request.get_data())
    town_to_update = towns_to_update[0]
    town_to_update = db.session.query(Town).filter_by(id = id).first()
    town_to_update.region = data['region']
    town_to_update.area = data['area']
    town_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(town_to_update.to_dict())