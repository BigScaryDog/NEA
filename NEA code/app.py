
from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')

def home():

    return render_template('Log_in.html')





# Run the app and initialize the database if it doesn't exist
if __name__ == '__main__':

    with app.app_context():


# Start the Flask app

        app.run(debug=True)