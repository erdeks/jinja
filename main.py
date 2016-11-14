from flask import Flask
from flask import render_template
from flask import request
import random
app= Flask (__name__)
#Crear numero para ejercicio adivina
rand = random.randrange(1,100)


@app.route("/")
def main():
	return render_template ('main.html')
@app.route('/calendari')
def calendari ():
	return render_template ('calendari.html')
@app.route('/sudoku')
def jinja1():
	return render_template("sudoku.html")
@app.route('/adivinNum', methods=['GET', 'POST'])
def adivina():
	global rand
	print rand
	mes = "No hay numero"
	if request.method == "POST":
		num = request.form["numer"]
		num = int(num)
		if rand != num:
			if (rand<num):
				mes ='El numero es MENOR al numero introducido'
			else:
				mes = 'El numero es MAYOR que el numero introducido'
		else:
			mes = 'Correcto! Se ha generado otro numero' 
			rand = random.randrange(1, 100)
			print rand
	return render_template("adivinNum.html", mesage=mes)

if __name__=="__main__":
	app.run()