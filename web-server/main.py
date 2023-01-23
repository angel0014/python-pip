import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #instancia


@app.get('/') # decorador--> ruta desde la web se va ingresar
def get_list():
    return [10,11,12,13,14]


@app.get('/contact', response_class=HTMLResponse) # decorador--> ruta desde la web se va ingresar
def get_contact():
    return '''<h1>Littles Turtles</h1>
              <p>Primeros pasos de una Tortuga, iniciando en el mundo de la programacion?...</p>
              '''

def run():
    store.get_categories()

if __name__ == '__main__': # ejecutar como script
    run()