# Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence

**Autores / Authors:** Anton Korinek, Jai Vipra
**Año / Year:** 2024 (NBER WP, forthcoming *Economic Policy* 2025)
**Publicación / Venue:** NBER Working Paper No. 33139
**PDF:** [papers/pdfs/korinek-vipra_2025_concentrating-intelligence.pdf](../../papers/pdfs/korinek-vipra_2025_concentrating-intelligence.pdf)
**Fuente / Source:** https://www.nber.org/papers/w33139

## 1. Cita completa

Korinek, Anton, and Jai Vipra. 2024. "Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence." NBER Working Paper No. 33139. National Bureau of Economic Research. Forthcoming, *Economic Policy* 2025.

## 2. Pregunta de investigación

¿La estructura del mercado de los modelos de fundación (foundation models) — particularmente los grandes modelos de lenguaje (LLMs) — se está moviendo hacia la concentración monopolística, y qué herramientas de política de competencia pueden usar los reguladores para mantener un panorama competitivo? Los autores examinan los rasgos tecnológicos (escalas de costo, leyes de escalamiento, integración vertical) que podrían "tippear" (volcar) el mercado hacia uno o pocos jugadores dominantes.

## 3. Método

- **Enfoque:** análisis económico-institucional descriptivo (no econométrico). Combina:
  - Datos de mercado y benchmarks (tabla LMSYS, valuaciones, cuotas de mercado al cierre de 2023/2024).
  - Análisis de la estructura de costos de los foundation models (pre-entrenamiento, fine-tuning, inferencia).
  - Revisión de marcos regulatorios actuales (FTC, DoJ, CMA, EU AI Act, Digital Markets Act).
- **Marco conceptual clave:** economías de escala y de alcance derivadas de altos costos fijos + bajos costos variables; "leyes de escalamiento" (Kaplan et al. 2020; Hoffmann et al. 2022) que predicen que el desempeño crece con el cómputo invertido.
- **Supuestos:** los avances de capacidad seguirán correlacionados con el gasto en cómputo durante 3–5 años más (p. 15); los retornos económicos a la IA serán suficientes para justificar la inversión.

## 4. Hallazgos principales

- **Costos de pre-entrenamiento explosivos:** Epoch (2024) estima que entrenar Gemini Ultra en 2023 costó USD 130 millones (PDF p. 13). El cómputo desplegado en modelos de frontera ha crecido 4.1× por año durante los últimos 15 años (PDF p. 14), y el gasto en cómputo 3.09× por año (PDF p. 14, n. 6).
- **Concentración aguas arriba (chips):** Nvidia controlaba aproximadamente 92% del mercado de GPUs según Fernandez et al. (2023) (Figure 3, PDF p. 11), y un reporte de Wells Fargo estimó 98% del mercado de GPUs para data center en febrero 2024 (PDF p. 11).
- **Cuotas de mercado iniciales muy concentradas:** a fines de 2023, OpenAI (vía GPT-4) capturaba 39% del mercado de IA generativa y Microsoft (también vía GPT-4) 30% — juntos 69% (Figure 1, PDF p. 9). Google DeepMind quedaba en segundo lugar lejano con 7%.
- **Pero competencia feroz en el frontier:** al 4 de noviembre de 2024 había al menos 16 laboratorios con modelos comparables al GPT-4 original (PDF p. 3), y los cuatro líderes (OpenAI, Google DeepMind, xAI, Anthropic) están agrupados dentro de 54 puntos LMSYS — ChatGPT-4o tiene solo 55.3% de probabilidad de vencer a Gemini 1.5 Pro 002 y 57.7% contra Claude 3.5 Sonnet (PDF p. 5). Esto sugiere "competencia tipo Bertrand" con precios cerca de costos variables (PDF p. 6).
- **Talento académico drenado a la industria:** Henshall (2024) reporta que la proporción de Ph.D.s en IA que van a la industria pasó de 21% en 2004 a 73% en 2022 (PDF p. 17), encareciendo el "pipeline" de investigadores y profundizando ventajas de incumbentes.
- **Riesgos de tipping y bucles de retroalimentación:** los autores identifican un mecanismo nuevo —"intelligence feedback loop"— por el cual el laboratorio líder usa sus propios modelos internos para acelerar la siguiente versión, lo que en el límite podría producir una "explosión de inteligencia" (Good 1965) y "first-mover advantages" auto-reforzantes (PDF p. 19).
- **Integración vertical preocupante:** OpenAI ya exigió cláusulas de exclusividad a inversionistas (incluida Nvidia) en su ronda de octubre 2024 (PDF p. 10); Microsoft "absorbió" a Inflection AI vía un acuerdo de licencia de USD 650 millones que evitó la revisión antimonopolio (PDF p. 10). Microsoft invirtió ~USD 14 mil millones en OpenAI (PDF p. 7); OpenAI fue valorada en USD 157 mil millones en octubre 2024 (Figure 2, PDF p. 9).

