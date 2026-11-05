# 🌌 Experimento 9 — Horizonte Perceptivo
**Colapso de la ortogonalidad y nacimiento de la ilusión del horizonte recto**  
📘 *Hanzzel Corp ∑Δ9 — Proyecto Cero Absoluto / Física clásica aplicada a la percepción*

---

## 🔭 Introducción

Vivimos sobre una superficie curva, pero la percibimos plana.  
Nuestros ojos solo captan unos pocos kilómetros del entorno; más allá, el cerebro pierde la resolución del horizonte y **rellena el vacío con linealidad**.  

Ese “relleno” es el origen de la **ilusión del horizonte recto**, una interpretación geométrica/perceptiva que el experimento propone explorar; la explicación neurocognitiva requeriría evidencia independiente.  

> 🧠 “El ojo no miente: el ojo completa.”  
> La simulación representa cómo una proyección local puede percibirse aproximadamente plana aunque la superficie modelada sea curva.

---

## 📁 Estructura del Proyecto

```bash
Experimento-9-Horizonte-Perceptivo/
├── docs/                           # Documentación detallada
│   ├── README.md                   # Guía de documentación
│   ├── Ortogonalidad_Percibido.md  # Doc del experimento base
│   ├── Ortogonalidad_Percibido01.md # Doc versión animada
│   ├── Experimento_9B.md           # Doc variante animada
│   └── Experimento_9B02.md         # Doc versión con anotaciones
├── Ortogonalidad_Percibido.py      # Experimento base (estático)
├── Ortogonalidad_Percibido01.py    # Versión animada
├── Experimento_9B.py               # Variante animada alternativa
├── Experimento_9B02.py             # Versión con colormap coolwarm
├── README.md                       # Este archivo
└── LICENSE                         # Licencia MIT
```

---

## 🚀 Instalación Rápida

```bash
# Clonar o navegar al directorio
cd Experimento-9-Horizonte-Perceptivo

# Crear entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install numpy matplotlib
```

---

## 🎮 Uso

Ejecuta cualquiera de los scripts:

```bash
python Ortogonalidad_Percibido.py      # Estático - para análisis detallado
python Ortogonalidad_Percibido01.py    # Animado - rotación automática
python Experimento_9B.py               # Animado - variante visual
python Experimento_9B02.py             # Estático con anotaciones
```

---

## 🧩 Modelo del Experimento

- **Realidad física (azul):** una esfera que representa el espacio real.  
- **Percepción humana (naranja):** el plano tangente del observador, que interpreta todo lo que ve como si fuera plano.  
- **Error perceptivo Δ (gradiente):** diferencia entre la posición real y la proyectada sobre el plano.

**Fórmula clave:**

$$
\Delta = |R\cos(\phi) - R|
$$

| Variable | Significado |
|----------|-------------|
| `R` | Radio de la esfera (mundo real) |
| `φ` | Ángulo polar desde el observador |
| `Δ` | Error perceptivo |

- Cuando mirás cerca (φ pequeño), Δ ≈ 0 → el mundo parece plano.  
- Cuando mirás lejos, Δ crece → tu mente empieza a inventar la recta.

---

## ⚙️ Simulaciones Disponibles

| Script | Tipo | Descripción |
|--------|------|-------------|
| `Ortogonalidad_Percibido.py` | Estático | Simulación base con visualización 3D fija. Ideal para análisis detallado del colapso de ortogonalidad. |
| `Ortogonalidad_Percibido01.py` | Animado | Rotación automática de 360° con oscilación vertical. Permite comprender la geometría desde múltiples ángulos. |
| `Experimento_9B.py` | Animado | Variante animada con diferentes parámetros de visualización y gradiente de colores 'plasma'. |
| `Experimento_9B02.py` | Estático | Versión con colormap 'coolwarm' y anotaciones textuales explicativas en la escena 3D. |

---

## 📖 Documentación

Cada script tiene documentación detallada en la carpeta `docs/`:

- [docs/Ortogonalidad_Percibido.md](docs/Ortogonalidad_Percibido.md) — Experimento base
- [docs/Ortogonalidad_Percibido01.md](docs/Ortogonalidad_Percibido01.md) — Versión animada
- [docs/Experimento_9B.md](docs/Experimento_9B.md) — Variante animada
- [docs/Experimento_9B02.md](docs/Experimento_9B02.md) — Versión con anotaciones

---

## 📊 Interpretación de Resultados

| Zona | Color | Interpretación |
|------|-------|----------------|
| Cercana | Azul | El ojo interpreta correctamente; Δ ≈ 0 |
| Intermedia | Gradiente | Comienza el colapso perceptivo |
| Lejana | Roja | Máxima invención lineal del cerebro |

La visualización ilustra una posible diferencia entre geometría global y representación local; no demuestra por sí sola una teoría general de la percepción humana.

---

## 🔮 Conclusión Visual

El horizonte no es recto ni curvo: es una **negociación** entre lo que vemos y lo que podemos comprender.

- La **ortogonalidad** es una herramienta cognitiva, no una propiedad universal.
- El **universo** no se adapta a nosotros; nosotros lo simplificamos para poder existir dentro de él.

---

## 🧭 Créditos

- **Autor:** José Zamora — Hanzzel Corp ∑Δ9
- **Simulación y documentación:** Colaborativa con IA
- **Base teórica:** Observación perceptiva y modelado geométrico euclidiano

---

## � Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

## 📡 Hashtags

#HorizontePerceptivo #HanzzelCorp #Experimento9 #FísicaVisual #PercepciónHumana #Curvatura #Neurociencia #RealidadSimulada #CeroAbsoluto #Linealidad #CienciaVisual #FilosofíaDeLaPercepción

---

## Dirección de investigación y autoría

**José Zamora — Investigador principal independiente (Independent Principal Investigator), Hanzzel Corp.**

Este repositorio es un proyecto individual del ecosistema Hanzzel Corp. La relación técnica de este proyecto con NCT, cuando existe, se limita al alcance descrito en esta documentación; la pertenencia institucional no implica integración adicional ni valida resultados más allá de la evidencia documentada aquí.
