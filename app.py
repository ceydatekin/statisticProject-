from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
from pandas.core.base import PandasObject
from werkzeug.utils import secure_filename
import numpy as np
import seaborn as sns
import base64
from io import BytesIO
from matplotlib.figure import Figure
import statistics
from numpy import random
app = Flask(__name__)



@app.route("/")
def index():

    return render_template("index.html" )


@app.route('/stdhesapla', methods = ["GET", "POST"])
def stdhesapla():
    if request.method == "POST":
        return render_template("number.html")
    else:
        return redirect(url_for("index"))

@app.route('/stdhesapla1', methods = ["GET", "POST"])
def stdhesapla1():
    if request.method == "POST":
        try:
            number1= request.form.get("number1")
            b = []
            a = number1.split(",")
            for i in a:
                b.append(int(i))
            b = pd.DataFrame(b, columns=["df"])
            total2 = b["df"].std();
            son =  "{:.4}".format(total2)
            return render_template("sonuc1.html", total = b["df"].mean(),total2= son,total3=b["df"].median(),total4 =statistics.multimode(b["df"]))
            
        except :
           return render_template("hata.html")
       
    else:
        return redirect(url_for("index"))


@app.route('/ahhesapla', methods = ["GET", "POST"])
def ahhesapla():
    if request.method == "POST":
        return render_template("number2.html")
    else:
        return redirect(url_for("index"))

@app.route('/ahhesapla1', methods = ["GET", "POST"])
def ahhesapla1():
    if request.method == "POST":
        try :
            number1= request.form.get("number1")
            b = []
            a = number1.split(",")
            for i in a:
                b.append(int(i))
            snc1=harmonik(b)
            son1 =  "{:.4}".format(snc1)
            snc1=geometrik(b)
            son2 =  "{:.4}".format(snc1)
            return render_template("sonuc2.html", total1 = son1,total2=son2)
        except :
           return render_template("hata.html")
    else:
        return redirect(url_for("index"))


def harmonik(self):
    har = 1 / self[0]
    for i in range(1, len(self)):
        har += (1 / self[i])
    har = len(self) / har
    return har

def geometrik(self):
    geo = self[0]
    for i in range(1, len(self)):
        geo *= self[i]
    geo **= (1 / len(self))
    return geo

@app.route('/ghesapla', methods = ["GET", "POST"])
def ghesapla():
    if request.method == "POST":
        return render_template("number3.html")
    else:
        return redirect(url_for("index"))
@app.route('/ghesapla1', methods = ["GET", "POST"])
def ghesapla1():
    if request.method == "POST":
        try:
            number1= request.form.get("number1")
            b = []
            a = number1.split(",")
            for i in a:
                b.append(int(i))
            b = pd.DataFrame(b, columns=["df"])
        
            fig = Figure()
        
            ax = fig.subplots()
            ax.title.set_text("Number Sequence Graph")
            ax.plot(random.normal(loc = b["df"].mean(), scale = b["df"].std() , size = (b["df"].count())))
        
        
            buf = BytesIO()
            fig.savefig(buf, format = "png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return render_template("sonuc3.html", total1 = data)
        except :
           return render_template("hata.html")
    else:
        return redirect(url_for("index"))

@app.route('/yhesapla', methods = ["GET", "POST"])
def yhesapla():
    if request.method == "POST":
        return render_template("number4.html")
    else:
        return redirect(url_for("index"))
@app.route('/yhesapla1', methods = ["GET", "POST"])
def yhesapla1():
    if request.method == "POST":
        try:
            number1= request.form.get("number1")
            b = []
            a = number1.split(",")
            for i in a:
                b.append(int(i))
            b = pd.DataFrame(b, columns=["df"])
            return render_template("sonuc4.html", total1 = b["df"].count() , total2 = b["df"].sum(), total3 = b["df"].max(), total4= b["df"].min())
        except :
           return render_template("hata.html")
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug = True)
    
