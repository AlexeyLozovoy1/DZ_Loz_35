from flask import Flask
from  flask import url_for, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # return send_file(url_for('static', filename='index.html'))
    return send_file('static/index.html')

@app.route('/home2')
@app.route('/home')
def home():  # put application's code here
    return 'Home!'

if __name__ == '__main__':
    app.run()
