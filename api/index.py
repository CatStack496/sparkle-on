from flask import Flask, send_file
from datetime import datetime
import pytz

app = Flask(__name__)

def sparkleGif():
    eastern = pytz.timezone('US/Eastern')
    utc_now = datetime.now(pytz.utc)
    est_now = utc_now.astimezone(eastern)
    current_day_est = est_now.strftime("%A")
    return "./static/" + current_day_est + ".gif"

@app.route('/')
def sparkleOn():
    image = sparkleGif()
    return send_file(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)