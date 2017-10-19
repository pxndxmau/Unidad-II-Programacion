"""Jose Mauricio Hernandez Jimenez GITI9071-E"""

from area import triangle_area
from flask import Flask, render_template, redirect, request

'importamos la variable del area '

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html', the_title='welcome to the form')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    b = float(request.form["b"])
    h = float(request.form["h"])
    result = triangle_area(b, h)
    title = "Triangle area result"
    return render_template('result.html', the_b=b, the_h=h, the_result=result, the_title=title)


'se agregaron las variables b que es base y h que es haltura'

app.run(debug=True)
