from flask import Flask
import requests
import sys
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Deployment Info</h1>
    <p><b>Python versie:</b> {sys.version}</p>
    <p><b>Platform:</b> {platform.system()} {platform.release()}</p>
    <p><b>Flask versie:</b> {__import__('flask').__version__}</p>
    <p><b>Requests versie:</b> {requests.__version__}</p>
    <p>Virtual environment deployment geslaagd!</p>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

