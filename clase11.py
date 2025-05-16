import numpy as np
import matplotlib.pyplot as plt

fs = 100
t= np.linspace(0,2,2*fs) #agarra un rango (los primeros dos nums) y finalmente divide entre 200 trozos, fs = 100 *2
print(t)
print(len(t))
acel = np.zeros_like(t)
print(acel)
acel[:50] = 20
print(acel)
acel = acel -9.8
vel = np.cumsum(acel)/ fs
print(vel)
altura = np.cumsum(vel) / fs
for i in range(len(altura)):
    if altura[i] <= 0:
        altura[i] = altura[i-1]
plt.plot(t,altura)
plt.title('Altura vs tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Altura(m)')
plt.show()
