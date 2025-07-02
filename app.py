from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # This is a hardcoded secret - SonarQube should find this!
    db_password = "mySuperSecretPassword123"
    
    # CORRECTED: 'print' is now all lowercase
    print(f"A user connected! The secret password is {db_password}") # Logging secrets is also bad practice
    
    return '<h1>Hello, World! This is our test application.</h1>'

# This allows us to run the app directly using 'python app.py'
if __name__ == '__main__':
    # Running in debug mode is insecure for production
    app.run(debug=True, host='0.0.0.0', port=8080)
