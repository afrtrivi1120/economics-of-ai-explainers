# AI Agents for Economic Research

**Autores / Authors:** Anton Korinek
**Año / Year:** 2025
**Publicación / Venue:** NBER Working Paper 34202
**PDF:** [papers/pdfs/korinek_2025_ai-agents-econ-research.pdf](../../papers/pdfs/korinek_2025_ai-agents-econ-research.pdf)
**Fuente / Source:** https://www.nber.org/papers/w34202

## 1. Cita completa

Korinek, Anton. 2025. "AI Agents for Economic Research." NBER Working Paper 34202, September 2025. National Bureau of Economic Research. Recursos en línea: https://www.GenAIforEcon.org

## 2. Pregunta de investigación

¿Cómo pueden los economistas — incluso aquellos sin experiencia en programación — incorporar agentes de IA (sistemas autónomos basados en LLMs que planifican, usan herramientas y ejecutan tareas multipaso) en cada etapa del flujo de trabajo investigativo, desde la revisión de literatura hasta la limpieza de datos, codificación econométrica y síntesis de resultados? El paper combina un marco conceptual con una guía práctica con código funcional.

## 3. Método

No es un paper empírico sino una **guía metodológica y técnica** dirigida a investigadores. Korinek:

- **Documenta** la evolución de la IA generativa en tres paradigmas: chatbots tradicionales (LLMs estilo "Sistema 1"), modelos de razonamiento ("Sistema 2", lanzados en septiembre 2024) y chatbots agénticos (diciembre 2024) (p. 4).
- **Compara** ofertas de los principales laboratorios (OpenAI, Anthropic, Google DeepMind, xAI, Alibaba, Moonshot) usando benchmarks LMSYS, GPQA y SWE-Bench V (Tablas 2 y 3, pp. 9, 11).
- **Demuestra** con ejemplos ejecutables: gráficos de la curva de Beveridge en ChatGPT o3 (pp. 12–14), revisiones tipo Deep Research, "vibe coding" de una herramienta OLS con Claude Code (pp. 28–30), y construcción de agentes propios en Python usando la API de FRED y el framework LangGraph (pp. 32–42).
- **Supuesto clave:** los agentes son asistentes — no sustitutos — del investigador; requieren supervisión humana cercana (p. 6).

## 4. Hallazgos principales

- **Los agentes ya completan tareas multi-paso significativas.** Kwa et al. (2025) muestran que los agentes pueden realizar autónomamente tareas que toman ~50 minutos a un humano, y la duración de las tareas que pueden manejar **se ha duplicado cada siete meses desde 2019**; al ritmo actual, podrían realizar tareas de un día completo a finales de 2026 (p. 22).
- **El frontier de razonamiento se saturó rápidamente.** GPT-5 alcanza 89.4% y Grok-4 88.9% en GPQA (preguntas de doctorado); cuando el benchmark se publicó en noviembre 2023 el mejor modelo lograba sólo 39%, y los doctorandos del área puntean ~65% (p. 11). En julio 2025 dos modelos lograron medalla de oro en la Olimpiada Internacional de Matemáticas (p. 11).
- **El acceso al frontier se está volviendo función de la capacidad de pago.** Las suscripciones premium de los laboratorios cuestan ~$200/mes (un aumento de 10× respecto al año anterior); un "power user" con todas las suscripciones gastaría ~$1,000/mes, y Sam Altman ha mencionado un sistema "PhD-level" a $20,000/año (p. 16).
- **Existen alternativas open-source competitivas.** Kimi-K2 (Moonshot, julio 2025) ofrece desempeño cercano al frontier a **15 centavos por millón de tokens de entrada vs. $15 de Claude — diferencia de 100×** (p. 18). DeepSeek y Alibaba Qwen también ofrecen open-weights útiles para investigadores con recursos limitados.
- **"Vibe coding" democratiza la implementación técnica.** Korinek muestra que con ~300 líneas de Python (en gran parte generadas por lenguaje natural) se puede construir un agente Deep Research multi-agente en LangGraph; el reporte completo de su ejemplo costó ~1 centavo en tokens y 15 búsquedas Tavily (p. 43).
- **Limitaciones documentadas:** alucinaciones, "datos pseudo" generados cuando el agente no puede acceder a la fuente real (p. 15), fragilidad ante cambios menores en prompts, vulnerabilidad a prompt injection, y razonamiento económico aún débil ("a veces malaplican marcos teóricos y reproducen ideas erróneas comunes en sus datos de entrenamiento") (p. 6).

