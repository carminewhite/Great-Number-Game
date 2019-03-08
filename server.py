from random import randint
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'super secret'
@app.route('/')

def hello_world():
    if 'guess_this' in session:
        pass
    else:
        session['guess_this'] = randint(1,101)
    
    if 'guessed_number' in session:
        pass
    else:
        session['guessed_number'] = "temp"
    print (f"My guessed number is {session['guessed_number']} and my 'guess this' number is {session['guess_this']}")
    return render_template('index.html')


@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    session['guessed_number'] = request.form['guess']
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/right_guess')
def right_guess():
    pass

if __name__=="__main__":
    app.run(debug=True)