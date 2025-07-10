from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

# Create a Flask web application instance
app = Flask(__name__)

# --- FIX ---
# A SECRET_KEY is needed to generate secure CSRF tokens.
# In a real app, this should not be hardcoded.
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize CSRF protection on the app
csrf = CSRFProtect(app)
# -----------

@app.route('/ping')
def ping():
    return 'pong'

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # This is a hardcoded secret - SonarQube should find this!
    db_password = "mySuperSecretPassword123"
    
    print(f"A user connected! The secret password is {db_password}")
    
    return '<h1>Hello, World! This is our test application.</h1>'

# This allows us to run the app directly using 'python app.py'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)