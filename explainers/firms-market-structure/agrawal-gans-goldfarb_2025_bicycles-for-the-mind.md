# The Economics of Bicycles for the Mind

**Autores / Authors:** Ajay K. Agrawal, Joshua S. Gans, Avi Goldfarb
**Año / Year:** 2025
**Publicación / Venue:** NBER Working Paper No. 34034 (July 2025)
**PDF:** [papers/pdfs/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.pdf](../../papers/pdfs/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.pdf)
**Fuente / Source:** https://www.nber.org/papers/w34034

## 1. Cita completa

Agrawal, A. K., Gans, J. S., & Goldfarb, A. (2025). *The Economics of Bicycles for the Mind*. NBER Working Paper No. 34034. National Bureau of Economic Research.

## 2. Pregunta de investigación

¿Cómo deberíamos modelar formalmente las computadoras y la IA como "herramientas cognitivas" — bicicletas para la mente, en la metáfora de Steve Jobs — y qué implica ese marco para productividad, desigualdad, automatización y diseño organizacional? El paper construye un modelo unificador que explica por qué las computadoras parecen haber aumentado la desigualdad mientras que la IA generativa, al menos hasta ahora, parece reducirla dentro de las firmas adoptantes (p. 2).

## 3. Método

- **Modelo teórico**, no empírico. No hay datos primarios; el paper sintetiza la literatura empírica existente sobre computadoras e IA.
- Un agente realiza **mejora iterativa de tareas**. En cada periodo, con probabilidad γ ("opportunity judgment") identifica una oportunidad de mejora; al implementarla, ejerce esfuerzo *e* con costo *c(e)* y probabilidad de éxito *p(se)*, donde *s* es la habilidad de implementación (p. 5–6).
- Una herramienta cognitiva, parametrizada por θ, **sustituye el esfuerzo de implementación** y **complementa el opportunity judgment** (la capacidad de ver qué mejorar). El "payoff judgment" α — saber qué acción tomar dado un diagnóstico — solo es complementario bajo condiciones específicas (p. 13, Definición 1).
- Supuestos clave: *p(·)* cóncava (rendimientos decrecientes al esfuerzo), *c(·)* convexa, y la herramienta reduce la razón beneficio marginal/costo marginal del esfuerzo (ecuación 5, p. 7).
- Extensiones: desigualdad salarial con habilidades heterogéneas (sección 4), automatización vs. colaboración humano-herramienta (sección 5), y producción en equipos con especialistas en juicio (sección 6).

## 4. Hallazgos principales

