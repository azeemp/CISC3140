from flask import Flask
from flask import render_template
import urllib
import json
import ssl






app = Flask(__name__)

@app.route('/')
@app.route('/home')
ssl._create_default_https_context = ssl._create_unverified_context
urlobj = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=aQeGLw1cGqQ5xY96Jvez21uwOooN07fanc4bAvF9')
apodread = urlobj.read()
data = json.loads(apodread.decode('utf-8'))
def main():
    
    return render_template('home.html', imageurl=data["url"],explanation=data["explanation"],title=data["title"])

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
