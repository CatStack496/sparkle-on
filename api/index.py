from flask import Flask, redirect, render_template_string, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current day of the week
    day_of_week = datetime.datetime.now().strftime('%A').lower()
    # Redirect to the appropriate URL
    return redirect(f'/its-{day_of_week}/')

# Template for each day
template = """
<html style="height: 100%">
  <head>
    <meta name="viewport" content="width=device-width, minimum-scale=0.1" />
    <title>Sparkle on! It's {{ day_of_week }}</title>
  </head>
  <body style="margin: 0px; height: 100%; background-color: rgb(14, 14, 14)">
    <img
      style="
        display: block;
        -webkit-user-select: none;
        margin: auto;
        background-color: hsl(0, 0%, 90%);
        transition: background-color 300ms;
      "
      src="{{ url_for('static', filename=day_of_week + '.gif') }}"
      width="945"
      height="945"
    />
  </body>
</html>
"""

@app.route('/its-monday/')
def monday():
    return render_template_string(template, day_of_week="Monday")

@app.route('/its-tuesday/')
def tuesday():
    return render_template_string(template, day_of_week="Tuesday")

@app.route('/its-wednesday/')
def wednesday():
    return render_template_string(template, day_of_week="Wednesday")

@app.route('/its-thursday/')
def thursday():
    return render_template_string(template, day_of_week="Thursday")

@app.route('/its-friday/')
def friday():
    return render_template_string(template, day_of_week="Friday")

@app.route('/its-saturday/')
def saturday():
    return render_template_string(template, day_of_week="Saturday")

@app.route('/its-sunday/')
def sunday():
    return render_template_string(template, day_of_week="Sunday")

if __name__ == '__main__':
    app.run(debug=True)
