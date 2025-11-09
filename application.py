#n9ie bedzie dzial na tym

from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    text = """<!DOCTYPE html>
    
    <html>
        <head>
            <title> Witaj swiecie, czesc AGA :)</title>
        </head>
        <body>
            
            <h1>Witaj swiecie! ibig data z pythonem</h1>
           <p>Procesy CI/CD - autmmatyczne wdrażanie</p>
        </body>
    
    </html>

    
    """
    return text

if __name__ == "main__":
    application.run(debug=True) #na produkcji powinno to byc wylaczone, wiec dobrze miec taki sam ale drugi plik na proda z tym aylczanym


