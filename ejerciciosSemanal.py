# Pequeño progama que utiliza el Módulo de MatPlotLib para generar una gráfica de los ejericicos que he hecho esta semana
# TRACKING DE EJERCICIOS v1
import matplotlib.pyplot as plt

"""   Inicializar los parametros   """
semanas_Mes = [1,2,3,4] # Eje X
# Dias de la Semana
weekdays = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
# Semanas
semanas = []
semanal = []

"""" Tomar Inputs"""

# Semanas
cant = int(input("Semanas que quiere graficar: "))
for i in range(cant):
    semanas.append([])

# Periodo
#ini = int(input("Fecha de inicio de la semana: "))
#fin = int(input("Fecha de fin de la semana: "))

# Repeticiones
for i in range(cant):
    for j in range(7):
        ejercicios = int(input("Por favor introduzca sus repeticiones del dia " + str(weekdays[j]) + " de la semana " + str(i + 1) + " :"))
        semanas[i].append(ejercicios)

# Realizar la grafica con los datos obtenidos
for i in range(cant):
    semanal.append(sum(semanas[i]))

plt.plot(semanas_Mes, semanal, semanas_Mes, semanal, "bo")
plt.xlabel('Semana del Mes')
plt.ylabel('Repeticiones totales')
plt.suptitle("Aumento Mensual de Ejercicios")
# plt.suptitle("Ejercicios Semana " + str(ini) + " - " + str(fin))
plt.show()