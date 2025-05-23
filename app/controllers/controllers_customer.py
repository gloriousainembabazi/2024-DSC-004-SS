from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Customer, Category
from flask import Flask
from flask import jsonify, request


#POST /customers
#POST /customers/{customer_id}/products
bp = Blueprint('customer', __name__)
@bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    db.session.commit()
    return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email}), 201