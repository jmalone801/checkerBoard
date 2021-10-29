from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def board1():
    return render_template("index.html", num = 8, num1=8, clr="yellow", clr2="teal")

@app.route('/<int:num>')
def board2(num):
    return render_template("index.html", num=num, num1=8, clr="yellow", clr2="teal")

@app.route('/<int:num>/<int:num1>')
def board3(num, num1):
    return render_template("index.html", num=num, num1=num1, clr="yellow", clr2="teal")

@app.route('/<int:num>/<int:num1>/<color1>/<color2>')
def board4(num, num1, color1, color2):
    return render_template("index.html", num=num, num1=num1, clr=color1, clr2=color2)


if __name__=="__main__":
    app.run(debug=True)
