from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Oh no my Data"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process' , methods=['post'])
def process():
    data = request.form
    print(data)
    session['data'] = data
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('display.html' , data = session['data'])

if __name__ == "__main__":
    app.run(debug = True)