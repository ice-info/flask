from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Shoe, db  # Import your model and database instance
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Home Route
@app.route('/')
def home():
    return "Hello, Flask with database!"

# Shoes Route
@app.route('/shoes')
def show_shoes():
    try:
        shoes = Shoe.query.all()
        return render_template('shoes.html', shoes=shoes)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create Database if not exists
@app.before_first_request
def create_tables():
    db.create_all()
    print("Database created successfully!")

if __name__ == '__main__':
    app.run(debug=True)




