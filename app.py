from flask import Flask
from flask import url_for, render_template, send_file, redirect
import datetime, time as sleep
# import json
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # return send_file(url_for('static', filename='index.html'))
    # return send_file('static/index.html')
    time = datetime.datetime.now()
    # hello = "Добрый Ночь"
    # if 5 < time.hour < 17:
    #     hello = "Добрый день"

    arr = [1, 2, 3, 4]
    # return render_template("header.html")
    return render_template("index.html", title=time, head1='head1', arr=arr, time=time, sleep=sleep.sleep)

@app.route('/prodject')
def prodject():
    return render_template("prodject.html", title='Abaut')

@app.route('/abaut')
def abaut():
    return render_template("abaut.html", title='Abaut')

@app.route('/api')
def api():
    print('COntent-type application/json')
    print('')

    import json, random
    obj = None
    with open('example.json', 'r') as file:
        obj = json.load(file)

    obj['temperature'] = random.randint(15, 30)
    obj['humidity'] = random.randint(10, 100)
    ob = random.randint(0, 1)
    if ob == 1:
        obj['boiler']['isRun'] = True
    else:
        obj['boiler']['isRun'] = False
    obj['meter']['electricity']['consumption'] = random.randint(0, 5)
    obj['meter']['gas']['consumption'] = random.randint(0, 5)
    obj['meter']['water']['consumption'] = random.randint(0, 5)

    print(json.dumps(obj))
    return json.dumps(obj)

if __name__ == '__main__':
    app.run(debug=True)
