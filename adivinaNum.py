from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/adivinaNum", methods=["GET","POST"])
def adivinaNum():
	if request.method == "POST":
		trobat = 0
		while trobat == 0:
			rand = random.random()
			if rand == num:
				print 'Correcto! Se ha generado otro numero' 
			else:
				if (rand<num):
					print 'El numero es MENOR al numero introducido'
				else:
					print 'El numero es MAYOR que el numero introducido'
	return render_template( "adivinNum.html", missatge=miss )
 if __name__ == "__main__":
    app.run()
