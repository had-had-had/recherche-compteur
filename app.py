from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

file = "data.xlsx"

@app.route("/", methods=["GET", "POST"])
def index():
    df = pd.read_excel(file)

    search = request.form.get("numctr")

    if search:
        df = df[df["NUM_CTR"].astype(str).str.contains(search)]

    data = df.to_dict(orient="records")

    return "klemek s7i7"

@app.route("/update", methods=["POST"])
def update():
    num = request.form.get("num")
    new_index = request.form.get("index")

    df = pd.read_excel(file)

    df.loc[df["NUM_CTR"].astype(str) == num, "INDEX_DEPS"] = new_index

    df.to_excel(file, index=False)

    return redirect("/")
app.run(debug=True)