from flask import Flask, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get the current day of the week
    day_of_week = datetime.now().strftime('%A')
    
    # Define the HTML content with the day of the week replaced
    html_content = f"""
    <html style="height: 100%">
      <head>
        <meta name="viewport" content="width=device-width, minimum-scale=0.1" />
        <title>Sparkle on! It's {day_of_week}</title>
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
          src="{ url_for('static', filename=day_of_week + '.gif') }"
          width="945"
          height="945"
        />
      </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
