# Experimento_9B02.py — Documentación

## Descripción

**Experimento 9 — Horizonte Perceptivo (Versión Visual Física Clásica)**

Visualización estática del fenómeno perceptivo donde el cerebro humano proyecta linealidad sobre un horizonte inherentemente curvo.

## Autor

Hanzzel Corp ∑Δ9

## Dependencias

- `numpy` — Cálculos matemáticos y arrays
- `matplotlib` — Visualización 3D
- `mpl_toolkits.mplot3d` — Gráficos 3D
- `matplotlib.cm` — Mapas de colores (coolwarm)

## Parámetros

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `R` | 1.0 | Radio de la esfera terrestre/simulada |
| `phi` | 0 a π/2 (100 puntos) | Ángulo polar del hemisferio |
| `theta` | 0 a 2π (200 puntos) | Ángulo azimutal completo |

## Algoritmo

### 1. Coordenadas Reales (Mundo Curvo)
```
x = R * sin(φ) * cos(θ)
y = R * sin(φ) * sin(θ)
z = R * cos(φ)
```

### 2. Proyección Perceptiva (Plano Lineal)
```
z_proy = R (constante)
delta = |z - z_proy|
```

### 3. Mapeo de Color
El colormap `coolwarm` codifica el error perceptual:
- **Azul**: Bajo error (cerca del observador)
- **Rojo**: Alto error (lejos del observador)

## Visualización

- **Superficie esférica**: Coloreada según el error perceptual Δ
- **Superficie plana naranja**: Plano de proyección perceptiva en z = R
- **Textos dinámicos**:
  - "🌍 Zona donde el cerebro inventa linealidad"
  - "Δ = error perceptivo"

## Vista Inicial

- Elevación: 30°
- Azimut: 45°

## Uso

```bash
python Experimento_9B02.py
```

## Concepto Físico

Este experimento aplica principios de física clásica a la percepción humana:

- El observador en la superficie de una esfera (radio R) percibe localmente un plano tangente
- La diferencia entre la superficie real y el plano perceptivo crece con la distancia
- El cerebro compensa esta diferencia proyectando linealidad

## Salida

Ventana matplotlib con visualización 3D estática del horizonte perceptivo y su error asociado.
