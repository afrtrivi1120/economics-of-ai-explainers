# Understanding Economic Behavior Using Open-ended Survey Data

**Autores / Authors:** Ingar K. Haaland, Christopher Roth, Stefanie Stantcheva, Johannes Wohlfart
**Año / Year:** 2024 (revisado diciembre 2024)
**Publicación / Venue:** NBER Working Paper No. 32421
**PDF:** [papers/pdfs/stantcheva-et-al_2024_open-ended-survey.pdf](../../papers/pdfs/stantcheva-et-al_2024_open-ended-survey.pdf)
**Fuente / Source:** https://www.nber.org/papers/w32421

## 1. Cita completa

Haaland, Ingar K., Christopher Roth, Stefanie Stantcheva, and Johannes Wohlfart. 2024. "Understanding Economic Behavior Using Open-ended Survey Data." NBER Working Paper No. 32421, May 2024 (revised December 2024). JEL C90, D83, D91.

## 2. Pregunta de investigación

¿Cómo pueden los economistas usar preguntas abiertas en encuestas — combinadas con modelos de lenguaje grandes (LLMs) — para descubrir los motivos, modelos mentales y narrativas que están detrás de comportamientos y expectativas económicas que las preguntas cerradas tradicionales no logran captar? La revisión documenta una literatura emergente y propone un manual de buenas prácticas para recolectar y analizar datos cualitativos a gran escala.

## 3. Método

- **Tipo de trabajo:** revisión metodológica (review article) que cubre publicaciones en revistas líderes de economía y working papers de NBER, CEPR y CESifo desde 1990 (PDF p. 2, Figura 1).
- **Fuentes de datos discutidas:** preguntas abiertas de un solo ítem en encuestas escritas, grabaciones de voz y entrevistas cualitativas conducidas por IA (PDF p. 3).
- **Métodos de análisis cubiertos:**
  - Codificación humana con esquemas inductivos vs. deductivos, libros de códigos y métricas de confiabilidad inter-codificadores (ICR) como kappa de Cohen, alfa de Krippendorff (PDF pp. 26–28).
  - Codificación con LLMs (GPT-4o, Claude 3 Opus) vía API, evaluada contra benchmarks humanos usando F1-scores (PDF pp. 29–30).
  - Métodos tradicionales: diccionarios, topic modeling, keyness analysis, clasificadores de ML (PDF p. 32).
- **Supuestos clave:** (i) los respondientes pueden articular verbalmente al menos una parte de su razonamiento (PDF p. 4, debate Ericsson-Simon vs. Nisbett-Wilson); (ii) los LLMs frontera replican la codificación humana con calidad aceptable cuando se valida una submuestra (PDF p. 30); (iii) la riqueza de los datos abiertos justifica los costos adicionales frente a preguntas cerradas.

## 4. Hallazgos principales

- **Crecimiento explosivo del método:** los estudios con mediciones abiertas en revistas líderes de economía pasaron de ~1–4 por año entre 1990–2017 a aproximadamente 37 en 2024 (PDF p. 2, Figura 1).
- **Aplicaciones temáticas documentadas:** razonamiento detrás de decisiones (redistribución, no participación bursátil, propiedad de armas), narrativas y modelos mentales (causas de la inflación), asignación de atención y memoria asociativa (PDF pp. 5–6).
- **Las entrevistas conducidas por IA igualan la calidad humana percibida:** sociólogos entrenados califican entrevistas hechas por IA como comparables a las que un experto humano hipotético habría logrado (PDF p. 23, citando Geiecke y Jaravel 2024). Los respondientes muestran niveles similares de selección que en encuestas estándar (PDF p. 24).
- **LLMs como codificadores escalables:** modelos frontera "proveen resultados muy similares a la codificación humana en muchos casos" (PDF p. 29) y superan a métodos basados en diccionarios, igualando enfoques de ML sin requerir datos de entrenamiento adicionales (PDF p. 32).
- **Costos y privacidad:** APIs comerciales pueden ser prohibitivamente costosas con datasets grandes; LLMs open-source como Llama permiten ejecución local con replicabilidad completa pero exigen recursos computacionales y experticia técnica (PDF p. 33).
- **Riesgos metodológicos:** "convergencia interpretativa" por iteración excesiva del ICR puede suprimir matices (PDF p. 28); grados de libertad del investigador en el diseño de esquemas de codificación amenazan la replicabilidad y exigen pre-registro y documentación detallada (PDF pp. 34–35).

## 5. Implicaciones para política pública (Colombia / América Latina)

