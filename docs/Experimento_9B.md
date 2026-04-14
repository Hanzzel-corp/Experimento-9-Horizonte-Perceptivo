# Experimento_9B.py — Documentación

## Descripción

**Experimento 9B — Horizonte Euclidiano Percibido (Versión Animada)**

Simula la rotación del horizonte curvo proyectado sobre el plano perceptivo para visualizar el colapso de ortogonalidad desde múltiples ángulos en movimiento continuo.

## Autor

Hanzzel Corp ∑Δ9

## Dependencias

- `numpy` — Cálculos matemáticos y generación de mallas
- `matplotlib` — Visualización 3D y animación
- `mpl_toolkits.mplot3d` — Soporte para gráficos 3D

## Parámetros

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `R` | 1.0 | Radio de la esfera que representa el mundo real |
| `theta` | 0 a 2π (400 puntos) | Ángulo azimutal de la esfera |
| `phi` | 0 a π/2 (200 puntos) | Ángulo polar (hemisferio superior) |

## Funcionamiento

1. **Generación de datos**: Crea una malla esférica que representa la realidad física curva
2. **Plano perceptivo**: Genera un plano tangente que simula la visión humana linealizada
3. **Proyección**: Calcula cómo el horizonte curvo se proyecta sobre el plano perceptivo
4. **Mapa de curvatura**: Calcula el error perceptual como la diferencia entre la realidad y la proyección
5. **Animación**: Rota automáticamente la vista 3D durante 360 frames para observar el fenómeno desde todos los ángulos

## Visualización

- **Esfera azul claro**: Representa el mundo real (curvo)
- **Plano naranja**: Representa la percepción humana (plano)
- **Gradiente de colores**: Indica el error perceptual (curvatura)
- **Vectores rojo/verde**: Ejes de referencia del observador

## Función de Animación

```python
def rotar(frame):
    ax.view_init(elev=25 + np.sin(frame/50)*10, azim=frame)
```

Rota la vista con oscilación vertical suave mientras completa una rotación completa (360°).

## Uso

```bash
python Experimento_9B.py
```

La animación se ejecuta en una ventana matplotlib con rotación continua.

## Salida

Ventana 3D interactiva con animación del colapso de ortogonalidad desde múltiples perspectivas.
