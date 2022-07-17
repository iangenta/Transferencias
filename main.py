import json
from jinja2 import Environment, FileSystemLoader

from funciones import superf

userSelect = int(input("Por favor, ingrese su Dni: "))
userNumber = int(input("Por favor, ingrese su numero de cuenta: "))

if (userSelect == 29494777) & (userNumber == 100003):
  data = str("eventos_classic.json")
  nombre ="classic"
elif (userSelect == 29494777) & (userNumber == 100002):
  data = str('eventos_gold.json')
  nombre ="gold"
elif (userSelect == 29494777) & (userNumber == 100001):
  data = str('eventos_black.json')
  nombre ="black"
  
with open(data, "r") as eb:
  transacciones = json.load(eb)
    
fileLoader = FileSystemLoader("templates")

env = Environment(loader = fileLoader)
    
rendered = env.get_template("templateClassic.html").render(transacciones = transacciones,title="mis transacciones")

fileName3 =f"{nombre}.html"
with open (f"./site/{fileName3}","w") as ebfile:
 ebfile.write(rendered)
 
