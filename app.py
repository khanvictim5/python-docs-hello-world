from flask import Flask
app = Flask(__name__)

@app.route("/prepaid-cards/card-activation/")
def hello():
    return "Takeover by Memon"
