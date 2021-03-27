from flask import Flask, redirect
from datetime import timedelta, datetime
import random

app = Flask(__name__)


website_list = ["https://www.harvard.edu", "https://www.caltech.edu", "https://www.gatech.edu"]


@app.route("/")
def home():
    
    return redirect(website)


if __name__ == "__main__":
    app.run(debug=False)
