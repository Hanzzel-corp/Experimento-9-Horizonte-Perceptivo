# Documentación del Proyecto — Experimento 9

## Índice

- [Descripción General](#descripción-general)
- [Archivos del Proyecto](#archivos-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de Documentos](#estructura-de-documentos)
- [Marco Teórico](#marco-teórico)
- [Licencia](#licencia)

---

## Descripción General

Este proyecto explora el **colapso de la ortogonalidad en la percepción humana**, específicamente el fenómeno por el cual interpretamos un horizonte curvo como recto.

Desarrollado por **Hanzzel Corp ∑Δ9** como parte del *Proyecto Cero Absoluto*, combina física clásica, geometría diferencial y visualización científica para demostrar cómo el cerebro compensa la curvatura de la realidad con proyecciones lineales.

## Archivos del Proyecto

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `Ortogonalidad_Percibido.py` | Estático | Simulación base del colapso de ortogonalidad |
| `Ortogonalidad_Percibido01.py` | Animado | Versión animada con rotación de cámara |
| `Experimento_9B.py` | Animado | Variante animada con diferentes parámetros visuales |
| `Experimento_9B02.py` | Estático | Visualización con colormap coolwarm y anotaciones |

## Requisitos

```
python >= 3.8
numpy >= 1.20.0
matplotlib >= 3.5.0
```

## Instalación

```bash
# Clonar o navegar al directorio
cd 9-ortogonalidad

# Crear entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o: .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install numpy matplotlib
```

## Uso

Cada script puede ejecutarse independientemente:

```bash
# Versión estática básica
python Ortogonalidad_Percibido.py

# Versión animada
python Ortogonalidad_Percibido01.py

# Variante animada alternativa
python Experimento_9B.py

# Versión con anotaciones
python Experimento_9B02.py
```

## Estructura de Documentos

La carpeta `docs/` contiene documentación detallada de cada archivo:

| Documento | Contenido |
|-----------|-----------|
| `Ortogonalidad_Percibido.md` | Guía completa del experimento base |
| `Ortogonalidad_Percibido01.md` | Documentación de la versión animada |
| `Experimento_9B.md` | Referencia de la variante animada |
| `Experimento_9B02.md` | Manual de la versión con anotaciones |

## Marco Teórico

### Fórmula del Error Perceptual

```
Δ = |R·cos(φ) - R|
```

Donde:
- `R`: Radio de la esfera
- `φ`: Ángulo polar desde el observador
- `Δ`: Error perceptivo (diferencia entre realidad y proyección)

### Interpretación

- **φ ≈ 0** (cerca): Δ ≈ 0, la percepción coincide con la realidad
- **φ aumenta**: Δ crece, el cerebro compensa con linealidad proyectada
- **φ = π/2** (horizonte): Δ máximo, máxima "invención" perceptiva

## Licencia

Este proyecto está licenciado bajo la **MIT License**.

Ver archivo `LICENSE` para el texto completo.

---

**Proyecto Cero Absoluto**  
*Física clásica aplicada a la percepción*  
Hanzzel Corp ∑Δ9 — 2026
