from flask import Flask
from flask import render_template
app= Flask (__name__)
@app.route("/")
def main():
	return render_template ('main.html')
@app.route('/calendari')
def calendari ():
	return render_template ('calendari.html')
@app.route('/sudoku')
def jinja1():
	return render_template("sudoku.html")

if __name__=="__main__":
	app.run()