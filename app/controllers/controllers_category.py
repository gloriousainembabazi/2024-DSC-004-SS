# section: B
#QN: 2(a)

# create the fllowiing API endpoints
# install the required packages
from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Category, Product
from flask import Flask

#POST /categories
#POST /categories/{category_id}/products

bp = Blueprint('category', __name__)# create a blueprint for category
@bp.route('/categories', methods=['POST'])# create a new category
def create_category():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400# check if name is provided
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'id': category.id, 'name': category.name}), 201
