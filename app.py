@app.route("/")
def index():
    import pandas as pd
    import os

    file = os.path.join(os.path.dirname(__file__), "data.xlsx")

    try:
        df = pd.read_excel(file)
        df.columns = df.columns.str.strip()

        return "Columns: " + str(df.columns)

    except Exception as e:
        return "ERROR: " + str(e)