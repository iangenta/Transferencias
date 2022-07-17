import json
with open ("eventos_classic.json", "r") as c:
  datos = json.load(c)
with open ("eventos_gold.json", "r") as jg:
  dataGold = json.load(jg) 
with open ("eventos_black.json", "r") as jb:
  dataBlack = json.load(jb)
  
  
for x in range (0,9):
  tipo = (datos['transacciones'][x]['tipo'])
  e = (datos['transacciones'][x]['estado'])  == "RECHAZADA"
  rca =  tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO'
  te = tipo == 'TRANSFERENCIA_ENVIADA'
  tr = tipo == 'TRANSFERENCIA_RECIBIDA'
  atj = tipo == 'ALTA_TARJETA_CREDITO'
  ac = tipo == 'ALTA_CHEQUERA'
  cd = tipo == 'COMPRA_DOLAR'


def superf():
  if e & rca :
    def RETIRO_EFECTIVO_CAJERO_AUTOMATICO():
      print(f"Usted no puede retirar el dinero debido a que usted pertenece a ['tipo']") 

  elif e & te :
    def TRANSFERENCIA_ENVIADA():
      print(f"Usted no puede enviar el monto debido a que usted pertenece a ['tipo']") 

  elif e & tr :
    def TRANSFERENCIA_RECIBIDA():
      print(f"Usted no puede recibir el monto debido a que no se que poner")
    

  elif e & atj :
    def ALTA_TARJETA_CREDITO():
      print(f"Usted no puede dar el alta a esta tarjeta de credito debido a su categoria ['tipo']")
    

  elif e & ac :
    def ALTA_CHEQUERA():
      print(f"Usted no puede dar alta de la chequera debido a su categoria")
    

  elif e & cd:
    def COMPRA_DOLAR():
      print("algo")




    
  