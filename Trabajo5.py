import numpy as np
import matplotlib.pyplot as plt

# Configuración de tiempo
fs = 100  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 5, 5 * fs)  # Tiempo de 0 a 5 segundos

# Función para generar curvas de empuje con forma realista 
def thrust_curve_realista(t, peak, width, shift):
    base_curve = peak * np.exp(-((t - shift)*2) / (2 * width*2))
    # Añadir pequeñas oscilaciones realistas
    ripple = 0.01 * peak * np.sin(25 * t)  # ondulaciones pequeñas
    decay = 1 - 0.15 * np.exp(-(t - shift) * 2)  
    return base_curve * decay + ripple

# Definición de los combustibles y sus parámetros 
combustibles = {
    "HTPB": {"color": "blue", "peak": 5000, "width": 0.6, "shift": 2.0},
    "PBAN": {"color": "red", "peak": 4000, "width": 0.5, "shift": 2.2},
    "Composite": {"color": "gray", "peak": 6000, "width": 0.7, "shift": 2.5},
}

# Crear la figura
plt.figure(figsize=(10, 6))

# Graficar cada curva
for nombre, params in combustibles.items():
    thrust = thrust_curve_realista(t, params["peak"], params["width"], params["shift"])
    thrust = np.clip(thrust, 0, None)  # No permitir valores negativos
    plt.plot(t, thrust / 1000, label=nombre, color=params["color"])  # Mostrar en kN

# Personalización del gráfico
plt.title("Curvas de empuje de combustibles sólidos para cohete")
plt.xlabel("Tiempo (s)")
plt.ylabel("Empuje (kN)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
