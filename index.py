# Utilizamos una biblioteca (framwork) que nos permitira crear una aplicación Web
# Con flask podemos llamar a una biblioteca y empezar a escribir el código

from flask import Flask, render_template  # Llamamos a las bibiliotecas flask y render_template
App = Flask(__name__) # Flask es el archivo principal al cual le pasamos una variable llamada name
                # y el objeto que me devuelve Flask lo guardo en una variable llamada App
                # Esta variable la utilizamos para guardar la ruta del sevidor, nuestras URLs, etc

@App.route('/')  # Para crear una ruta utilizamos el decorador @ y un método route() que le podemos 
              # pasar un nombre para crear una URL. Slap (/) índica que es nuestra pàgina principal
def Inicio():  # Creamos la función inicio para que haga algo cuando un usuario entre en la pàgina principal
    # return "Pàgina Inicio # En este caso la función devuelve la cadena "Página Inicio" al navegador
    return render_template('home.html') # En este caso la plantilla home.html de nuestra carpeta templates
                        # Necesitamos que nuestra aplicación se quede escuchando nuevas peticiones

@App.route('/About') # Creamos otra ruta llamada About
def About():  # Creamos la función About para que alga algo cuando se acceda a esta ruta
    # return "About Page" # La función About retorna el texto "About Page" en el navegador
    return render_template('About.html') # En este caso la plantilla About.html de nuestra carpeta templates

if __name__ == '__main__': # Hacemos una validación para comprobar si estamos en el archivo principal
    App.run(debug= True)  #  El método run nos permite ejecutar nuestra aplicación en modo de prueba