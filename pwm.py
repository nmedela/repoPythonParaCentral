import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BCM)    
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)  
GPIO.setup(18, GPIO.OUT)
white=GPIO.PWM(12, 50)
red = GPIO.PWM(18, 50) 
  
white.start(0)              # Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)  
red.start(100)              # Iniciamos el objeto 'red' al 100% del ciclo de trabajo (completamente encendido)  
  
# A partir de ahora empezamos a modificar los valores del ciclo de trabajo
  
#pause_time = 1           # Declaramos un lapso de tiempo para las pausas
  
try:                        # Abrimos un bloque 'Try...except KeyboardInterrupt'
    while True:             # Iniciamos un bucle 'while true'  
        for i in range(0,101):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            white.ChangeDutyCycle(i)      # LED #1 = i
            red.ChangeDutyCycle(100 - i)  # LED #2 resta 100 - i
            time.sleep(0.02)
        for i in range(100,-1,-1):        # Desde i=100 a i=0 en pasos de -1  
            white.ChangeDutyCycle(i)      # LED #1 = i
            red.ChangeDutyCycle(100 - i)  # LED #2 resta 100 - i  
            time.sleep(0.02)  

except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
    white.stop()            # Detenemos el objeto 'white'
    red.stop()              # Detenemos el objeto 'red'
    GPIO.cleanup()     
