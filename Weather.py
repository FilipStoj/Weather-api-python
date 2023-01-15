from flask import Flask, render_template, request
import urllib, urllib.request, json
import re
from key import token

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    townName = 'No city found'
    mycountryName = 'No country found'
    mylocalTime = 'No local time found'
    mylocalTemp = 'No temperature found'
    myweatherDesc = 'No weather description found'

    if request.method == 'POST':
        mycityName= request.form['cityName']
        # real expression : Keep english characters + numbers + change space to "+" and other characters to "+" to avoid errors
        mycityName = re.sub(r'[^a-zA-Z0-9]+', '+', mycityName)

        url ="http://api.weatherapi.com/v1/current.json?key=" + token + "&q=" + mycityName

        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if data['location']['name'] == mycityName.capitalize():
            townName = data['location']['name']
            mycountryName = data['location']['country']
            mylocalTime = data['location']['localtime']
            mylocalTemp = data['current']['temp_c']
            myweatherDesc = data['current']['condition']['text']
    return render_template(
        'index.html',
        cityName = townName,
        countryName = mycountryName,
        localTime = mylocalTime,
        temperature = mylocalTemp,
        weatherDesc = myweatherDesc
        )

if __name__ == '__main__' :
    app.run('localhost', 4449)