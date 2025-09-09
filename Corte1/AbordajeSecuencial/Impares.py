# Este ejercicio vale 1 decima del primer corte 
import signal
import sys 
import time 
#def ctrlc(signum,frame):
#    print("Proceso Terminado")
#signal.signal(signal.SIGINT,ctrlc)

try:
    while True:  
        print("Ingresa un numero:")
        numero1=0
        numero1=input(numero1)
        int(numero1)
        if numero1==ValueError:
         print("El numero no es valido")
        else:
            mod=numero1/2
            if mod!=0:
                print("El numero es impar")
            else:
                print("El numero es par")
                print("Presionar Ctrl+C para finalizar")
except KeyboardInterrupt:
    print("\nProceso finalizado")






