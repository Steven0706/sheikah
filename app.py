from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! https://console.cloud.google.com/compute/instancesAdd?project=sheikah-tower'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
