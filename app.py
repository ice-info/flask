from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import shoe, db

app = Flask(__name__)

# Configure your database URI here (using SQLite for example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple model example
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Basic route
@app.route('/')
def home():
    return "Hello, Flask with database!"
@app.route('/shoes')
def show_shoes():
    shoes = Shoe.query.all()
    return render_template('shoes.html', shoes=shoes)

if __name__ == '__main__':
    app.run(debug=True)


# If you want both:
print("Hello from local version!")
print("Hello from GitHub version!")



