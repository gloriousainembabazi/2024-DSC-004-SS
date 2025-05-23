# section b:
# qn: 2(b)
from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Product, Category
from flask import Flask
from flask import jsonify, request
from app.extensions import db

#POST /products
#POST /products/{product_id}/categories

bp = Blueprint('product', __name__)
@bp.route('/products', methods=['POST'])
def create_product():# create new product
    data = request.get_json()# get json data from request
    name = data.get('name')# get name from json data
    price = data.get('price') # get price from json data
    if not name or not price:# check if name and price are provided
        return jsonify({'error': 'Name and price are required'}), 400
    product = Product(name=name, price=price)
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 201



#qn 2(d):

# PUT /products/{product_id}
@bp.route('/products/<int:product_id>', methods=['PUT'])
def Edit_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    name = data.get('name')
    id =data.ger("id")
    price = data.get('price')
    if name:
        product.name = name
    if price:
        product.price = price
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 200

# qn 2(e):
# GET /products/{product_id}
@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 200

# qn 2(f):
# DELETE /products/{product_id}
@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200
