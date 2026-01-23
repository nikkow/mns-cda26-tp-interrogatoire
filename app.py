from flask import Flask, render_template, redirect, session
from ollama import chat 
import json
from generators.case import CASE_SYSTEM_PROMPT, CASE_USER_PROMPT, Case
from generators.chat import SUSPECT_SYSTEM_TEMPLATE

app = Flask(__name__)
app.secret_key = 'riz-crousty-power'

@app.route("/", methods=["GET"])
def define_case():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def define_case_post():
    messages = [
        {"role": "system", "content": CASE_SYSTEM_PROMPT},
        {"role": "user", "content": CASE_USER_PROMPT}
    ]

    response = chat(
        model="gemma3:4b",
        messages=messages,
        format=Case.model_json_schema(),
        options={"temperature": 0.7}
    )

    session["case"] = json.loads(response["message"]["content"])

    return redirect("/questioning")

@app.route("/questioning", methods=["GET"])
def questioning():
    if "case" not in session:
        return redirect("/")

    return render_template("chat.html", case=session["case"])

@app.route("/questioning", methods=["POST"])
def questioning_post():
    system_prompt = SUSPECT_SYSTEM_TEMPLATE.format(
        CASE_JSON=json.dumps(session["case"], ensure_ascii=False, indent=2),
        MEMORY_SUMMARY=""
    )

if __name__ == "__main__":
    app.run(debug=True)