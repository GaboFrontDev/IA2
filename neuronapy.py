import matplotlib.pyplot as plt
import random
import numpy as np


def act_fun(val):
    return 1 if val > 0 else 0


entradas = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
]
# D = [0, 0, 0, 1]
D = [0, 1, 1, 1]

umbral = 0
etha = 0.1
peso1 = random.uniform(-1, 1)
peso2 = random.uniform(-1, 1)
print(peso1, peso2)
errors = [True, True, True, True]
salidas = [0, 1, 1, 0]
converge = False
idx = 0
pasos = 0
while True in errors:  # until converge
    pasos += 1
    #prod_punto = np.dot([peso1, peso2], entradas[idx])
    prod_punto = (entradas[idx][0]*peso1 + entradas[idx][1]*peso2) + umbral
    print(prod_punto)
    print("El resultado del producto punto es: ", prod_punto)
    y = act_fun(prod_punto)
    salidas[idx] = y

    print("Deseado: ", D[idx])
    print("Obtenido: ", y)
    error = D[idx] - y
    if error != 0:
        print("Recalculando pesos...")
        peso1 = peso1 + etha * error * entradas[idx][0]
        peso2 = peso2 + etha * error * entradas[idx][1]
        print("pesos: ", [peso1, peso2])
        umbral = umbral + etha*error
        print("umbral: ", umbral)
        errors[idx] = True
    else:
        errors[idx] = False
    idx += 1
    if idx >= len(entradas):
        x1 = np.linspace(-3, 3, 20)
        x2 = (-peso1/peso2) * x1 - (umbral / peso2)
        #graph = [[x, x*m+b]for x in np.linspace(-3, 3, 20)]
        print("salida: ", y)
        #print("linea: ", graph)
        for entrada, step in zip(entradas, D):
            plt.scatter(entrada[0], entrada[1],
                        color="blue" if step else "red")

        #plt.plot(x1, x2)
        idx = 0

print("Entrenamiento terminado, se obtuvo: ", salidas)
print("Cantidad de iteraciones: ", pasos)
x1 = np.linspace(-3, 3, 20)
x2 = (-peso1/peso2) * x1 - (umbral / peso2)
plt.plot(x1, x2)
plt.show()
