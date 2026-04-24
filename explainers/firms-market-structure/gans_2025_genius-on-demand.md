# Genius on Demand: The Value of Transformative Artificial Intelligence

**Autores / Authors:** Ajay K. Agrawal, Joshua S. Gans, Avi Goldfarb
**Año / Year:** 2025
**Publicación / Venue:** NBER Working Paper No. 34316
**PDF:** [papers/pdfs/gans_2025_genius-on-demand.pdf](../../papers/pdfs/gans_2025_genius-on-demand.pdf)
**Fuente / Source:** https://www.nber.org/papers/w34316

## 1. Cita completa

Agrawal, Ajay K., Joshua S. Gans y Avi Goldfarb (2025). *Genius on Demand: The Value of Transformative Artificial Intelligence*. NBER Working Paper No. 34316, octubre. JEL: D24, J24, O33.

## 2. Pregunta de investigación

¿Cómo absorbería el mercado laboral una "avalancha" de capacidad cognitiva tipo "genio" provista por IA transformadora —lo que Amodei (2024) llama "un país de genios en un centro de datos"— y qué consecuencias tendría para distintos tipos de trabajadores del conocimiento, en el corto y en el largo plazo? (PDF p. 3).

## 3. Método

- **Modelo teórico**, no empírico. Construye sobre Carnehl & Schneider (2025), que representa el conocimiento como pares pregunta-respuesta distribuidos en la recta real, con la respuesta verdadera generada por un movimiento browniano estándar (PDF p. 5).
- **Tres tipos de agentes**: (i) trabajadores rutinarios, que aplican conocimiento existente con varianza creciente en la distancia |x − x₀| al punto conocido; (ii) genios humanos, que crean conocimiento nuevo con costo cuadrático Cost(x) = η·(x − x₀)² (PDF p. 9); (iii) un *manager* que enruta cada pregunta al tipo de trabajador adecuado (PDF p. 11).
- **Función de valor**: la utilidad sigue una pérdida cuadrática 1 − (a(x) − y(x))²/q, con un parámetro de precisión q que define el umbral por encima del cual los rutinarios se abstienen (PDF p. 6).
- **Supuestos clave**: dominio uniforme [0,1] con x₀ = ½ y ½ > q; rutinarios abundantes (L_R ≥ 2q) pero genios escasos (L_G < 1); η ≤ 4 para que los genios cubran todo el dominio (PDF pp. 6–9).
- **IA**: se introduce como "genio" autónomo con función de costo simétrica pero potencialmente menos eficiente, η_AI ≥ η, y oferta efectivamente ilimitada (PDF pp. 14–15).
- **Comparativa estática**: corto plazo (asignación rutinaria fija por rigideces) vs. largo plazo (re-optimización completa).

## 4. Hallazgos principales

- **Asignación óptima sin IA**: cuando los genios son escasos, deben asignarse primero a las preguntas con mayor *ventaja absoluta* AA(x) = V_G(x) − V_R(x). Esto NO ocurre en los puntos más alejados (donde su costo es máximo) sino en los bordes del dominio rutinario, donde los rutinarios ya no pueden contestar pero el costo del genio aún es moderado (PDF p. 11).
- **Dos regímenes según η**: si η ≤ 1/(2q²) la capacidad escasa de genios va primero a los bordes x₀ ± q ("edge-first"); si η > 1/(2q²) va a bandas interiores en x₀ ± 1/(2ηq) ("interior-first"). En ambos casos las bandas se ensanchan al aumentar L_G (PDF pp. 12–13).
- **Corto plazo con IA (Proposición 2)**: surge una asignación de tres niveles —los genios humanos se especializan en las preguntas más alejadas del conocimiento existente (donde su ventaja sobre la IA, (η_AI − η)·(x − x₀)², es mayor); las IA cubren preguntas intermedias y rellenan zonas previamente sin respuesta; los rutinarios mantienen su asignación pre-IA (PDF pp. 15–16).
- **Largo plazo (Proposición 3)**: si η_AI está suficientemente cerca de η, los **trabajadores rutinarios son completamente desplazados** del trabajo de conocimiento. La condición exacta es η_AI ≤ 1/q²; si se cumple, la IA reemplaza al trabajo rutinario en toda la Región 2 (PDF p. 18).
- **Especialización extrema del talento humano**: en el largo plazo los genios humanos quedan asignados exclusivamente a las preguntas con |x − x₀| ≥ d*, donde d* se fija por la restricción de capacidad L_G (PDF p. 18). Es decir, el talento humano se "ultra-especializa" en la frontera más novedosa.
- **Expansión del dominio respondible**: preguntas en las Regiones 1 y 3 que antes quedaban sin respuesta ahora reciben respuesta de IA o de genios humanos, ampliando el conjunto total de problemas que la economía puede abordar (PDF pp. 18–19).

