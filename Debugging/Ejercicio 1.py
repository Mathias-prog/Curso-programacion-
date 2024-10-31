def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio:
            print(f"{num} es mayor que el promedio.")
        elif num < promedio:
            print(f"{num} es menor que el promedio.")
        else:
            print(f"{num} es igual al promedio.")
#las lineas 6 8 y 10 no les faltaban los dos puntos despues de promedio, promedio y else respectivamente error de syntax
# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = float(input("Introduce un número: ")) #hacia falta un float ya que sin este el numero introducido por el usuario seria tomado como un string y esto generaria un error de tipo
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)
