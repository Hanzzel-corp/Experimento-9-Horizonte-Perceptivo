#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌍 Experimento 9A — Horizonte Euclidiano Percibido
Simula cómo el observador (F) proyecta un horizonte curvo sobre un plano lineal,
y cómo se pierde la ortogonalidad al aumentar la distancia.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros base
R = 1.0  # Radio de la esfera
theta = np.linspace(0, 2*np.pi, 400)
phi = np.linspace(0, np.pi/2, 200)
theta, phi = np.meshgrid(theta, phi)

# Superficie esférica (mundo real)
x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)

# Plano tangente (visión humana lineal)
xx, yy = np.meshgrid(np.linspace(-1.2, 1.2, 40), np.linspace(-1.2, 1.2, 40))
zz = np.ones_like(xx) * R

# Proyección del horizonte sobre el plano
proj_x = R * np.sin(phi) * np.cos(theta)
proj_y = R * np.sin(phi) * np.sin(theta)
proj_z = np.ones_like(proj_x) * R

# Curvatura del horizonte (colapso angular)
curvature = np.abs(z - proj_z)
color_map = curvature / curvature.max()

# Gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Superficie real (curva)
ax.plot_surface(x, y, z, color='lightblue', alpha=0.5, linewidth=0)
# Plano de percepción
ax.plot_surface(xx, yy, zz, color='orange', alpha=0.3)
# Proyección aparente
ax.scatter(proj_x, proj_y, proj_z, c=color_map, cmap='plasma', s=0.3)

# Vectores base del observador
ax.quiver(0, 0, R, 0.3, 0, 0, color='red', linewidth=2, label='Horizonte (x)')
ax.quiver(0, 0, R, 0, 0.3, 0, color='green', linewidth=2, label='Vertical (y)')

# Configuración visual
ax.set_title("🧠 Colapso de Ortogonalidad Percibido — Horizonte Linealizado", fontsize=13)
ax.set_xlabel("Eje X (real)")
ax.set_ylabel("Eje Y (real)")
ax.set_zlabel("Eje Z (altura)")
ax.view_init(elev=28, azim=50)
ax.legend()
plt.tight_layout()
plt.show()
