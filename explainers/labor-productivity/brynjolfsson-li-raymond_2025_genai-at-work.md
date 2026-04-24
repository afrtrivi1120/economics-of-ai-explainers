# Generative AI at Work

**Autores / Authors:** Erik Brynjolfsson, Danielle Li, Lindsey R. Raymond
**Año / Year:** 2023 (revised Nov 2023; QJE 2025)
**Publicación / Venue:** QJE 2025 / NBER Working Paper No. 31161
**PDF:** [papers/pdfs/brynjolfsson-li-raymond_2025_genai-at-work.pdf](../../papers/pdfs/brynjolfsson-li-raymond_2025_genai-at-work.pdf)
**Fuente / Source:** https://www.nber.org/papers/w31161

## 1. Cita completa

Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). *Generative AI at Work*. NBER Working Paper No. 31161 (forthcoming, *Quarterly Journal of Economics*, 2025). National Bureau of Economic Research.

## 2. Pregunta de investigación

¿Cuál es el efecto causal del despliegue de un asistente conversacional basado en IA generativa sobre la productividad, la calidad del trabajo y la experiencia laboral de los agentes de servicio al cliente? Y, sobre todo, ¿cómo se distribuyen esas ganancias entre trabajadores de distintos niveles de habilidad y experiencia? (p. 2-3)

## 3. Método

- **Datos.** Registros administrativos a nivel de chat y agente-mes de 5,179 agentes de servicio al cliente de una empresa Fortune 500 de software de procesos de negocio, principalmente subcontratada en el extranjero, durante el despliegue escalonado de un asistente basado en GPT (p. 2; PDF p. 3, p. 12).
- **Estrategia de identificación.** Diferencias en diferencias con efectos fijos de año-mes, agente y antigüedad del agente; errores estándar agrupados a nivel de agente (ec. 1, p. 13). Como contraste robusto a heterogeneidad y dinámica del tratamiento se usa el estimador de eventos ponderado por interacción de Sun y Abraham (2021), con verificaciones adicionales con Callaway–Sant'Anna, Borusyak et al. y de Chaisemartin–D'Haultfœuille (p. 13–14).
- **Variable de resultado principal.** Resoluciones por hora (RPH); también tiempo medio de manejo (AHT), chats por hora (CPH), tasa de resolución (RR) y net promoter score (NPS) (p. 12).
- **Supuestos clave.** Tendencias paralelas, ausencia de comportamiento anticipatorio y perfiles dinámicos de tratamiento comparables entre cohortes (p. 13). El AI sugiere texto en tiempo real, pero el agente decide si lo usa (p. 2).

## 4. Hallazgos principales

- El acceso al asistente eleva la productividad media (RPH) en **14 %** —0.30 chats adicionales por hora sobre una media de 2.6 (Tabla 3, Col. 2; p. 14)—, con una caída del **9 %** en el tiempo medio de manejo (3.8 minutos sobre una base de ~40 min; p. 14) y un aumento de **1.3 puntos porcentuales** en la tasa de resolución (sobre una base de 82 %, sig. al 10 %; p. 14-15).
- Los efectos son fuertemente **heterogéneos por habilidad**: los agentes del quintil más bajo del índice de habilidad pre-IA ganan **34 %** en RPH (0.29 puntos log), mientras que los del quintil superior no muestran ganancia y exhiben pequeñas caídas en tasa de resolución y satisfacción del cliente (p. 15-16).
- **Por antigüedad**, los agentes con menos de un mes en la empresa mejoran **46 %** en RPH (0.38 puntos log) frente a no tratados de la misma antigüedad; los de más de un año no muestran efecto (p. 16). Un agente tratado con 2 meses de experiencia rinde como un no tratado con más de 6 meses, evidencia de un descenso acelerado por la curva de experiencia (p. 16-17).
- El asistente **mejora la experiencia laboral**: el sentimiento del cliente sube 0.18 puntos —~½ desviación estándar (Tabla 4, Col. 1; p. 25)—, las solicitudes de hablar con un supervisor caen ~25 % (sobre base de 6 p.p.; p. 26), y la rotación entre agentes nuevos disminuye ~10 p.p., una reducción de **40 %** sobre una base de 25 % (p. 26).
- Evidencia de **aprendizaje persistente**: durante apagones del sistema, los agentes con exposición previa siguen rindiendo por encima de su línea base, lo que sugiere internalización de buenas prácticas, no mera dependencia (p. 18, 20). El análisis textual muestra **convergencia**: la similitud comunicativa entre agentes de baja y alta habilidad sube de 0.55 a 0.61 (p. 23).

## 5. Implicaciones para política pública (Colombia / América Latina)

