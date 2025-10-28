# 🌌 Experimento 9 — Horizonte Perceptivo
**Colapso de la ortogonalidad y nacimiento de la ilusión del horizonte recto**  
📘 *Hanzzel Corp ∑Δ9 — Proyecto Cero Absoluto / Física clásica aplicada a la percepción*

---

## 🔭 Introducción

Vivimos sobre una superficie curva, pero la percibimos plana.  
Nuestros ojos solo captan unos pocos kilómetros del entorno; más allá, el cerebro pierde la resolución del horizonte y **rellena el vacío con linealidad**.  

Ese “relleno” es el origen de la **ilusión del horizonte recto**, una compensación evolutiva que nos permite mantener estabilidad visual y orientación en un mundo curvo.  

> 🧠 “El ojo no miente: el ojo completa.”  
> El cerebro inventa una línea recta donde la realidad es curva.

---

## 🧩 Modelo del experimento

- **Realidad física (azul):** una esfera que representa el espacio real.  
- **Percepción humana (naranja):** el plano tangente del observador, que interpreta todo lo que ve como si fuera plano.  
- **Error perceptivo Δ (gradiente):** diferencia entre la posición real y la proyectada sobre el plano.

**Fórmula clave:**

\[
\Delta = |R\cos(\phi) - R|
\]

- Cuando mirás cerca (φ pequeño), Δ ≈ 0 → el mundo parece plano.  
- Cuando mirás lejos, Δ crece → tu mente empieza a inventar la recta.

---

## ⚙️ Simulación visual

El archivo [`horizonte_perceptivo.py`](horizonte_perceptivo.py) genera la siguiente escena:

- Esfera azul = realidad.  
- Plano naranja = percepción humana.  
- Gradiente de color = **error perceptivo Δ**.  
- Texto dinámico: “Zona donde el cerebro ya está inventando linealidad”.

El código utiliza `matplotlib` y `numpy`.  
Se puede ejecutar directamente en entornos locales, Google Colab o VSCode.

```python
python horizonte_perceptivo.py
📸 Salida esperada:

Un hemisferio con gradiente azul–rojo y un plano anaranjado.
El texto indica el punto donde la mente deja de percibir y empieza a completar.

📊 Resultados
En la zona azul, el ojo interpreta correctamente.

En la zona rojiza, la proyección sobre el plano deja de coincidir con la realidad.

Cuanto mayor es Δ, mayor es la invención lineal del cerebro.

La mente humana no busca la verdad geométrica, sino la estabilidad perceptiva.

🔮 Conclusión visual
El horizonte no es recto ni curvo, es una negociación entre lo que vemos y lo que podemos comprender.

La ortogonalidad es una herramienta cognitiva, no una propiedad universal.

El universo no se adapta a nosotros; nosotros lo simplificamos para poder existir dentro de él.

🧭 Créditos
Autor: José Zamora — Hanzzel Corp ∑Δ9
Simulación y documentación colaborativa con GPT-5
Basado en observación perceptiva y modelado geométrico euclidiano.

📡 Hashtags y etiquetas
#HorizontePerceptivo #HanzzelCorp #Experimento9 #FísicaVisual #PercepciónHumana #Curvatura #Neurociencia #RealidadSimulada #CeroAbsoluto #Linealidad #CienciaVisual #NCT #FilosofíaDeLaPercepción