- **Las herramientas cognitivas reducen el esfuerzo humano pero aumentan el output neto** (Proposición 1, p. 14). El trabajador hace menos pero produce más — la esencia de la "bicicleta para la mente".
- **Desigualdad en forma de U** respecto a la calidad de la herramienta θ (Proposición 3, p. 18). Inicialmente, las herramientas favorecen a los trabajadores de baja habilidad ("inverse skill bias", el término θ/s), reduciendo la varianza salarial; eventualmente, la amplificación del juicio (γ₀, α) revierte el patrón y la desigualdad vuelve a crecer (p. 19).
- **Esto reconcilia dos literaturas**: la evidencia de que las computadoras aumentaron la desigualdad (Autor et al. 2006; Acemoglu-Restrepo 2018) refleja la fase larga de amplificación; la evidencia de que la IA generativa la reduce dentro de la firma (Brynjolfsson et al. 2025; Cui et al. 2025; Dell'Acqua et al. 2023) corresponde a la fase inicial de inverse skill bias (p. 21).
- **La automatización completa enfrenta tres "penalidades" multiplicativas** sobre la colaboración humano-herramienta: penalidad de identificación de oportunidades (ρ_γ < 1), de ajuste dinámico (Φ(ρ_γ) < 1), y de payoff judgment (ρ_α < 1) (Proposición 4, p. 25).
- **Paradoja de la mejora de la herramienta**: a medida que las herramientas cognitivas mejoran, la automatización completa se vuelve *más difícil* de justificar, no más fácil (p. 26). Esto explica por qué la automatización plena de tareas complejas (diagnóstico médico, planificación estratégica) ha sido escurridiza incluso con avances en IA (p. 26).
- **En equipos**, mejores herramientas desplazan el control de la implementación desde el especialista en habilidades de implementación hacia el especialista en juicio — pero "comunication tax" complica la asignación óptima (Proposición 5, p. 28; sección 6.3, p. 29).

## 5. Implicaciones para política pública (Colombia / América Latina)

- **Apuesta por el complemento, no por la sustitución.** El marco predice que la IA generativa, en su fase actual, está cerrando brechas de productividad dentro de las firmas — lo que es una oportunidad para que trabajadores colombianos sin credenciales de élite (analistas junior, médicos rurales, docentes, abogados de pequeñas firmas) accedan a tareas hoy reservadas para expertos. Esto refuerza la "let non-elites do expert tasks" framing de Autor.
- **Diseñar autoridad, no solo entregar herramientas.** El resultado clave del ejemplo médico (p. 11) — "la IA debe priorizarse para médicos que tienen la autoridad y conocimiento para actuar" — implica que en Colombia la regulación de prescripción, alcance profesional y delegación de funciones (Ley 100, scope-of-practice del MinSalud) determina cuánto valor genera la IA. Una IA diagnóstica de clase mundial no genera valor si el técnico que la opera no puede prescribir.
- **No esperar automatización plena.** Para el sector público colombiano que evalúa reemplazar trabajadores con IA, el modelo advierte: la rigidez del juicio pre-especificado hace que la automatización total sea costosa donde el contexto varía (atención al ciudadano, justicia administrativa, salud). El camino dominante es híbrido.
- **Vigilar la transición desigualdad-en-U.** Si Colombia adopta IA generativa hoy y captura la fase de inverse skill bias, podría reducir brechas dentro de firmas — pero el modelo predice que con herramientas más maduras, el "opportunity judgment" (creatividad, definición de problemas) volverá a ser premio, lo que exige inversión paralela en educación de orden superior.

## 6. Debates y caveats

- **Es un modelo, no evidencia nueva.** Las magnitudes (cuán pronunciada es la U, cuándo ocurre el punto de inflexión θ*) dependen de varianzas no observadas en habilidades vs. juicio (p. 18, ecuación 30). El paper no cuantifica nada empíricamente.
- **Optimismo selectivo sobre IA generativa.** Los autores se apoyan en Brynjolfsson-Li-Raymond y Cui et al. para sostener que la IA reduce desigualdad intra-firma — ver `brynjolfsson-li-raymond_2025_genai-at-work`. Pero reconocen excepciones: Otis et al. (2023) sobre PYMES en Kenia muestra que las firmas de menor desempeño *no* se benefician (p. 22). Para Colombia/AL, este caveat es central: si hay un piso mínimo de capital humano para capturar valor de la IA, el inverse skill bias no se materializa para los más pobres.
- **Diverge del pesimismo macro.** El marco trata la IA principalmente como complemento productivo. Esto contrasta con el cálculo conservador de Acemoglu (~0.66% de TFP en 10 años) — ver `acemoglu_2024_simple-macro-ai` — y se acerca más a la visión optimista de Aghion-Bunel (`aghion-bunel_2024_ai-and-growth`). El paper no resuelve la disputa macro; solo provee microfundamentos del lado del agente.
- **Equipos y autoridad subexplorados empíricamente.** La sección de equipos (p. 26–29) es teóricamente novedosa pero no contrastada; los resultados sobre "comunication tax" y asignación de derechos de decisión son hipótesis para investigación futura.

## 7. Lecturas relacionadas

- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — la tesis "let non-elites do expert tasks" que el paper formaliza microeconómicamente.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — evidencia empírica de inverse skill bias en call centers; el caso paradigmático que el modelo busca explicar.
- [johnson_2024_ricardo-thompson-ai](../labor-productivity/johnson_2024_ricardo-thompson-ai.md) — distinción complementariedad vs. sustitución que ancla la sección 5 sobre automatización.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — agenda de investigación de los mismos autores; este paper es una pieza del programa.
- [gans_2025_genius-on-demand](../firms-market-structure/gans_2025_genius-on-demand.md) — Gans solo, sobre cómo la IA democratiza el acceso al "genio" experto.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — contrapunto macro pesimista al optimismo micro de este paper.
