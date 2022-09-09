###this is a flask app which queries data from covid api
#https://api.covid19api.com/summary

from flask import Flask,render_template,request
import urllib.request
import json
import requests
import datetime
from pytz import timezone
import os

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def homepage():
    if request.method=="POST":
        country=request.form["country"]
        print(country)
        url= "https://api.covid19api.com/summary"
        print(url)
        api_data_from_url = requests.get(url).json()
        print(api_data_from_url)
        countries_data=api_data_from_url["Countries"]
        print(countries_data)
        data={}
        for i in countries_data:
            if i["Country"]==country:
                data["Country"] = i["Country"]
                data["TotalConfirmed"]=i["TotalConfirmed"]
                data["TotalDeaths"]=i["TotalDeaths"]
                data["status"]=200
                break
        else:
            data["status"]=404
            data["message"]="Country not found"
        print(data)
        return render_template("covidapp_homepage.html",mydata=data)
    else:
        data=None
        return render_template("covidapp_homepage.html",mydata=data)
#we are sending data to html file using the parameter mydata
#we need to access this mydata in html file and print it
port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(port=port)

