import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(steps, delta_t=1, diffusion_coefficient=1):
    """
    Simula un movimiento browniano en 2D.

    steps: Número de pasos de la partícula.
    delta_t: Incremento de tiempo en cada paso.
    diffusion_coefficient: Coeficiente de difusión que escala la varianza.
    """
    x, y = [0], [0]  # Posición inicial en el origen

    sigma = np.sqrt(2 * diffusion_coefficient * delta_t)  # Desviación estándar

    for _ in range(steps):
        dx = np.random.normal(0, sigma)
        dy = np.random.normal(0, sigma)

        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    return x, y

# Parámetros de simulación
steps = 1000
diffusion_coefficient = 1
x, y = brownian_motion(steps, diffusion_coefficient=diffusion_coefficient)

# Graficar la trayectoria
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker=".", linestyle="-", alpha=0.6, markersize=3)
plt.scatter([x[0]], [y[0]], color='green', label="Inicio", zorder=3)
plt.scatter([x[-1]], [y[-1]], color='red', label="Fin", zorder=3)
plt.xlabel("Dirección X")
plt.ylabel("Dirección Y")
plt.title("Simulación de Movimiento Browniano (Pasos Gaussianos)")
plt.legend()
plt.grid(True)
plt.show()
