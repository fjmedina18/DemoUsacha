import requests
import conf
import json

sandbox = "https://10.10.20.14"


def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "Application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token

#Get http://apic-ip-address/api/class/topSystem.json

def top_system():
    cabecera = {
        "Content-Type": "application/json"
    }
    galleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox+"/api/class/topSystem.json", headers=cabecera, cookies= galleta, verify=False)
    for i in range(0, 4):
        serial = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["serial"]
        print(serial)
top_system()