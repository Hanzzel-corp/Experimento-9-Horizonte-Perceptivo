#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌍 Experimento 9B — Horizonte Euclidiano Percibido (Versión Animada)
Simula la rotación del horizonte curvo proyectado sobre el plano perceptivo
para visualizar el colapso de ortogonalidad desde múltiples ángulos.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# --- PARTE 1: Datos base ---
R = 1.0  # Radio de la esfera
theta = np.linspace(0, 2*np.pi, 400)
phi = np.linspace(0, np.pi/2, 200)
theta, phi = np.meshgrid(theta, phi)

# Esfera real (mundo curvo)
x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)

# Plano perceptivo (visión humana)
xx, yy = np.meshgrid(np.linspace(-1.2, 1.2, 40), np.linspace(-1.2, 1.2, 40))
zz = np.ones_like(xx) * R

# Proyección del horizonte sobre el plano
proj_x = R * np.sin(phi) * np.cos(theta)
proj_y = R * np.sin(phi) * np.sin(theta)
proj_z = np.ones_like(proj_x) * R

# Mapa de curvatura / error perceptual
curvature = np.abs(z - proj_z)
color_map = curvature / curvature.max()

# --- PARTE 2: Visualización inicial ---
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Dibujar las superficies base
sphere = ax.plot_surface(x, y, z, color='lightblue', alpha=0.4, linewidth=0)
plane = ax.plot_surface(xx, yy, zz, color='orange', alpha=0.3)
scatter = ax.scatter(proj_x, proj_y, proj_z, c=color_map, cmap='plasma', s=0.3)

# Vectores del observador
ax.quiver(0, 0, R, 0.3, 0, 0, color='red', linewidth=2, label='Horizonte (x)')
ax.quiver(0, 0, R, 0, 0.3, 0, color='green', linewidth=2, label='Vertical (y)')

# Etiquetas y estilo
ax.set_title("🌍 Colapso de Ortogonalidad Percibido — Horizonte Linealizado (Animación)", fontsize=13)
ax.set_xlabel("Eje X (real)")
ax.set_ylabel("Eje Y (real)")
ax.set_zlabel("Eje Z (altura)")
ax.legend()

# --- PARTE 3: Función de animación ---
def rotar(frame):
    # Rotación suave del punto de vista
    ax.view_init(elev=25 + np.sin(frame/50)*10, azim=frame)
    return fig,

# --- PARTE 4: Animación ---
anim = animation.FuncAnimation(fig, rotar, frames=360, interval=40, blit=False)

plt.tight_layout()
plt.show()