## 5. Implicaciones para política pública (Colombia / América Latina)

- **Cierre de brecha computacional.** Para departamentos de economía, bancos centrales y centros de investigación en Colombia y América Latina, los agentes ofrecen una vía concreta para superar la brecha en habilidades programáticas: el "vibe coding" permite construir herramientas econométricas funcionales sin un staff técnico dedicado (p. 5). Investigadores junior pueden ahora "lograr lo que antes requería equipos enteros" (p. 47).
- **Estrategia anti-dependencia y soberanía de datos.** Korinek recomienda **mantener flexibilidad entre proveedores en lugar de comprometerse con un único ecosistema** (p. 6). Para instituciones latinoamericanas con datos sensibles (información de mercado de bancos centrales, microdatos del DANE, registros administrativos), los modelos open-weights desplegados localmente (gpt-oss, Llama, Qwen) son la "norma de oro" en seguridad y permiten cumplir requisitos de no transferencia de datos (p. 19).
- **Costo y acceso desigual.** El precio premium de $200/mes y la posibilidad de tarifas de $20,000/año para sistemas PhD-level es una **señal de alarma para presupuestos de investigación públicos en la región**. Convenios institucionales con APIs (pago por uso) o el uso de Kimi-K2 / Qwen / DeepSeek pueden ser estrategias más viables que múltiples suscripciones individuales (p. 19).
- **Infraestructura MCP local.** Las instituciones colombianas (Banco de la República, DANE, Fedesarrollo, universidades) podrían publicar **servidores MCP (Model Context Protocol)** que expongan sus bases de datos a agentes de manera estandarizada — análogo al rol de FRED en EE.UU. (p. 44). Esto aumentaría la visibilidad y uso de datos colombianos en investigación global automatizada.
- **Capacitación de investigadores.** El paper sugiere que los economistas deben "abrazar estas herramientas ahora, no sólo para aumentar productividad sino para entender sus capacidades y limitaciones" (p. 47). Programas de doctorado y maestría en la región deberían incluir agentes de IA en su currículum metodológico.

## 6. Debates y caveats

- **Optimismo democratizador vs. concentración.** Korinek presenta una tensión interna: aunque el "vibe coding" democratiza el acceso, los benchmarks GPQA/SWE-Bench muestran que las capacidades avanzadas siguen concentradas en laboratorios bien financiados (p. 11), y "los power users que mejor saben desplegar agentes pueden beneficiarse mucho más" (p. 5). Esta lectura es coherente con el trabajo paralelo del autor con Vipra — ver `korinek-vipra_2025_concentrating-intelligence` — que enfatiza el riesgo de concentración estructural en la industria de IA.
- **Capacidad real vs. capacidad anunciada.** El paper documenta sobreconfianza explícita: el sistema Deep Research de OpenAI afirmó que "los agentes de IA están transformando rápidamente cómo los economistas hacen investigación" — Korinek mismo no está seguro de que mejoren la inferencia causal (p. 26). Esto es relevante frente a estudios empíricos como `brynjolfsson-li-raymond_2025_genai-at-work` que miden ganancias de productividad reales en tareas más limitadas.
- **Razonamiento económico vs. síntesis.** Korinek es claro: los agentes son "soberbios asistentes pero todavía no investigadores independientes" (p. 47). Esto matiza visiones más expansivas sobre automatización de la investigación científica como las que se discuten en `agrawal-gans-goldfarb_2025_research-agenda-tai` y `agrawal-gans-goldfarb_2025_bicycles-for-the-mind`.
- **Riesgos novedosos:** Korinek cita el trabajo de Gans (2025) sobre manipulación de revisores LLM mediante prompt injection (p. 47), sugiriendo que la integración masiva de agentes en flujos académicos abre vectores de gaming inéditos.

## 7. Lecturas relacionadas

- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — el otro lado de la moneda: por qué la frontera de IA tiende a concentrarse en pocos laboratorios.
- [agrawal-gans-goldfarb_2025_bicycles-for-the-mind](../firms-market-structure/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.md) — la IA como "bicicleta para la mente" del investigador, complementario al enfoque "agentes como asistentes" de Korinek.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — agenda de investigación para IA transformativa.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — evidencia empírica sobre ganancias reales de productividad con IA generativa en el lugar de trabajo.
