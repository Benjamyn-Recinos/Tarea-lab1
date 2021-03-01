# Programa para probar app en el servidor del banco
# Medida de tiempo = minuto

import time

print("\n-----Capacidad máxima del sevidor: 12 apps por minuto-----\n")

# Llegada de apps = 10 * minuto (lambda)
llegada = int(input("¿Cuántas apps llegan por minuto?: "))

# Ejecucion de apps 1 * 5 segundos (miu) 12 por minuto
ejecucion = 12

# llegada de apps
for i in range(llegada):
    if i == 12:
        print("\nError, sobrecarga de apps")
        break
    
    print("\nLlegada de app", i+1)
    print("++++++++++++++++")
    time.sleep(5)  
    print("App", i+1, "probada")
    print("++++++++++++++++")
    
print("\n-----Fin de la simulación-----")   

# Cálculo de Vagancia
vagancia = 1 - (llegada/ejecucion)
percentage = "{:.0%}".format(vagancia)
print("\nLa probabilidad de vagancia del servidor es del", percentage)

# Cálculo de numero promedio de app esperando en cola
try:    
    wq = llegada / (ejecucion*(ejecucion-llegada))
except ZeroDivisionError:
    wq = 0        
print("El numero promedio de apps esperando en cola es de:", round(wq, 4), "\n")