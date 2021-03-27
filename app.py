from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)


website_list = ["https://www.harvard.edu", "https://www.caltech.edu", "https://www.gatech.edu"]

prime = (2**11) - 1

@app.route("/")
def home():
    curr_date = datetime.today()
    year = curr_date.year
    month = curr_date.month
    day = curr_date.day
    rand = ((year*month*day) % prime) % len(website_list)
    website = website_list[rand]
    return redirect(website)
    

if __name__ == "__main__":
    app.run(debug=False)
