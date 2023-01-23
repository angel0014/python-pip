import requests 


def get_categories():       
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # direccion solicitud
    print(r.status_code) # estado 200-> OK
    print(r.text)
    print(type(r.text)) # class str
    categories = r.json() # tranformar en formato json (dict)
    for category in categories:
        print(category['name'])

