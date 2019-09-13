import matplotlib.pyplot as plt
import random
import numpy as np

eta = 0.2
max_epoch = 20


# datos de entrada
num_muestras = 20
max_pendiente = 9
min_pendiente = 5
max_ordenadas = 1.5
min_ordenadas = 1
ruido = 2.5

# generacion de datos
X = np.random.randint(1, num_muestras, size=50)
# pendiente = min_pendiente + \
#     (max_pendiente - min_pendiente) * np.random.uniform(1)
# ordenada = min_ordenadas + \
#     (max_ordenadas - min_ordenadas) * np.random.uniform(1)
# Y = pendiente*X + ordenada
# Y = Y + ruido * np.random.randn(20, 1)

# escalar datos

# X = (X - min(X)) / max(X) - min(X)
# Y = (Y - min(Y) / max(Y) - min(Y))
# plt.plot(X, Y, color='b')
# plt.show()
print(X)


# # crear ADALINE

# dim = 1
# w = -1 + 2*np.random.rand(dim, 1)
# b = -1 + 2*np.random.rand()

# # Entrenar

# for i in range(max_epoch):
#     for p in range(num_muestras):
#         # prediccion
#         y_pred = w.T * X[p] + b
#         # entrenamiento
#         w = w + eta + (Y[p] - y_pred) * X[p]
#         b = b + eta * (Y[p] - y_pred)


# y1 = w.T * 0 + b
# y2 = w.T * 1 + b

# plt.plot([0, 1], [y1, y2], "r")

# plt.show()
