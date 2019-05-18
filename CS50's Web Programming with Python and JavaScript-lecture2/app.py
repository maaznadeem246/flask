from flask import Flask,render_template ,request, session
from flask_session import Session

import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/',methods=["GET","POST"])
def index():
    if session.get("notes") is None:
        session['notes'] = []
    if request.method == "POST":
        note = request.form.get("notes")
        session['notes'].append(note)

    return render_template('formn.html',notes=session['notes'])

@app.route('/formsub')
def formsub():
    return render_template('fromsubmit.html')    

@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method == "GET":
        return "Please Submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)

@app.route('/checkInex')
def checkInex():
    return render_template("index.html")


@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/condition')
def condition():
    headLine= "hello World to All !"
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    return render_template('condition.html',new_year = new_year)
   
@app.route('/loop')
def loop(): 
    names = ['Alice','Bob','Charlie','Maaz','M']
    return render_template("loop.html",names=names)



if __name__ == '__main__':
    #$env:FLASK_ENV = "development"
    app.run(debug=True)