## 5. Implicaciones para política pública (Colombia / América Latina)

Para Colombia y la región andina, este artículo es de lectura obligada porque enmarca la IA como **infraestructura crítica con tendencia natural al monopolio global**, no como un mercado competitivo más:

1. **Soberanía de cómputo limitada por diseño:** Colombia no tiene ni tendrá capacidad de competir en la frontera del entrenamiento de LLMs (los costos de entrenamiento se proyectan en miles de millones de USD para 2027 según Cottier et al. 2024, citado en bibliografía PDF p. 27). La estrategia nacional de IA debe asumir que **será consumidora, no productora**, de modelos de frontera, y enfocarse en (a) acceso negociado a APIs en condiciones no discriminatorias, (b) capacidad de fine-tuning con datos colombianos, y (c) talento local para evaluar y adaptar modelos.
2. **Política de competencia preventiva:** la SIC (Superintendencia de Industria y Comercio) debería incorporar lecciones del DMA europeo y del análisis FTC/CMA citado por los autores (PDF p. 11–12). Específicamente: vigilar adquisiciones "encubiertas" tipo Microsoft–Inflection, contratos exclusivos cloud–LLM, y privilegios de acceso temprano que distorsionan mercados downstream.
3. **Datos como activo estratégico:** el artículo destaca que el 79% de sitios de noticias de EE.UU. bloquearon los crawlers de OpenAI (PDF p. 16). Colombia podría coordinar políticas de data sharing público (datos de salud, educación, judiciales anonimizados) para reducir la dependencia de modelos entrenados solo con corpus en inglés y para fortalecer la posición negociadora frente a proveedores extranjeros.
4. **Riesgo de "intelligence divide":** los autores advierten que la UE enfrenta un riesgo de "intelligence divide" al carecer de un laboratorio frontera propio (PDF p. 24). Colombia y América Latina enfrentan una versión más severa: si la concentración global se consolida, el acceso, los precios y los términos de uso de los modelos quedarán determinados por reguladores en EE.UU., UE y China.

## 6. Debates y caveats

- **Optimistas vs. pesimistas sobre la magnitud:** los autores citan explícitamente la estimación conservadora de Acemoglu (2024) de un efecto de crecimiento de **0.07% anual** sobre la próxima década — bajo ese escenario, dicen, "the market concentration implications will be a footnote in economic history" (PDF p. 4). Korinek y Vipra están más cerca del campo optimista (Hatzius et al. 2023; JP Morgan 2024 que proyectan que la IA podría sustentar 7–10% del PIB global en una década, PDF p. 4). Compárese con `acemoglu_2024_simple-macro-ai` (estimación conservadora de TFP) y `aghion-bunel_2024_ai-and-growth` (~0.8–1.3pp/año).
- **¿Tipping inevitable?** El análisis subraya que en noviembre 2024 había competencia feroz, no monopolio. Joshua Gans (2024, citado en PDF p. 19) argumenta que los data feedback loops no garantizan dominancia si los retornos a datos adicionales decrecen rápido. Los autores reconocen esta tensión pero apuestan a que los costos crecientes terminarán reduciendo el número de jugadores viables.
- **Competencia vs. seguridad:** los autores señalan honestamente un trade-off ético: hacer el mercado más competitivo (vía open-source) puede colisionar con regular la seguridad de la IA (PDF p. 24). Esto contrasta con visiones más maximalistas pro-open-source.
- **Limitaciones empíricas:** el artículo es descriptivo y prospectivo, no causal. No estima elasticidades, no testea hipótesis, y depende fuertemente de un snapshot de noviembre 2024 que ya envejece rápidamente.

## 7. Lecturas relacionadas

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Estimación conservadora de impacto macro que, si se cumple, vuelve secundaria la preocupación por concentración.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — Visión más optimista del crecimiento por IA; eleva el premio del mercado y refuerza la urgencia de política de competencia.
- [aghion-jones-jones_2017_ai-economic-growth](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — Marco teórico sobre cuellos de botella e ideas que se vuelven escasas — relevante para el "intelligence feedback loop".
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — Evidencia microeconómica de que los LLMs sí generan productividad real, justificando la inversión que alimenta la concentración.
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Marco de tareas y automatización que complementa la pregunta de quién captura las rentas.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — Sobre cómo la IA podría redistribuir poder de mercado en el trabajo, dependiente de la estructura del mercado upstream que Korinek-Vipra describen.
