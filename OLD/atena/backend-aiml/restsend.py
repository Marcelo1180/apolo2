import requests
import json

url = 'http://localhost:5984/institucion/_find'
data = {
    'selector': {
        'doc_type': 'documentos'
    }
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# requests.post(url, json=json.dumps(data), headers=headers)
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json())

# https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
# estaba viendo eso para meterle tipo array functions para las validaciones

# TODO: tengo que hacer una funcion que ejecute el post y que llame al servicio atena para ejecutar los comandos
