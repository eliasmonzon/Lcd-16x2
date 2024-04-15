from lcd16x2 import LCD_16x2 
import machine
import utime

boton_1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
boton_2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
boton_3 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
boton_4 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

'''
Configura los pines a usar de la pico para
la conexión del lcd a 4 bits 
'''
lcd = LCD_16x2(rs_pin=16, e_pin=17, d4_pin=10, d5_pin=11, d6_pin=12, d7_pin=13)
lcd.clear()



lcd.display_string("THE WORLD IS YOUR", 1, 0)  # Muestra el mensaje en el LCD

#lcd.message("hola mundo")
