import numpy as np
import matplotlib.pyplot as plt

weigth = 4
bascula = [0, 0.002, 0.003, 0.004, 0.005, 0.007, 1.32, 5.52, 1.84, 2.6, 0.88, 0.96, 0.98, 1.01, 1.03, 1.05]

x = np.arange(len(bascula))

peso_constante = [weigth] * len(bascula)

promedio = [(b + weigth) / 2 for b in bascula]

plt.figure(figsize=(10, 5))

plt.plot(x, peso_constante, label='Peso constante (4 kg)', color='green', linestyle='--')

plt.plot(x, bascula, label='Mediciones de la báscula', marker='o')

plt.plot(x, promedio, label='Promedio (medición + peso) / 2', marker='x', color='red')

plt.title("Comparación entre Peso Constante, Mediciones y Promedio")
plt.xlabel("Índice de medición")
plt.ylabel("Peso (kg)")
plt.grid(True)
plt.legend()
plt.tight_layout()


plt.show()
