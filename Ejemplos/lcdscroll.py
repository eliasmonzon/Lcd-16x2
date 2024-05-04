# Importar los módulos necesarios
from lcd16x2 import LCD_16x2 
import utime

# Configura los pines a usar de la pico para la conexión del lcd a 4 bits
# RS, E, D4, D5, D6, D7
lcd = LCD_16x2(16,17,10,11,12,13) 
lcd.clear()
# Texto a mostrar en el LCD
texto_completo = "EL MUNDO ES TUYO"

while True:
    #Bucle desplazamiento del texto
    for i in range(len(texto_completo)+1 ):  # Longitud del texto menos la longitud de la pantalla (16 caracteres)
        # Obtener la subcadena desplazada
        subcadena_visible = texto_completo[i:i+16]  # Mostrar solo los siguientes 16 caracteres
        #limpia la pantalla
        lcd.clear()
        utime.sleep(0.01)
        # Mostrar la subcadena en la pantalla fila 1 columna 0
        lcd.display_string(subcadena_visible, 1, 0)
        # Esperar un breve período de tiempo para el efecto de desplazamiento
        utime.sleep(1)

