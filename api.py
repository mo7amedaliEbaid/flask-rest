from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')

def home():
    return '<h1>Flask Rest Api</h1>'

if __name__=='__main__':
    app.run(debug=True)