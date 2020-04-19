from flask import Flask, render_template, request ,escape
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/')
def home():
        return render_template("index.html",the_title="Weather App")
@app.route('/weather', methods=['POST'])
def weather():
        selected_city = request.form.get('manu')
        r = requests.get(selected_city,timeout=10)
        c = r.content
        soup = BeautifulSoup(c,"html.parser")
        all_items = soup.find_all("div", {"class":"cont25"})
        time_items = soup.find_all("div",{"class":"24_in"})
        return render_template("weather.html",
                                all_items=all_items,
                                time_items=time_items,
                                selected_city=selected_city.split("/",5)[-1])
        
if __name__ == '__main__':
        app.run(debug=True)
