from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def products():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)