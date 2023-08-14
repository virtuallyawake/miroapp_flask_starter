from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/submit', methods=['POST'])
def submit():
    print('Form received')
    # We get the board url from the form
    board_url = request.form['board-url']
    print(board_url)
    return app.send_static_file('acknowledgement.html')
