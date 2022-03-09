from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/hello')
def hello():
    name = "Hello world! (Version 1.0)"
    return name

if __name__ == "__main__":
    app.run(port=5000)
