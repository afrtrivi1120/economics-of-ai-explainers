# Exporting the Surveillance State via Trade in AI

**Autores / Authors:** Martin Beraja, Andrew Kao, David Y. Yang, Noam Yuchtman
**Año / Year:** 2023
**Publicación / Venue:** NBER Working Paper No. 31676
**PDF:** [papers/pdfs/yuchtman-et-al_2023_exporting-surveillance-state.pdf](../../papers/pdfs/yuchtman-et-al_2023_exporting-surveillance-state.pdf)
**Fuente / Source:** https://www.nber.org/papers/w31676

## 1. Cita completa

Beraja, Martin; Kao, Andrew; Yang, David Y.; Yuchtman, Noam. *Exporting the Surveillance State via Trade in AI.* NBER Working Paper No. 31676, September 2023.

## 2. Pregunta de investigación

¿Está China exportando, junto con su tecnología de inteligencia artificial de reconocimiento facial, también las instituciones del Estado vigilante? Más concretamente: ¿quiénes compran esa tecnología, cuándo la compran, y qué pasa con la calidad de las instituciones políticas de los países importadores? El paper desafía la creencia de que la integración comercial necesariamente difunde instituciones liberales (p. 1, p. 25).

## 3. Método

- **Datos:** Construcción de una base novedosa de 1.636 acuerdos comerciales globales de IA de reconocimiento facial entre 2008 y 2021, a partir del reporte de la Carnegie Endowment (Feldstein, 2019), web-scraping de 15.351 fuentes adicionales, validación con NLP (Stanza/NER) y verificación humana, complementada con la base Capital IQ (2.878 firmas) (pp. 5–6). Cubre 36 países exportadores y 136 importadores.
- **Comparadores:** Comercio en otras 9 tecnologías de frontera (drones, robótica, genómica, etc.) desde UN Comtrade (pp. 6–7), datos de Polity IV (regímenes), NELDA (calidad electoral), GDELT (eventos de protesta — 18.4 millones de eventos), Banco Mundial, AidData, China Global Investment Tracker y SIPRI.
- **Identificación:** Modelos de probabilidad lineal a nivel diada país-país-sector-año. La estrategia clave es un *triple-difference* (China × IA × régimen autocrático), descontando comercio en otras tecnologías de frontera para neutralizar factores no observados de comercio bilateral (p. 10, ec. 1; p. 14, ec. 2). Para el efecto de protestas usan un event-study con leads/lags y efectos fijos de país e año (p. 17, ec. 3). Para erosión institucional, una regresión long-difference 2005–07 vs. 2019–21 (p. 20, ec. 4).
- **Supuestos clave:** Que comercio en otras tecnologías de frontera capta los confounders generales bilaterales; que ausencia de pre-tendencias respalda interpretación causal del shock de protesta sobre importaciones (p. 17).

## 4. Hallazgos principales

- **China domina las exportaciones de IA de vigilancia.** Entre 2008–2021 China registra 250 acuerdos de exportación de reconocimiento facial (vs. 215 EE.UU.), exporta a 83 países (vs. 57 EE.UU.) (pp. 6, 10). En "ciudades inteligentes" China lidera con 158 acuerdos (vs. Alemania, 124) (p. 6).
- **Ventaja comparativa específica a IA.** El coeficiente de interacción China×IA es **+47.4 pp** en la probabilidad de comercio diádico, robusto a controles de PIB, distancia, lenguaje, frontera y colonia compartida (p. 10, Tabla 2). En el resto de tecnologías de frontera China no muestra esta dominancia (Figura 2, p. 13).
- **Sesgo autocrático en la demanda.** El 44% de las exportaciones chinas de IA va a autocracias y democracias débiles, vs. solo 24% de las exportaciones de EE.UU. (pp. 2–3). El triple-difference implica un **+22% de aumento en la probabilidad** de que un autócrata o democracia débil importe IA china respecto a otras tecnologías de frontera (p. 14, Tabla 3 Panel A). El sesgo no aparece en imports desde EE.UU. (p. 15).
- **Las importaciones se disparan en años de protesta interna.** En autocracias y democracias débiles, un shock de protestas eleva contemporáneamente las importaciones de IA china (coef. 0.073–0.097, significativo al 5%) sin pre-tendencias detectables (p. 19, Tabla 4). El patrón es exclusivo de IA — no aparece en otras 14 tecnologías de frontera (Figura 5, p. 22) — ni en democracias maduras (Figura 4, p. 21).
- **Erosión institucional concomitante.** Importar IA china durante años de alta agitación se asocia con un descenso significativo del índice NELDA de calidad electoral (coef. −0.556 a −0.704, p. 23, Tabla 5 Panel A). El mismo patrón no aparece en democracias maduras importadoras de la misma tecnología.
- **Atrincheramiento del régimen.** Países que importan IA china por encima de la mediana durante alta agitación tienen solo **4.7% (1 en 21) de probabilidad** de transitar a democracia consolidada, frente a **21.7% (5 en 23)** entre quienes importan poco (p. 25).

