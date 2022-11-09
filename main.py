import board
import usb_hid
import digitalio
import time as t
from machine import ADC
from ulab import numpy as np
from adafruit_hid.mouse import Mouse

#print(dir(board)) 
button0 = digitalio.DigitalInOut(board.GP10)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.UP
#Declaramos el pin y funcion de input pull-up al botón 1.
button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
#Declaramos el pin y funcion de input pull-up al botón 2.
button2 = digitalio.DigitalInOut(board.GP25) #Buscar pin
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
#Declaramos el pin y funcion de input pull-up al botón 2.
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
#Declaramos el pin y funcion de output del led incorporado en la placa.
potentiometer = ADC(27)
#Declaramos el pin del potenciometro
POT_MIN = 0
POT_MAX = 65000
#Declaramos las constantes de los valores maximos y minimos que detecta el potenciometro

LEFT_BUTTON = 1
m = Mouse(usb_hid.devices) #Creamos un objeto de mouse, para luego utilizarlo en el main() 

def main():
    pot_reading = potentiometer.read_u16() 
    #Leemos el valor del potenciometro
    t.sleep(0.5) 
    #Damos un tiempo de descanso.
    print(pot_reading)
    #np.interp(pot_reading, (pot_min, pot_max), (lower, higher))
    #mapped_pot = np.interp(pot_reading, (POT_MIN, POT_MAX), (0.5, 10))

    #'Mapeamos' el valor dentro de los segundos a los que se va a volver a realizar el click
    if pot_reading <= 10000:
        mapped_pot = 0.5
    elif pot_reading >= 10000 and pot_reading <= 20000:
        mapped_pot = 1
    elif pot_reading >= 20000 and pot_reading <= 30000:
        mapped_pot = 2
    elif pot_reading >= 30000 and pot_reading <= 40000:
        mapped_pot = 4
    elif pot_reading >= 40000 and pot_reading <= 50000:
        mapped_pot = 6
    else: 
        mapped_pot = 10    

    if not button0.value or not button1.value or not button2.value: #Como devuelve un booleano negativo, pedimos que si NO es Negativo, clickee.
        print('Button pressed!')
        m.click(Mouse.LEFT_BUTTON)
        #Llamamos a la funcion mouse y realizamos el click izquierdo.
        t.sleep(mapped_pot)
        #Damos un tiempo de descanso para que no se realizen muchos clicks al mismo tiempo al realizar solo uno.
        #En este caso, es el valor mapeado del potenciometro.
        led.value = False
    else:
        led.value = True #Si no se presiona, prendemos el led incorporado en la placa.

while True:
    main() #Pedimos que constantemente se ejecute la funcion.