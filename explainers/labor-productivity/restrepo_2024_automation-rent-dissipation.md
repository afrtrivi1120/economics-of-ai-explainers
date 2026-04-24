# Automation and Rent Dissipation: Implications for Wages, Inequality, and Productivity

**Autores / Authors:** Daron Acemoglu, Pascual Restrepo
**Año / Year:** 2024 (revisado octubre 2025)
**Publicación / Venue:** NBER Working Paper No. 32536
**PDF:** [papers/pdfs/restrepo_2024_automation-rent-dissipation.pdf](../../papers/pdfs/restrepo_2024_automation-rent-dissipation.pdf)
**Fuente / Source:** https://www.nber.org/papers/w32536

## 1. Cita completa

Acemoglu, Daron y Pascual Restrepo. 2024 (rev. 2025). "Automation and Rent Dissipation: Implications for Wages, Inequality, and Productivity." NBER Working Paper No. 32536. National Bureau of Economic Research. Disponible en https://www.nber.org/papers/w32536.

## 2. Pregunta de investigación

¿Cómo cambian los efectos de la automatización sobre salarios, desigualdad y productividad cuando el mercado laboral tiene rentas — es decir, cuando algunos puestos pagan salarios por encima del costo de oportunidad del trabajador (por sindicatos, salarios de eficiencia, regulación o licencias)? El paper introduce un mecanismo de *rent dissipation*: la automatización ataca selectivamente las tareas con mayores rentas, amplificando las pérdidas salariales y borrando parte de las ganancias de productividad esperadas.

## 3. Método

- **Datos:** BEA Integrated Industry-Level Production Accounts (49 industrias), Censo de EE.UU. de 1980 (500 grupos demográficos), O*NET (contenido rutinario de ocupaciones), CPS (salarios por percentil 1980–2016), tres proxies de automatización: penetración ajustada de robots industriales (Acemoglu y Restrepo, 2020), participación de software especializado y maquinaria dedicada en valor agregado (BLS) (PDF p. 23).
- **Estrategia de identificación:** (i) regresión de cuantiles por grupo (Chetverikov et al., 2016) sobre el cambio en el log-salario en cada percentil contra el "task displacement" del grupo (PDF p. 26); (ii) descomposición del cambio salarial promedio en componente de salario base (percentil 30) y componente de disipación de rentas (caída adicional sobre el percentil 30) (PDF p. 29); (iii) medida directa de desplazamiento desde empleos de alta renta usando proxies de rentas a nivel industria-ocupación (PDF p. 30).
- **Modelo:** Extensión del modelo de tareas de Acemoglu-Restrepo (2022). Los puestos pagan un wedge µ_gx ≥ 1 sobre el salario base, tratado como rígido (eficiencia, contratación, licencias, regulación) (PDF p. 6). Equilibrio general con efectos "ripple" entre grupos vía dos matrices: *propagation matrix* y *rent-impact matrix* (PDF p. 2).
- **Supuestos clave:** wedges fijos que no se ajustan en equilibrio; λ = 0.5 (elasticidad de sustitución entre tareas); π_i = 30%; µ_A/µ_i = 1.35 (PDF p. 23). Los wedges de monopsonio generan implicaciones similares (PDF p. 6, nota 6).

## 4. Hallazgos principales

- La automatización entre 1980 y 2016 explica el **52% del aumento de la desigualdad salarial entre grupos** en EE.UU.; **42 pp** corresponden al efecto base vía demanda laboral y **10 pp** (≈ un quinto) provienen específicamente de disipación de rentas (PDF p. 3).
- El ahorro de costos por automatización aumentó la PTF en aproximadamente **3% acumulado** entre 1980 y 2016, pero el targeting ineficiente de tareas con altas rentas **anuló entre el 60% y el 90%** de esa ganancia. La PTF agregada neta solo creció **0.3–1.3%** y el consumo agregado **0.45–1.95%** durante todo el período (PDF p. 3).
- Los grupos en el medio-bajo de la distribución salarial perdieron **15%–20%** de sus tareas a la automatización; los grupos con posgrado, casi nada (PDF p. 23).
- Un aumento de 10 pp en task displacement se asocia con una caída de **24%** en los salarios relativos del grupo (sin controles) o **20%** con controles completos (PDF p. 24–25). Esa única medida explica el **66%** de la variación de cambios salariales entre grupos demográficos desde 1980 (PDF p. 24).
- La curva de cambio salarial dentro del grupo expuesto tiene forma de **U**: caídas de 25–30% por cada 10 pp de displacement entre los percentiles 70–90 (donde se concentran los puestos de alta renta), versus 16% en los percentiles 5–40 (PDF p. 26).
- La tasa estimada de disipación de rentas (µ_A/µ_g − 1) es **37%** sin controles por diferenciales compensatorios y **28%** con controles (PDF p. 29). En promedio, la automatización desplazó trabajadores de empleos cuyos salarios excedían su costo de oportunidad en **≈35%** (PDF p. 2).

