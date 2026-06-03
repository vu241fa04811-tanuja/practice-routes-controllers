from flask import Flask

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return "hello"

@app.route('/user')
def user_home():
    return "welcome to users platform"

if __name__ == "__main__":
    app.run(debug=True)