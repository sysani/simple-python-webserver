import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask App</h1>"

if __name__ == "__main__":
    app.run()