## 5. Implicaciones para política pública (Colombia / América Latina)

- **No todo "ahorro de costos" se traduce en ganancia social.** En economías con mercados laborales segmentados — formal/informal, sindicalizados/no sindicalizados, con licencias o salarios mínimos vinculantes — la automatización puede destruir rentas que cumplían función redistributiva sin generar la productividad agregada prometida. Para Colombia, donde el sector formal urbano concentra rentas (vía contratos, sindicatos sectoriales, regulación profesional) y coexiste con un 55–60% de informalidad, la métrica relevante para evaluar adopción de IA y robotización debe incluir el costo de reasignación, no solo la productividad técnica.
- **Diseño de políticas activas de empleo:** los trabajadores desplazados de puestos de alta renta no se reubican a puestos equivalentes; bajan en la distribución. Esto justifica programas robustos de seguro de desempleo, recapacitación dirigida y protección de ingresos durante la transición — más que subsidios a la adopción tecnológica per se.
- **Política tributaria sobre automatización:** el resultado de que la disipación de rentas borra 60–90% de las ganancias de PTF refuerza el argumento de Acemoglu (2024) y otros para revisar el tratamiento fiscal asimétrico que actualmente favorece capital sobre trabajo (depreciación acelerada, deducciones por inversión). Para América Latina, donde el código tributario suele privilegiar bienes de capital importados, el hallazgo sugiere recalibración.
- **Regulación profesional y licencias:** dado que los wedges generados por licencias son una fuente identificada de rentas, las reformas a barreras de entrada profesional deben evaluar el efecto de equilibrio sobre incentivos a automatizar, no solo el efecto de competencia estática.

## 6. Debates y caveats

- **Refinamiento del marco Acemoglu-Restrepo (2022).** El paper extiende explícitamente el modelo de tareas previo (ver `acemoglu-restrepo_2018_ai-automation-work`) introduciendo wedges µ_gx ≥ 1. La novedad teórica clave: la automatización no es neutral respecto a qué tareas elige; selecciona aquellas donde el salario excede el costo de oportunidad, lo que rompe la equivalencia entre ahorro privado de costos y ahorro social.
- **Tensión con visiones macro-optimistas.** Los autores estiman ganancias agregadas netas de PTF de apenas 0.3–1.3% en 36 años — un orden de magnitud inferior a las proyecciones de `aghion-bunel_2024_ai-and-growth` (0.8–1.3 pp anuales) y aún por debajo del cálculo conservador de `acemoglu_2024_simple-macro-ai` (~0.66% en 10 años). La diferencia: aquí la ineficiencia de targeting actúa como un "impuesto" sobre las ganancias de productividad ausente en modelos de crecimiento balanceado como `aghion-jones-jones_2017_ai-economic-growth`.
- **Dependencia de wedges fijos.** El supuesto crítico es que µ_gx no se ajusta en equilibrio. Si los sindicatos renegocian o las regulaciones se relajan ante automatización, la disipación se mitiga. Los autores discuten micro-fundamentos donde esto no ocurre (PDF p. 6, nota 7), pero el resultado cuantitativo es sensible.
- **Compatible con la lectura institucional de Autor.** Coincide con `autor_2024_rebuild-middle-class` en que la pérdida de empleos de clase media no es solo un fenómeno de oferta-demanda de habilidades sino de erosión de rentas. Diverge de explicaciones puramente skill-biased (Katz-Murphy, 1992) que el paper cita como insuficientes (PDF p. 4).
- **Limitación geográfica.** Los wedges están calibrados con datos de EE.UU. (1980); su mapeo a economías con instituciones laborales distintas (informalidad, salario mínimo más vinculante) requiere recalibración antes de transferir las magnitudes.

## 7. Lecturas relacionadas

- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Marco original de tareas que este paper extiende incorporando rentas.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Estimación macro conservadora (≈0.66% PTF/10 años) consistente con la lectura escéptica aquí.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — Visión más optimista del crecimiento que este paper implícitamente cuestiona.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — Lectura institucional/política de la erosión de la clase media compatible con el mecanismo de rentas.
- [autor_2022_labor-market-impacts-tech](../labor-productivity/autor_2022_labor-market-impacts-tech.md) — Evidencia empírica complementaria sobre polarización y desplazamiento por tecnología.