## 5. Implicaciones para política pública (Colombia / América Latina)

América Latina es objetivo activo del despliegue de IA china: el paper cita el caso de Brasil, donde Israel exportó "Digital Intelligence" para la Policía Federal en 2020 (p. 6), pero el patrón general — Huawei en Laos, Uganda, Zambia, Myanmar (pp. 1–2) — refleja un mercado que también está penetrando ciudades latinoamericanas vía proyectos de "Safe City" y "Smart City". Para Colombia, los hallazgos generan al menos cuatro implicaciones concretas:

1. **Due-diligence institucional para contratos de infraestructura urbana de IA.** El paper muestra que el riesgo no es la tecnología en abstracto sino la combinación tecnología × régimen × contexto político: importar IA china durante una crisis interna correlaciona con erosión electoral (p. 23). Colombia debería exigir evaluaciones de impacto en derechos antes de procurar reconocimiento facial municipal o policial, especialmente en contextos electorales o de protesta social.
2. **Transparencia en compras subnacionales.** Muchas compras se hacen vía intermediarios B2B (p. 5, nota 10) y municipios. Sin un registro nacional consolidado de contratos de IA de vigilancia, el país pierde capacidad de auditoría legislativa.
3. **Regulación de externalidades transfronterizas.** Los autores proponen modelar la regulación de IA de vigilancia sobre regímenes existentes para bienes de doble uso o con externalidades globales (p. 26). Colombia, como miembro de la OCDE, podría liderar una agenda regional latinoamericana en estándares de exportación/importación de IA con riesgo a derechos.
4. **No es solo un debate "China vs. EE.UU."** El paper documenta que cuando autocracias y democracias débiles importan IA *de EE.UU.* tras protestas, también se observa erosión institucional (p. 24). El problema es la tecnología en manos de demandantes con motivaciones represivas, no el origen geopolítico del proveedor.

## 6. Debates y caveats

- **Causalidad imperfecta.** Los autores son explícitos: la asociación entre importaciones de IA china en años de protesta y caída de calidad electoral *no* se interpreta como efecto causal directo de la IA sobre las instituciones. Es más probable que ambas sean co-resultados de un esfuerzo deliberado del régimen por consolidar control (p. 22). Esta cautela contrasta con la lectura periodística más alarmista de "China exportando autoritarismo".
- **Muestra pequeña en el resultado de cambio de régimen.** El estadístico 4.7% vs. 21.7% (p. 25) se basa en 21 y 23 países respectivamente — sugestivo, no concluyente.
- **No diferencia oferta vs. demanda.** Los autores reconocen que no pueden testear directamente si China subsidia exportaciones a autocracias como política exterior, ni separarlo de auto-bans estadounidenses (IBM, Microsoft, Google después de 2018) (p. 16). El sesgo es robusto a excluir el período post-2018.
- **Tensión con narrativas optimistas sobre IA y crecimiento.** Mientras `aghion-bunel_2024_ai-and-growth` y `acemoglu_2024_simple-macro-ai` debaten la magnitud de las ganancias de productividad de la IA, este paper muestra que los costos institucionales globales pueden no ser internalizados por esos modelos macro. Una contabilidad de bienestar de la IA debería incluir externalidades sobre derechos políticos.
- **Complemento con `korinek-vipra_2025_concentrating-intelligence`.** Korinek y Vipra se preocupan por concentración de poder *económico* vía IA; este paper documenta concentración de poder *político-coercitivo* — son dos caras del mismo problema de gobernanza.

## 7. Lecturas relacionadas

- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Concentración de capacidades de IA y riesgos de poder; complemento natural sobre gobernanza.
- [jones_2026_ai-economic-future](../ai-models-governance/jones_2026_ai-economic-future.md) — Marco macro sobre futuro económico de la IA, donde encajar las externalidades políticas documentadas aquí.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Discute usos "malos" de la IA (incluyendo vigilancia) que no entran en estimaciones convencionales de TFP.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — Agenda de investigación sobre IA transformativa que requiere incorporar la dimensión geopolítica documentada.
