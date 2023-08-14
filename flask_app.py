from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/submit', methods=['POST'])
def submit():
    print('Form received')
    print(request.form)
    return app.send_static_file('acknowledgement.html')
