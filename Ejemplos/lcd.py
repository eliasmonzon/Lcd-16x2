from lcd16x2 import LCD_16x2 
import machine
import utime

'''
Configura los pines a usar de la pico para
la conexión del lcd a 4 bits 
RS, E, D4, D5, D6, D7
'''
lcd = LCD_16x2(16,17,10,11,12,13) 
lcd.clear()
#Caracteres que seran mostrados :
caracter1= [
     0B01110,
     0B10001,
     0B10010,
     0B10100,
     0B10100,
     0B10010,
     0B10001,
     0B01110,
 ]

caracter2= [
  0B01110,
  0B10001,
  0B10001,
  0B11011,
  0B10001,
  0B10001,
  0B11011,
  0B10101,
 ]
# LLama a los caracteres 0 y 1 
lcd.create_char(0, caracter1)
lcd.create_char(1, caracter2)
 # Muestra el mensaje en el LCD
lcd.display_string("Hola Mundo", 1, 0)
# Muestra los caracteres en pantalla
lcd.display_string("\x00\x01 \x01 \x01", 2, 0)  # Muestra los caracteres personalizados en la fila 1


