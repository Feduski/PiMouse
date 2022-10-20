import board
import usb_hid
import digitalio
import time as t
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
LEFT_BUTTON = 1
m = Mouse(usb_hid.devices) #Creamos un objeto de mouse, para luego utilizarlo en el main() 

def main():
    if not button0.value or not button1.value or not button2.value: #Como devuelve un booleano negativo, pedimos que si NO es Negativo, clickee.
        print('Button pressed!')
        m.click(Mouse.LEFT_BUTTON)#Llamamos a la funcion mouse y realizamos el click izquierdo.
        t.sleep(0.5) #Damos un tiempo de descanso para que no se realizen muchos clicks al mismo tiempo al realizar solo uno.
    else:
        led.value = True #Si no se presiona, prendemos el led incorporado en la placa.
        
while True:
    main() #Pedimos que constantemente se ejecute la funcion.