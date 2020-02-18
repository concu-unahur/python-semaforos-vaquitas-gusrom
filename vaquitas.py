import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

valor=int(input("Vacas al mismo tiempo: "))
vaquitas=threading.Semaphore(valor)

class Puente(threading.Thread):
  def __init__(self,inicio,largo):
    self.inicioPuente=inicio
    self.largoPuente=largo
    self.finPuente=inicio+largo

  def dibujarPuente():
    print(' ' * inicioPuente + '=' * largoPuente)
  

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):
      self.avanzar()
      try:
        if(self.posicion== inicioPuente):
          vaquitas.acquire()
          self.avanzar()
      finally:
        if (self.posicion== inicioPuente + largoPuente):
          vaquitas.release()
        
        
      

vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
