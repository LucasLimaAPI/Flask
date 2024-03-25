from flask import Flask  # Importing flask

app = Flask(__name__)  # Specify the module


@app.route('/start')  # Create a route
def hello():
    return '<h1>Hello world!</h1>'


app.run()  # running the application
