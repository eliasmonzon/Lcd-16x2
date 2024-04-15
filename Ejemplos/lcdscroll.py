# Importar los módulos necesarios
from lcd16x2 import LCD_16x2 
import utime

# Inicializar el LCD con los pines correspondientes
lcd = LCD_16x2(rs_pin=16, e_pin=17, d4_pin=10, d5_pin=11, d6_pin=12, d7_pin=13)

# Texto a mostrar en el LCD
texto_completo = "THE WORLD IS YOURS"

while True:
  
    
    
    # Simular el desplazamiento del texto
    for i in range(len(texto_completo)+1 ):  # Longitud del texto menos la longitud de la pantalla (16 caracteres)
        # Obtener la subcadena desplazada
        
        subcadena_visible = texto_completo[i:i+16]  # Mostrar solo los siguientes 16 caracteres
        #limpia la pantalla
        lcd.clear()
        # Mostrar la subcadena en la pantalla
        lcd.display_string(subcadena_visible, 1, 0)
        
        # Esperar un breve período de tiempo para el efecto de desplazamiento
        utime.sleep(1)

