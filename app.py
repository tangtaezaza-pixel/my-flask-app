
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My First Website</title>
        </head>
        <body>
            <h1>Hello from Flask!</h1>
            <p>เทส123 123 123 123 123 Vercel</p>
        </body>
    </html>
    """
