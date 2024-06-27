from flask import Flask, send_file
from datetime import datetime

app = Flask(__name__)

def sparkleGif():
    return "./static/" + datetime.now().strftime('%A') + ".gif"

@app.route('/')
def sparkleOn():
    image = sparkleGif()
    return send_file(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)