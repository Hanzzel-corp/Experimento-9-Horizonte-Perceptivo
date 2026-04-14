#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌌 Experimento 9 — Horizonte Perceptivo
Autor: Hanzzel Corp ∑Δ9
Versión Visual — Física Clásica Aplicada a la Percepción
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parámetros
R = 1.0  # radio de la esfera
phi = np.linspace(0, np.pi / 2, 100)
theta = np.linspace(0, 2 * np.pi, 200)
phi, theta = np.meshgrid(phi, theta)

# Coordenadas reales
x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)

# Proyección sobre el plano perceptivo
z_proy = np.ones_like(z) * R
delta = np.abs(z - z_proy)

# Visualización
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Esfera (realidad)
ax.plot_surface(x, y, z, facecolors=cm.coolwarm(1 - delta / delta.max()), rstride=2, cstride=2, alpha=0.8)
ax.plot_surface(x, y, z_proy, color='orange', alpha=0.3)

# Etiquetas y título
ax.text(0, 0, 1.3, "🌍 Zona donde el cerebro inventa linealidad", color='red', fontsize=12, ha='center')
ax.text(0, 0, 1.1, "Δ = error perceptivo", color='white', fontsize=10, ha='center')

ax.set_title("🌌 Experimento 9 — Horizonte Perceptivo", fontsize=14, color='cyan')
ax.set_xlabel("X (horizonte)")
ax.set_ylabel("Y (periferia visual)")
ax.set_zlabel("Z (vertical)")

ax.view_init(elev=30, azim=45)
plt.tight_layout()
plt.show()