## 5. Implicaciones para política pública (Colombia / América Latina)

- **El "piso" del trabajo del conocimiento es el más expuesto, no el techo.** El modelo predice que el grupo más vulnerable no es el experto creativo sino el trabajador rutinario que aplica conocimiento codificado: paralegales, residentes médicos en diagnóstico estándar, desarrolladores que implementan algoritmos conocidos (PDF p. 7). En Colombia esto cubre buena parte del empleo formal urbano de cuello blanco —servicios jurídicos, contables, BPO— sectores que han sido motor de empleo profesional en los últimos 15 años.
- **Política educativa: invertir en "frontera", no solo en "aplicación".** Si los genios humanos sobrevivientes se concentran en preguntas con |x − x₀| grande, los retornos a programas de doctorado, investigación aplicada y formación de especialistas-frontera (medicina especializada, derecho de innovación, ingeniería de investigación) crecen relativamente. La ampliación masiva de pregrados orientados a tareas rutinarias de oficina podría tener retornos decrecientes.
- **Capacidad de cómputo y acceso a IA "genio".** El modelo asume oferta ilimitada de IA-genio una vez desarrollada (PDF p. 15). Para América Latina, sin frontera tecnológica propia, la pregunta de política es el acceso (precio, soberanía de datos, contratos con proveedores extranjeros) más que el desarrollo. Sin acceso barato, el régimen relevante es η_AI alto y el desplazamiento rutinario es lento o parcial.
- **Tránsito laboral**: la distinción corto/largo plazo (PDF pp. 15, 17) sugiere que el ajuste no es instantáneo —las rigideces organizacionales protegen a los rutinarios temporalmente. Esa ventana es la oportunidad para reconversión activa (no pasiva) de la fuerza laboral profesional.

## 6. Debates y caveats

- **Modelo de sustitución pura vs. modelos de complementariedad.** El propio paper reconoce, en la conclusión, que modela la IA como "agente independiente que reemplaza" y que esto "puede no capturar el potencial más prometedor" (PDF p. 18). Los mismos autores, en `agrawal-gans-goldfarb_2025_bicycles-for-the-mind`, exploran la visión opuesta —IA como herramienta complementaria, no como sustituto autónomo. Las dos perspectivas conviven en el mismo equipo de investigación.
- **Tractabilidad vs. realismo.** El modelo asume un único punto de conocimiento, distribución uniforme de preguntas, costo cuadrático y un manager omnisciente sobre capacidades de los trabajadores (PDF pp. 5–11). No hay heterogeneidad dentro de "rutinario" ni dentro de "genio", ni jerarquías à la Garicano.
- **Sin números empíricos.** A diferencia de `acemoglu_2024_simple-macro-ai` (que estima ~0.66% de ganancia de TFP en 10 años) o `aghion-bunel_2024_ai-and-growth` (0.8–1.3 puntos porcentuales por año), aquí no hay calibración macro. Las predicciones son cualitativas: dirección de la asignación, no magnitud del impacto en empleo o PIB.
- **Asume η_AI ≥ η.** Si la IA fuera más eficiente que los humanos también en la frontera (η_AI < η), el modelo predice sustitución inmediata e indiscriminada de todos los genios humanos (PDF p. 14, nota 5). El paper descarta este caso por supuesto, no por evidencia.
- **Comparación con Ide & Talamas (2025)**: ambos abordan la IA en la economía del conocimiento, pero Ide-Talamas usa diferencias *de stock* de conocimiento entre trabajadores (jerarquía garicaniana), mientras este paper usa diferencias en el *modo de procesar* el conocimiento existente (PDF p. 4). Las predicciones distributivas pueden diferir.

## 7. Lecturas relacionadas

- [agrawal-gans-goldfarb_2025_bicycles-for-the-mind](../firms-market-structure/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.md) — Misma trinidad de autores, visión complementaria: IA como bicicleta para la mente, no como genio sustituto.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Si la "oferta ilimitada de genios IA" se concentra en pocas firmas, el resultado distributivo cambia.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Estimación macro conservadora del impacto de la IA, contrapunto cuantitativo a este modelo cualitativo.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — Si los rutinarios son desplazados, ¿qué queda de la clase media de cuello blanco?
- [jones_2026_ai-economic-future](../ai-models-governance/jones_2026_ai-economic-future.md) — Marco macro complementario sobre el futuro económico de la IA.
