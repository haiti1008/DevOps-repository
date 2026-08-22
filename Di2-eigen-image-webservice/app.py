from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Di2 Docker webservice!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False, processes=1)

