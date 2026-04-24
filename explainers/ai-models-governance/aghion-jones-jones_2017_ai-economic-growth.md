# Artificial Intelligence and Economic Growth

**Autores / Authors:** Philippe Aghion, Benjamin F. Jones, Charles I. Jones
**Año / Year:** 2017
**Publicación / Venue:** NBER Working Paper 23928 (later published as a chapter in *The Economics of Artificial Intelligence: An Agenda*, U. Chicago Press, 2019)
**PDF:** [papers/pdfs/aghion-jones-jones_2017_ai-economic-growth.pdf](../../papers/pdfs/aghion-jones-jones_2017_ai-economic-growth.pdf)
**Fuente / Source:** https://www.nber.org/papers/w23928

## 1. Cita completa

Aghion, Philippe, Benjamin F. Jones, and Charles I. Jones. 2017. "Artificial Intelligence and Economic Growth." NBER Working Paper No. 23928. National Bureau of Economic Research, Cambridge, MA.

## 2. Pregunta de investigación

¿Cómo afecta la inteligencia artificial —entendida como la última fase de un proceso de automatización de más de 200 años— al crecimiento económico de largo plazo, a la distribución del ingreso entre capital y trabajo, y a la posibilidad de "singularidades" tecnológicas? El paper busca construir el andamiaje teórico (no empírico) para responderlas (p. 1, p. 2).

## 3. Método

- **Clase de modelo:** teoría neoclásica y de crecimiento endógeno. Construye sobre Zeira (1998) y Acemoglu–Restrepo (2016), modelando la IA como automatización de tareas (p. 3, p. 5).
- **Supuestos clave:**
  - Producción CES de bienes con elasticidad de sustitución *menor que uno* (ρ < 0): las tareas son complementos, no sustitutos (eq. 5, p. 7). Esta es la pieza central que activa el "efecto Baumol".
  - Cada tarea automatizada usa una unidad de capital; cada tarea no automatizada usa una unidad de trabajo (eq. 2, p. 5; eq. 6, p. 7).
  - Una fracción β_t de tareas están automatizadas en t; los autores tratan β_t como exógeno (p. 9).
  - Cierre neoclásico estándar con tasa de inversión constante (p. 5, p. 8).
- **Estrategia analítica:** comparativa estática y simulaciones del modelo (Figuras 1–3) sin calibración a datos reales; el objetivo declarado es "dar forma a una agenda de investigación" (p. 2).

## 4. Hallazgos principales

- **El efecto Baumol domina.** Cuando la elasticidad de sustitución entre tareas es menor que uno, la economía termina restringida no por lo que la IA hace bien sino por las tareas esenciales que mejoran lentamente: "growth may be constrained not by what we do well but rather by what is essential and yet hard to improve" (Abstract, p. 1; reiterado p. 3, p. 29).
- **Crecimiento balanceado pese a automatización casi total.** En la simulación de la Figura 1, con automatización continua (una fracción θ de tareas no automatizadas se automatiza cada año), el crecimiento del PIB se estabiliza ≈ 2% anual durante 500 años, β_t → 1, y la participación del capital asintota a ~1/3 mientras el trabajo retiene ~2/3 del PIB (Figura 1, p. 12; texto p. 11).
- **La automatización es, contraintuitivamente, *labor-augmenting* y *capital-depleting*.** Con ρ < 0, automatizar equivale a una combinación de cambio técnico que aumenta el trabajo y diluye el capital (eq. 16, p. 10). Esto invierte la intuición habitual de que la automatización siempre favorece al capital.
- **Idea production y crecimiento endógeno.** Si la IA automatiza la producción de ideas (Sección 3), el factor escaso (los investigadores humanos) limita la aceleración cuando ρ < 0; pero con producción Cobb-Douglas, automatizar la producción de ideas sí puede elevar permanentemente la tasa de crecimiento (p. 18, eq. 25 p. 20).
- **Singularidades posibles, pero frágiles.** Si la IA automatiza *todas* las tareas (Ejemplo 1, p. 21–22) o si γ ≡ (σ/(1−α))·(β/(1−φ)) > 1 con producción Cobb-Douglas (Ejemplo 3, eq. 36, p. 24), el modelo genera explosiones de crecimiento "Tipo II" (ingresos infinitos en tiempo finito). Pero los autores enfatizan que estos resultados dependen de supuestos particulares y son revertidos por cuellos de botella tipo Baumol o "fishing-out" (p. 27, p. 28).
- **Cuellos de botella tres veces:** límites a la automatización completa, "search limits" (las ideas son cada vez más difíciles de encontrar; φ ≤ 0), y leyes naturales (segunda ley de la termodinámica, restricciones físicas) (p. 27–29). Moore's Law se invoca como advertencia: la computación se aceleró 10^11 desde la Segunda Guerra Mundial (p. 28, nota 16) y el crecimiento del PIB no se aceleró.

