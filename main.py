from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title='Главная')

@app.route('/prodject')
def prodject():
    return render_template("prodject.html", title='Наши проэкты')

@app.route('/abaut')
def abaut():
    return render_template("abaut.html", title='О нас')

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
    app.run(debug=True, port=os.getenv("PORT", default=5000))
