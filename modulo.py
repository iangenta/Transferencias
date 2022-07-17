import json
from main import data
with open (data, "r") as susc:
  susc = json.load(susc)
for x in range(0,9):
  x = x

def RETIRO_EFECTIVO_CAJERO_AUTOMATICO():

 resultado = susc["transacciones"][x]["saldoEnCuenta"]-susc["transacciones"][x]["monto"]
 print (resultado) 
def ALTA_TARJETA_CREDITO():
  resultado = susc["transacciones"][x]["totalTarjetasDeCreditoActualmente"] +1
  if (susc["tipo"] == "CLASSIC" ):
    print("Classic no tiene acceso a tarjeta")
  elif susc["tipo"] == "GOLD" and resultado > 1:
    print("Gold solo puede tener una tarjeta")
  elif susc["tipo"] == "GOLD" and resultado == 1:
    print(resultado)
  elif susc["tipo"] == "BLACK" and resultado > 5:
    print("Black no puede tener mas de 5 tarjetas")
  elif susc["tipo"] == "BLACK" and resultado <= 5:
    print(resultado)  
def ALTA_CHEQUERA():
  resultado = susc["transacciones"][x]["totalChequerasActualmente"] +1
  if (susc["tipo"] == "CLASSIC" ):
    print("Classic no tiene acceso a Chequera")
  elif susc["tipo"] == "GOLD" and resultado > 1:
    print("Gold solo puede tener una Chequera")
  elif susc["tipo"] == "GOLD" and resultado == 1:
    print(resultado)
  elif susc["tipo"] == "BLACK" and resultado > 2:
    print("Black no puede tener mas de 2 Chequeras")
  elif susc["tipo"] == "BLACK" and resultado <= 2:
    print(resultado)
def COMPRA_DOLAR():
  resultado = susc["transacciones"][x]["cupoDiarioRestante"] -susc["transacciones"][x]["monto"]
  saldoRestante = susc["transacciones"][x]["saldoEnCuenta"] -susc["transacciones"][x]["monto"]
  if (susc["tipo"] == "CLASSIC" ):
    print("Classic no puede comprar dolares")
  elif susc["tipo"] == "GOLD" or susc["tipo"] == "BLACK":
    if resultado < 0:
      print("error, supera el cupo diario")
    elif saldoRestante < -10000:
      print("Supera tu saldo restante")
    elif resultado > 0 and saldoRestante >-10000:
      print("Compra realizada con exito")
def TRANSFERENCIA_ENVIADA():
 if (susc["tipo"] == "CLASSIC" ):
   comision = 0.01
 elif (susc["tipo"] == "GOLD" ):
   comision = 0.005
 elif (susc["tipo"] == "BLACK" ):
   comision = 0
 print(susc["transacciones"][x]["monto"]*comision)       
def TRANSFERENCIA_RECIBIDA():
 if (susc["tipo"] == "CLASSIC" ):
   limite = 150000
 elif (susc["tipo"] == "GOLD" ):
   limite = 500000
 elif (susc["tipo"] == "BLACK"):
  limite = 0   
 resultado = limite - susc["transacciones"][x]["monto"]
 if (resultado < 0):
  print("supera el limite")
 elif (resultado >= 0):
  print("Transferencia recibida")
  print("su limite actual es: ",resultado)

