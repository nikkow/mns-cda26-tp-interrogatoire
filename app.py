from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def define_case():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def define_case_post():
    return "Handle POST Request"

@app.route("/questioning", methods=["GET"])
def questioning():
    return render_template("chat.html")

@app.route("/questioning", methods=["POST"])
def questioning_post():
    return "Handle Questioning POST Request"

if __name__ == "__main__":
    app.run(debug=True)