import os
from flask import Flask, jsonify


application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev') #pobierz mi zmienna srodowiskowa ale jezeli jej nie znajdziesz to pryjmij ze to jest dev





@application.route('/')
def hello_world():
    text = """<!DOCTYPE html>
    
    <html>
        <head>
            <title> Witaj swiecie, czesc AGA :)</title>
  
        </head>
        <body>
            
            <h1>Witaj swiecie! ibig data z pythonem</h1>
           <p>Procesy CI/CD - autmmatyczne wdrażanie, hej AGA :)</p>
        </body>
    
    </html>

    
    """
    if ENV == 'dev':
        text += "<style>body { background-color: red; }</style>"
    return text

@application.route('/json')
def get_json():
    return jsonify({"FLASK_ENV": ENV})



#nie dziala mi to an domyslnym 127.0.0.1:5000 bo projekt nie mam na puplcie tylko w jakims kataalogu, czytalem ze jest an to obesjcie
if __name__ == "main__":
    application.run(debug=True) #na produkcji powinno to byc wylaczone, wiec dobrze miec taki sam ale drugi plik na proda z tym aylczanym