- **Compresión de la distribución de productividad.** A diferencia de olas anteriores de TI —que tendían a complementar a los más calificados— la IA generativa parece **reducir la brecha entre trabajadores novatos y expertos** (p. 15-16, 23). Para Colombia, donde los servicios tercerizados (BPO, contact centers en Bogotá, Medellín, Manizales, Barranquilla) son una fuente importante de empleo formal joven, esto sugiere que la IA puede **acortar curvas de entrenamiento** y permitir que trabajadores con menos años de educación accedan rápidamente a niveles de desempeño antes reservados a personal experimentado.
- **Política de capacitación.** El SENA y programas de empleabilidad pueden integrar asistentes generativos como herramienta pedagógica activa, no solo como contenido. La evidencia de aprendizaje durante apagones (p. 20) implica que la exposición temprana deja capital humano residual.
- **Riesgo distributivo del lado de los puestos**, no solo de los salarios. Los autores advierten que sus datos no observan demanda agregada de trabajo: si la demanda por servicio al cliente es inelástica, la productividad podría traducirse en **menos puestos** (p. 3, p. 27). Para una economía colombiana con ~600,000 empleos en BPO/KPO, esto exige monitoreo activo de empleo sectorial y políticas activas de transición.
- **Compensación de "datos de entrenamiento".** El paper plantea que los trabajadores top no son retribuidos por las prácticas tácitas que la IA extrae de sus chats (p. 3-4, p. 27). Esto abre un debate concreto para la regulación laboral: ¿propiedad o licencia de datos generados en relaciones laborales? Una pregunta abierta para el MinTrabajo y la SIC.
- **Bienestar laboral.** La caída de rotación y la mejora del trato del cliente (p. 25-26) son resultados poco discutidos en el debate público sobre IA, pero relevantes para la formalización y la salud mental en sectores de alta presión emocional.

## 6. Debates y caveats

- **Compatibilidad con el techo macro de Acemoglu.** Acemoglu (2024) estima ganancias de TFP del orden de 0.66 % acumuladas en 10 años a partir de tareas IA-expuestas con ~14 % de mejora micro promedio (`acemoglu_2024_simple-macro-ai`). El 14 % medio de Brynjolfsson-Li-Raymond es **exactamente el orden de magnitud** que Acemoglu usa como cota razonable; este paper, en ese sentido, **no contradice** la visión conservadora de Acemoglu.
- **Tensión con Aghion-Bunel.** Aghion y Bunel (2024) reportan ganancias de 0.8–1.3 puntos porcentuales anuales de crecimiento de TFP en el escenario optimista (`aghion-bunel_2024_ai-and-growth`), un orden de magnitud por encima. Si la IA generalmente comprime la cola de baja productividad como aquí, las ganancias agregadas pueden ser mayores que lo que sugiere extrapolar el promedio.
- **Sesgo-habilidad invertido respecto a Acemoglu-Restrepo.** Acemoglu y Restrepo (2018) modelan automatización como sesgada contra trabajadores de baja calificación (`acemoglu-restrepo_2018_ai-automation-work`). Aquí la dirección se invierte: la IA generativa **iguala hacia arriba** a los menos calificados (p. 15-16), lo que apoya la hipótesis de Autor (2024) de que la IA puede recomponer la clase media (`autor_2024_rebuild-middle-class`).
- **Caveats internos del paper.** (i) Una sola firma en un sector relativamente estable; los autores advierten que los efectos pueden no generalizar a entornos con productos cambiantes (p. 27-28). (ii) No observan salarios, demanda agregada ni cambios en composición de contratación (p. 3). (iii) Los resultados de rotación son menos robustos por imposibilidad de incluir efectos fijos de agente (p. 26). (iv) Los efectos negativos pequeños sobre los top performers (p. 16) son consistentes con que la IA "distrae" o homogeneiza.
- **Concentración de poder.** El hecho de que un único modelo de OpenAI capture conocimiento tácito de miles de trabajadores (p. 3-4) refuerza la preocupación de Korinek y Vipra sobre concentración (`korinek-vipra_2025_concentrating-intelligence`).

## 7. Lecturas relacionadas

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — la cota macro conservadora con la que el 14 % de este paper es aritméticamente compatible.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — visión más optimista del crecimiento agregado vía IA.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — hipótesis de que la IA puede recomponer la clase media; este paper aporta evidencia micro consistente.
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — marco teórico sobre tareas y automatización con el que conviene contrastar el patrón de compresión observado.
- [aghion-jones-jones_2017_ai-economic-growth](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — base teórica sobre IA y crecimiento.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — quién captura las rentas del conocimiento tácito agregado por LLMs.
