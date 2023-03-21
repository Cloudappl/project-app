from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    else:
        return render_template("hello.html")


if __name__ == "__main__":
    app.run(host="localstack", port=5000, debug=True)
