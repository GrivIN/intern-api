from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>testing!</h1>"

@app.route("/health")
def health():
    return "<h1>testing testing!</h1>"

if __name__ == "__main__":
    app.run(debug=True)