## 5. Implicaciones para política pública (Colombia / América Latina)

- **No esperar un "shock IA" automático sobre la productividad agregada.** El marco predice que la automatización sectorial puede convivir con tasas de crecimiento agregado estables, porque los sectores esenciales pero difíciles de mejorar (cuidado, educación presencial, infraestructura) absorben una creciente fracción del gasto. Para Colombia, esto sugiere que estrategias de política industrial centradas únicamente en adoptar IA en manufactura/servicios financieros tendrán efectos macro modestos a menos que se ataquen también los cuellos de botella en sectores Baumol-intensivos (salud, educación, justicia).
- **El cuello de botella es la complementariedad humana.** Si el trabajo escaso ancla el crecimiento, las políticas con mayor retorno son las que aumentan la productividad del trabajo en tareas no automatizadas: formación docente, profesionalización del cuidado, certificación de oficios. Esto coincide con el argumento de Autor sobre re-expandir empleo de clase media (ver `autor_2024_rebuild-middle-class`).
- **Distribución capital/trabajo.** El modelo predice que la participación del capital puede subir transitoriamente pero está acotada por el efecto Baumol. Para política tributaria colombiana, esto modera el alarmismo sobre una "captura masiva del capital" pero advierte que la dinámica transicional sí puede aumentar la concentración (Figura 2, p. 14).
- **Investigación y desarrollo.** Si la IA puede automatizar parte del proceso de innovación (p. 17), los retornos a inversión en I+D doméstico aumentan: una IA que multiplica la productividad de cada investigador colombiano hace más rentable mantener capacidad investigativa nacional, no menos.

## 6. Debates y caveats

- **Conservador vs. optimista.** Aghion–Jones–Jones es teórico y no estima magnitudes; en trabajo posterior, Aghion–Bunel cuantifican un impacto de 0.8–1.3 puntos porcentuales/año en crecimiento (ver `aghion-bunel_2024_ai-and-growth`), mientras que Acemoglu (2024) ofrece la estimación más conservadora —~0.66% de TFP en 10 años (ver `acemoglu_2024_simple-macro-ai`). Este paper es la *plomería teórica* sobre la cual ambos campos construyen y disputan.
- **Supuesto crítico ρ < 0.** Todo el resultado de "crecimiento balanceado pese a automatización" depende de que las tareas sean complementos brutos (p. 9, p. 10). Si ρ > 0 (sustitutos), incluso sin automatización el modelo genera crecimiento explosivo (p. 19). La elección de ρ < 0 es defendida como "el caso natural", pero es una elección, no un dato. Acemoglu–Restrepo (2018) trabaja con un marco más rico que endogeniza esta elasticidad (ver `acemoglu-restrepo_2018_ai-automation-work`).
- **β exógeno.** Los autores reconocen explícitamente que tratan la fracción de tareas automatizadas como exógena y que endogenizarla "es una dirección importante para investigación futura" (p. 9). La evidencia empírica de adopción real de GenAI (ver `brynjolfsson-li-raymond_2025_genai-at-work`) sugiere que β crece de manera muy desigual entre firmas y trabajadores.
- **Sin estructura de mercado.** El paper introduce firmas en una sección posterior pero el núcleo del argumento de crecimiento ignora poder de mercado. Korinek–Vipra (2025) muestra que las leyes de escala de IA generan concentración fuerte (ver `korinek-vipra_2025_concentrating-intelligence`), un canal ausente aquí.
- **Singularidades como ejercicio retórico.** Las cuatro "vías" hacia singularidad (Sección 4.1) son construidas para mostrar bajo qué supuestos *podrían* ocurrir; los propios autores listan tres clases de objeciones (automation limits, search limits, Baumol) que las hacen poco probables (p. 27–29).

## 7. Lecturas relacionadas

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — la versión empírica conservadora del marco de tareas; estima ~0.66% TFP/10 años.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — Aghion vuelve sobre el mismo problema con datos de Francia y obtiene cifras sustancialmente más altas (0.8–1.3 pp/año).
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — el marco hermano de tareas, con automatización endógena y creación de nuevas tareas.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — evidencia empírica de campo sobre β en una firma real (call center).
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — interpretación complementaria: si IA es complementaria al trabajo no-experto, puede re-expandir clase media.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — añade el canal de estructura de mercado que este paper omite.
