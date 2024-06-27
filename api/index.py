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
    return send_file(image, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)
    
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r