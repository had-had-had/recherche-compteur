from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

file = os.path.join(os.path.dirname(__file__), "data.xlsx")

@app.route("/")
def index():
    return str(os.listdir())

@app.route("/update", methods=["POST"])
def update():
    num = request.form.get("num")
    new_index = request.form.get("index")

    df = pd.read_excel(file)
    df.loc[df["NUM_CTR"].astype(str) == num, "INDEX_DEPS"] = new_index
    df.to_excel(file, index=False)

    return redirect("/")