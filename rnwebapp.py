from flask import Flask
app = Flask(__name__)

text1 = " this is my first website"
@app.route("/")
def index():
    return text1

if __name__ == "__main__":
    app.run()