Esta es la única pieza del corpus cuya contribución es metodológica más que sustantiva, y por eso es de alto valor para el diseño de encuestas en contextos colombianos y latinoamericanos:

- **Captar realidades del sector informal.** Las preguntas cerradas estándar de encuestas como la GEIH del DANE asumen categorías ocupacionales y de ingreso construidas para mercados formales. Preguntas abiertas analizadas con LLMs podrían revelar cómo trabajadores informales conceptualizan empleo, riesgo, ahorro y exposición a shocks — categorías que probablemente no aparecen en los formularios estructurados.
- **Encuestas a poblaciones de baja alfabetización.** Los autores destacan explícitamente que las entrevistas asistidas por IA con preguntas de seguimiento mejoran la calidad de los datos en poblaciones "menos alfabetizadas o con bajo nivel educativo" (PDF p. 23) — directamente relevante para encuestas en zonas rurales y comunidades indígenas.
- **Medición de creencias sobre IA y desplazamiento laboral.** Las encuestas estructuradas sobre adopción de IA (al estilo de Bloom et al. o Bick-Blandin-Deming) pueden complementarse con preguntas abiertas para entender cómo trabajadores colombianos perciben las amenazas y oportunidades de la IA, capturando narrativas locales que no caben en categorías importadas.
- **Diseño de política redistributiva.** Stantcheva (citada en PDF p. 6) ha usado preguntas abiertas para mapear cómo los ciudadanos piensan sobre impuestos e inflación. Aplicar este enfoque a debates colombianos sobre reforma tributaria o pensional podría informar comunicación pública y diseño de instrumentos.
- **Costos accesibles.** El uso de LLMs vía API o modelos open-source baja drásticamente la barrera de entrada para centros de investigación con presupuestos limitados, democratizando una metodología que antes requería ejércitos de asistentes de investigación.

## 6. Debates y caveats

- **Validez de los reportes verbales.** Los autores reconocen la disputa clásica entre Ericsson-Simon (1980, 1993), que defienden los reportes verbales como ventana al razonamiento, y Nisbett-Wilson (1977), que documentan introspección poco confiable (PDF p. 4). Esto importa para cualquier intento de medir actitudes hacia la IA: lo que la gente *dice* sobre el desplazamiento tecnológico puede no coincidir con sus comportamientos reveladados — una preocupación que limita extrapolaciones de política.
- **Medición vs. mecanismo: contraste con Brynjolfsson.** `brynjolfsson-li-raymond_2025_genai-at-work` mide productividad observada (resoluciones por hora) con datos administrativos. Las preguntas abiertas de Stantcheva et al. abren la "caja negra" del *por qué* —cómo agentes piensan sobre la herramienta— pero no sustituyen la medición de output. Idealmente las dos metodologías se combinan: datos administrativos para el efecto causal, datos abiertos para el mecanismo.
- **Aplicación a debates Acemoglu vs. Aghion.** El desacuerdo macro sobre la magnitud del impacto de IA (ver `acemoglu_2024_simple-macro-ai` con su ~0.66% TFP/10 años vs. `aghion-bunel_2024_ai-and-growth` con 0.8–1.3 pp/año) descansa en parte en supuestos sobre qué tareas son automatizables. Stantcheva-et-al ofrece una vía empírica para preguntar a trabajadores y gerentes directamente qué partes de su trabajo creen que la IA puede o no hacer, complementando los ejercicios de exposición à la `frey-osborne_2024_genai-reappraisal`.
- **Sesgos algorítmicos en codificación con LLM.** Los autores advierten sobre sesgos potenciales (Rozado 2024) y privacidad de datos (Dell 2024) (PDF p. 23), riesgos amplificados en contextos de vigilancia documentados por `yuchtman-et-al_2023_exporting-surveillance-state`.
- **Replicabilidad frágil.** Los grados de libertad del investigador y la dependencia de modelos comerciales que pueden ser descontinuados (PDF p. 33) son una preocupación seria — especialmente cuando los resultados informan política pública.

## 7. Lecturas relacionadas

- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — medición de productividad observada que se complementaría con preguntas abiertas sobre mecanismos.
- [korinek_2025_ai-agents-econ-research](../ai-models-governance/korinek_2025_ai-agents-econ-research.md) — uso de LLMs en el flujo de trabajo del economista, otra vertiente de la misma transformación metodológica.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — supuestos sobre tareas automatizables que los datos abiertos podrían validar empíricamente.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — narrativas sobre clase media y trabajo que admiten medición con preguntas abiertas.
