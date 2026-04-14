# Ortogonalidad_Percibido01.py — Documentación

## Descripción

**Experimento 9B — Horizonte Euclidiano Percibido (Versión Animada Alternativa)**

Esta versión animada complementa el Experimento 9A con rotación dinámica de la cámara, permitiendo observar el colapso de ortogonalidad desde perspectivas cambiantes.

## Autor

Hanzzel Corp ∑Δ9

## Diferencias con Ortogonalidad_Percibido.py

| Aspecto | Ortogonalidad_Percibido.py | Ortogonalidad_Percibido01.py |
|---------|---------------------------|------------------------------|
| Tipo | Estático | Animado |
| Interacción | Vista fija | Rotación automática |
| Objetivo | Análisis detallado | Comprensión espacial dinámica |

## Dependencias

- `numpy` — Operaciones matemáticas vectorizadas
- `matplotlib` — Framework de visualización
- `mpl_toolkits.mplot3d` — Proyección 3D
- `matplotlib.animation` — Motor de animación

## Parámetros de Simulación

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `R` | 1.0 | Radio esférico normalizado |
| `theta` | 0 a 2π, 400 pasos | Resolución azimutal |
| `phi` | 0 a π/2, 200 pasos | Resolución polar (hemisferio) |

## Estructura del Código

### PARTE 1: Datos Base
Generación de la geometría esférica y del plano perceptivo.

### PARTE 2: Visualización Inicial
Configuración de la escena 3D con:
- Superficie esférica translúcida
- Plano perceptivo naranja
- Scatter plot del error proyectado
- Vectores de referencia del observador

### PARTE 3: Función de Animación
```python
def rotar(frame):
    ax.view_init(elev=25 + sin(frame/50)*10, azim=frame)
```

### PARTE 4: Renderizado
```python
anim = FuncAnimation(fig, rotar, frames=360, interval=40, blit=False)
```

**Parámetros de animación:**
- `frames`: 360 (rotación completa)
- `interval`: 40ms entre frames (~25 fps)
- `elev`: Oscila entre 15° y 35°
- `azim`: Rota 0° a 360°

## Paleta de Colores

| Elemento | Color | Alpha | Propósito |
|----------|-------|-------|-----------|
| Esfera | lightblue | 0.4 | Mostrar estructura sin ocultar |
| Plano | orange | 0.3 | Indicar plano perceptivo |
| Scatter | plasma | - | Codificar error perceptual |
| Eje X | red | 1.0 | Orientación horizonte |
| Eje Y | green | 1.0 | Orientación vertical |

## Uso

```bash
python Ortogonalidad_Percibido01.py
```

## Notas Técnicas

- `blit=False` fuerza redibujado completo (necesario para 3D)
- El intervalo de 40ms balancea fluidez y carga de CPU
- La oscilación vertical (sin) añade dinamismo sin mareo

## Concepto Visualizado

El experimento demuestra que:
1. La percepción humana opera como una proyección plana
2. La curvatura real solo es apreciable a gran escala
3. El cerebro compensa la discrepancia con "inventos" perceptivos
4. La ortogonalidad es una construcción local, no global
