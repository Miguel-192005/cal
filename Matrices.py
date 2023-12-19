import numpy as np

A = np.array([[-19, 2, 0],
              [2, -5.5, 0],
              [1, -1, -1]])

b = np.array([20, -7, 0])

np.set_printoptions(precision=5)

Inversa = np.linalg.inv(A)

print("La inversa de la matris es:\n\n" ,Inversa)

Respuesta = np.dot(np.linalg.inv(A), b)

print("\n La Matriz solucion es:\n", Respuesta)
// este codigo se subio por error solo es un programa en python para resolver matrices 3x3 que cree 
