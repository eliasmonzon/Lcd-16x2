from lcd16x2 import LCD_16x2 
import machine
import utime



'''
Configura los pines a usar de la pico para
la conexión del lcd a 4 bits 
'''
lcd = LCD_16x2(rs_pin=16, e_pin=17, d4_pin=10, d5_pin=11, d6_pin=12, d7_pin=13)
lcd.clear()



lcd.display_string("THE WORLD IS YOUR", 1, 0)  # Muestra el mensaje en el LCD

#lcd.message("hola mundo")
