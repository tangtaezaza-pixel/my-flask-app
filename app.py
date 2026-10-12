
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
            <p>เว็บไซต์แรกของฉันบน Vercel</p>
        </body>
    </html>
    """
