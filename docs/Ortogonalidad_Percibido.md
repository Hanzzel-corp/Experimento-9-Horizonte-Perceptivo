# Ortogonalidad_Percibido.py — Documentación

## Descripción

**Experimento 9A — Horizonte Euclidiano Percibido**

Simulación estática que modela cómo un observador proyecta un horizonte curvo sobre un plano lineal, demostrando visualmente la pérdida de ortogonalidad a medida que aumenta la distancia.

## Autor

Hanzzel Corp ∑Δ9

## Dependencias

- `numpy` — Cálculos numéricos y generación de mallas
- `matplotlib` — Visualización 3D
- `mpl_toolkits.mplot3d` — Soporte 3D para matplotlib

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `R` | 1.0 | Radio normalizado de la esfera |
| `theta` | 400 puntos (0 a 2π) | Resolución angular azimutal |
| `phi` | 200 puntos (0 a π/2) | Resolución angular polar |

## Componentes del Modelo

### 1. Superficie Real (Curva)
```python
x = R * sin(φ) * cos(θ)
y = R * sin(φ) * sin(θ)
z = R * cos(φ)
```
Representa el mundo físico real con curvatura.

### 2. Plano Tangente (Percepción)
```python
xx, yy ∈ [-1.2, 1.2]
zz = R (constante)
```
Representa cómo el sistema visual humano interpreta el espacio: como un plano local.

### 3. Proyección del Horizonte
```python
proj_x = R * sin(φ) * cos(θ)
proj_y = R * sin(φ) * sin(θ)
proj_z = R
```
Los puntos del horizonte real proyectados sobre el plano perceptivo.

### 4. Métrica de Curvatura
```python
curvature = |z - proj_z|
color_map = curvature / curvature.max()
```
Normaliza el error perceptual para visualización con colormap 'plasma'.

## Elementos Visuales

| Elemento | Color | Significado |
|----------|-------|-------------|
| Esfera | Azul claro (α=0.5) | Realidad física curva |
| Plano | Naranja (α=0.3) | Percepción linealizada |
| Puntos proyectados | Gradiente 'plasma' | Error perceptivo Δ |
| Vector X | Rojo | Eje del horizonte |
| Vector Y | Verde | Eje vertical local |

## Configuración de Vista

- **Elevación**: 28°
- **Azimut**: 50°
- **Título**: "🧠 Colapso de Ortogonalidad Percibido — Horizonte Linealizado"

## Uso

```bash
python Ortogonalidad_Percibido.py
```

## Interpretación

- **Cerca del observador**: La curvatura es mínima, el plano tangente aproxima bien la realidad
- **Lejos del observador**: La diferencia entre la esfera y el plano crece, el cerebro "inventa" la linealidad
- **Gradiente de colores**: Zonas rojas indican mayor invención perceptiva

## Referencias Conceptuales

- Geometría diferencial: plano tangente a superficie esférica
- Psicofísica de la percepción espacial
- Fenómeno del horizonte aparentemente recto
