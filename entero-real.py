# librerias
from flask import Flask, render_template, request
from enum import Enum


# Instancia de Flask.Aplicación
app = Flask(__name__)

# clase de estados de la maquina


class Estado(Enum):
    INICIO = 0
    Q1 = 1
    Q2 = 2
    Q3 = 3
    ENTERO = 4
    REAL = 5
    NO_RECONOCIDO = 6


@app.route('/')
def template():
    return render_template("index.html")


@app.route('/entero1', methods=['POST'])
def entero():

    entero = request.form['entero']

    ultimo = Global.reconocerNumeroEnteros(entero)

    if ultimo == Estado.ENTERO:
        return "<h1>El numero es entero</h1>"
        #print("La cadena ingresada es un numero entero", end = '')
        #print("\n", end = '')
    else:
        for indice in range(len(entero)):
            caracter = entero[indice]
            if not caracter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']:

                # print(f'En el índice" {indice}, "tenemos el caracter" {caracter} "que no es un caracter de tipo número')
                return "<h3>La cadena ingresada no es un numero entero</h3><h3>En el índice: " + str(indice) + " tenemos el caracter: " + str(caracter) + " que no es un caracter de tipo número</h3>"
        #print("La cadena ingresada no es un numero entero ni real", end = '' )
        #print("\n", end = '')

    print("\n", end='')
    return 0


class Global:

    def reconocerNumeroEnteros(entero):
        pos = 0
        actual = Estado.INICIO
        cadenaRechazada = False

        while not cadenaRechazada and pos < len(entero):
            simbolo = entero[pos]

            if actual == Estado.INICIO:
                if simbolo.isdigit():
                    # Si es un digito, va al estado ENTERO lo que indica que alcanzo el estado de aceptacion
                    actual = Estado.ENTERO

                elif simbolo == '+' or simbolo == '-':
                    actual = Estado.Q1                          # Si es un signo, va al estado Q1

                else:
                    # Rechazada la cadena si no es un num o simbolo + o -
                    cadenaRechazada = True

            elif actual == Estado.Q1:

                if simbolo.isdigit():                          # Si empiza con simbiolo y el siguiente es un digito, va al estado ENTERO lo que indica que alcanzo el estado de aceptacion
                    actual = Estado.ENTERO

                else:
                    # Si la cadena continua con un caractar no numerico rechazada la cadena
                    cadenaRechazada = True

            elif actual == Estado.ENTERO:
                if simbolo.isdigit():
                    actual = Estado.ENTERO
                else:
                    cadenaRechazada = True
                    for indice in range(len(entero)):
                        caracter = entero[indice]
                        if not caracter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']:
                            return "En el índice {} tenemos a '{}'".format(indice, caracter)
                        "El caracter " + caracter + "en el indice" + \
                            str(indice) + "no es un numero entero"
                        print("En el índice {} tenemos a '{}'".format(
                            indice, caracter))

            # Incrementa la posicion del caracter a analizar
            pos += 1

        if cadenaRechazada:
            # Si la cadena no empiza con un digito o simbolo + o - rechazada la cadena
            return Estado.NO_RECONOCIDO
        return actual

# Codigo para validar numeros reales


@app.route('/real1', methods=['POST'])
def real():

    real = request.form['real']

    ultimo = Globals.reconocerNumero(real)

    if ultimo == Estado.REAL:
        return "<h1>El numero es real</h1>"
    else:
        return "<h1>La cadena ingresada no es un numero real<h1>"

    #  print("\n", end = '')
    #  return 0;


class Globals:

    @staticmethod
    def reconocerNumero(real):
        pos = 0
        actual = Estado.INICIO
        cadenaRechazada = False
        while not cadenaRechazada and pos < len(real):
            simbolo = real[pos]
            if actual == Estado.INICIO:
                if simbolo.isdigit():
                    actual = Estado.Q2
                elif simbolo == '+' or simbolo == '-':
                    actual = Estado.Q1
                else:
                    cadenaRechazada = True
            elif actual == Estado.Q1:
                if simbolo.isdigit():
                    actual = Estado.Q2
                elif simbolo == '.':
                    actual = Estado.Q3
                else:
                    cadenaRechazada = True
            elif actual == Estado.Q2:
                if simbolo.isdigit():
                    actual = Estado.Q2
                elif simbolo == '.':
                    actual = Estado.Q3
                else:
                    cadenaRechazada = True
            elif actual == Estado.Q3:
                if simbolo.isdigit():
                    actual = Estado.REAL
                else:
                    cadenaRechazada = True
            elif actual == Estado.REAL:
                if simbolo.isdigit():
                    actual = Estado.REAL
                else:
                    cadenaRechazada = True
            pos += 1
        if cadenaRechazada:
            return Estado.NO_RECONOCIDO
        return actual


if __name__ == '__main__':
    app.run(debug=True)
