"""Páginas adicionales: Sobre mí (trayectoria y certificados), Notas (artículos) y la hoja de vida en PDF."""
from pathlib import Path

ROOT = Path(__file__).parent

TIMELINE = [
    ("2024", "Empiezo Estadística en la Universidad de Antioquia",
     "Pregrado en Estadística, con grado esperado en 2029. Allí está la base de todo lo demás: probabilidad, inferencia, "
     "modelos y la costumbre de preguntar cuánta incertidumbre hay detrás de un número.", "cientifico"),
    ("Nov. 2024", "Diseñador de formación en IA para empresas",
     "Diseño contenidos para que equipos de empresa, técnicos y no técnicos, usen IA generativa en su trabajo diario. "
     "Construí un curso completo sobre el uso de Claude en procesos de negocio (casos de uso, buenas prácticas de prompts "
     "y flujos de trabajo), con materiales de presentación revisados con un sistema de diseño. También traduje al español "
     "guías técnicas de certificación en IA.", "ia"),
    ("Nov. 2025", "Consultor independiente en análisis de datos y documentación",
     "Apoyo a clientes de distintos sectores con análisis de datos e informes: limpieza y análisis en Python (pandas, SciPy) "
     "y Excel con pruebas estadísticas y gráficos, documentos corporativos en Word y Excel, traducción y digitalización con OCR, "
     "y uso de IA para acelerar la producción con control de calidad.", "analista"),
    ("Ago.–oct. 2026", "90 días, 82 publicaciones, seis proyectos",
     "Seguí un canal educativo de IA y anoté cada publicación. De esas notas salieron los seis proyectos de este portafolio, "
     "todos con código, datos y tests públicos.", "amber"),
    ("2029", "Grado en Estadística (esperado)", "", "muted"),
]

SKILLS = [
    ("Estadística", "cientifico", ["Inferencia y pruebas de hipótesis", "Regresión y modelos lineales", "Calibración de probabilidades",
                                   "PSI, KS y chi-cuadrado", "Variables de confusión", "Diseño de métricas de negocio"]),
    ("Programación", "amber", ["Python", "pandas", "scikit-learn", "SciPy", "matplotlib y Plotly", "pytest"]),
    ("Bases de datos", "analista", ["SQL", "DuckDB", "CTE y funciones de ventana", "Modelado en capas", "Reglas de calidad de datos", "Excel"]),
    ("IA generativa", "ia", ["Claude API y tool use", "RAG y búsqueda híbrida", "Evaluación de LLMs", "Diseño de prompts",
                             "Costo y latencia", "Formación de equipos"]),
]

SOFTWARE = [
    ("Estadística", "cientifico", ["R y RStudio"]),
    ("Datos y BI", "analista", ["Excel avanzado", "Power BI", "Tableau", "Google Sheets y Looker Studio"]),
    ("Desarrollo", "amber", ["VS Code", "Cursor", "PyCharm", "Jupyter y Google Colab", "Anaconda", "Git y GitHub", "PostgreSQL y MySQL"]),
    ("IA", "ia", ["Claude y Claude Code", "ChatGPT y Copilot", "Gemini y NotebookLM", "Perplexity", "OpenAI API y Gemini API",
                  "LangChain y LlamaIndex", "Ollama y LM Studio", "Midjourney"]),
    ("Productividad", "muted", ["Word y PowerPoint", "Notion y Google Workspace", "n8n, Zapier y Make", "Microsoft Teams y Slack"]),
]

LANGS = [("Español", "Nativo"), ("Inglés", "Intermedio (B1–B2)"), ("Portugués", "Intermedio"),
         ("Alemán", "Básico"), ("Italiano", "Básico")]

# Para agregar un certificado: ("Nombre", "Entidad", "Año", "enlace de verificación o None")
CERTS = []

NOTES = [
    {
        "slug": "nota-90-dias-canal-ia",
        "title": "Seguí un canal de IA durante 90 días y medí qué me estaba enseñando",
        "date": "Noviembre de 2026", "role": "analista", "project": "my-data-diary-analytics",
        "summary": "Pasé de leer publicaciones a contarlas. El canal empezó enseñando a construir y terminó preparando para buscar empleo.",
        "body": [
            ("p", "Entre agosto y octubre de 2026 seguí un canal educativo de IA y, cada mes, escribí un informe en Word con lo que se había publicado. "
                  "Al final tenía tres documentos y una sensación: el contenido había cambiado. Quise saber si era cierto o solo una impresión."),
            ("h", "Convertir informes en datos"),
            ("p", "Lo primero fue sacar las tablas de los tres informes a un solo dataset. Quedaron 82 publicaciones en 72 días activos. "
                  "Limpié fechas, detecté reenvíos y separé las series que se repiten a propósito de los duplicados reales, que no son lo mismo."),
            ("p", "Para clasificar cada publicación por formato y tema usé reglas escritas a mano, no un modelo. La razón es práctica: con 82 filas, "
                  "una regla se puede leer, discutir y probar con tests. Si una publicación cae en el tema equivocado, sé exactamente por qué."),
            ("h", "Lo que mostraron los números"),
            ("p", "Las publicaciones sobre carrera profesional pasaron del 9 % en agosto al 48 % en octubre. Los proyectos guiados bajaron del 41 % al 16 %, "
                  "y los temas de modelos de lenguaje, del 31 % al 8 %. La impresión era cierta y además tenía una dirección clara: el canal pasó de enseñar a construir a preparar para el empleo."),
            ("h", "Qué me llevo"),
            ("p", "Primero, que vale la pena medir lo que uno consume. Agosto sirve para aprender a construir; septiembre y octubre, para buscar trabajo, y saberlo cambia cómo uso el canal. "
                  "Segundo, que no todo problema de clasificación necesita IA: con pocos datos, una regla auditable es más honesta que un modelo. "
                  "Y tercero, que mis propias notas eran un dataset. De ellas salieron los otros cinco proyectos del portafolio."),
        ],
    },
    {
        "slug": "nota-umbral-churn",
        "title": "Por qué mi modelo de churn decide con 0,25 y no con 0,5",
        "date": "Noviembre de 2026", "role": "cientifico", "project": "churn-prediction-pipeline",
        "summary": "El umbral por defecto no sabe cuánto cuesta una oferta de retención. Elegirlo por beneficio subió la ganancia en 19 %.",
        "body": [
            ("p", "Casi todos los tutoriales de clasificación terminan igual: el modelo da una probabilidad y, si pasa de 0,5, el cliente se clasifica como “se va”. "
                  "Ese número parece neutral, pero esconde una decisión de negocio que nadie tomó."),
            ("h", "El problema real"),
            ("p", "Una empresa de telecomunicaciones quiere ofrecer retención a los clientes con riesgo de irse. Cada oferta cuesta dinero, y cada cliente retenido vale más que esa oferta. "
                  "Equivocarse por no contactar a alguien que se iba no cuesta lo mismo que contactar a alguien que se iba a quedar. Con costos distintos, 0,5 casi nunca es el mejor punto de corte."),
            ("h", "Cómo lo resolví"),
            ("p", "Comparé regresión logística, Random Forest y Gradient Boosting con validación cruzada de 5 folds. El más simple empató con los complejos: PR-AUC de 0,659 frente a 0,657. "
                  "Me quedé con la regresión logística porque se puede explicar variable por variable."),
            ("p", "Después elegí el umbral que maximiza el beneficio, usando predicciones out-of-fold y no el conjunto de prueba. Esto importa: si elijo el umbral mirando el test, el resultado final deja de ser una medición honesta."),
            ("h", "El resultado"),
            ("p", "El umbral óptimo quedó en 0,25. En el conjunto de prueba, el beneficio fue de 51.819 dólares frente a 43.440 con el umbral de 0,5: un 19 % más. "
                  "Con ese umbral se encuentra al 80 % de los clientes que se iban. El ROC-AUC en prueba fue de 0,842."),
            ("h", "Qué me llevo"),
            ("p", "Un modelo no termina en la métrica. La pregunta útil no es “¿qué tan bien clasifica?”, sino “¿qué decisión tomo con esto y cuánto vale?”. "
                  "Elegir el umbral es parte del modelo, y debería hacerse con los números del negocio sobre la mesa."),
        ],
    },
    {
        "slug": "nota-drift-monitoreo",
        "title": "Monitorear los datos no basta: lo que aprendí simulando drift",
        "date": "Noviembre de 2026", "role": "cientifico", "project": "model-drift-monitoring",
        "summary": "Simulé 16 semanas de producción. El cambio que más daño hizo no se veía en los datos, solo en el rendimiento.",
        "body": [
            ("p", "Un modelo entrenado hoy empieza a envejecer mañana. Los clientes cambian, los precios cambian y la relación entre las variables y el resultado también. "
                  "Quería ver ese envejecimiento de cerca, así que lo simulé."),
            ("h", "El montaje"),
            ("p", "Tomé el modelo de churn y simulé 16 semanas de producción con dos tipos de cambio controlados: data drift, cuando cambia la distribución de las variables, "
                  "y concept drift, cuando cambia la relación entre las variables y el churn. Para vigilarlo implementé PSI por variable, pruebas KS y chi-cuadrado, y monitoreo de calibración."),
            ("h", "Lo que pasó"),
            ("p", "La primera alerta de drift llegó en la semana 6. Desde la semana 7, el PSI de MonthlyCharges y Contract entró en zona crítica. La caída fuerte del rendimiento llegó en la semana 8."),
            ("p", "El hallazgo más importante fue incómodo: el concept drift no aparece en el PSI. Las variables pueden verse estables mientras el modelo se equivoca cada vez más. "
                  "Solo se detecta mirando el rendimiento, y para eso hacen falta etiquetas reales."),
            ("h", "Reentrenar también puede salir mal"),
            ("p", "Diseñé una política de reentrenamiento con disparadores por datos y por rendimiento, y un periodo de enfriamiento. Documenté un error propio: un reentrenamiento temprano, con pocos datos nuevos, empeoró el modelo. "
                  "Con la política final, el modelo vivo llegó a un AUC de 0,789 en las semanas 13 a 16, frente a 0,763 del modelo que nunca se actualizó."),
            ("h", "Qué me llevo"),
            ("p", "Vigilar solo los datos da una falsa tranquilidad. Un monitoreo útil combina las dos miradas, datos y rendimiento, y una regla clara de cuándo actuar y cuándo esperar."),
        ],
    },
]

COLOR = {"cientifico": "var(--cientifico)", "ia": "var(--ia)", "analista": "var(--analista)", "amber": "var(--amber)", "muted": "var(--faint)"}


def build(g):
    e, head, nav, FOOT, NAME = g["e"], g["head"], g["nav"], g["FOOT"], g["NAME"]
    BACK, GH, EMAIL, LINKEDIN, CV, PROJECTS = g["BACKDROP_ROLE"], g["GH"], g["EMAIL"], g["LINKEDIN"], g["CV"], g["PROJECTS"]

    # ---------- Sobre mí ----------
    tl = "".join(
        f'<li style="--role:{COLOR[c]}"><p class="when">{e(d)}</p><div><h3>{e(t)}</h3>{f"<p>{e(x)}</p>" if x else ""}</div></li>'
        for d, t, x, c in TIMELINE)
    sk = "".join(
        f'<div class="skill-group" style="--role:{COLOR[c]}"><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>'
        for n, c, items in SKILLS)
    if CERTS:
        certs = '<ul class="certs">' + "".join(
            f'<li><h3>{e(n)}</h3><p>{e(org)}, {e(y)}</p>{f"<a href={chr(34)}{u}{chr(34)}>Verificar</a>" if u else ""}</li>'
            for n, org, y, u in CERTS) + "</ul>"
    else:
        certs = ('<div class="certs-empty"><p>Estoy reuniendo mis certificados de formación. Este espacio se llenará pronto; '
                 'mientras tanto, cada proyecto del portafolio tiene su código y sus tests públicos como evidencia.</p>'
                 '<div class="slots" aria-hidden="true"><span></span><span></span><span></span></div></div>')
    body = f"""{head(f'Sobre mí · {NAME}', 'Trayectoria, habilidades y certificados de Juan Manuel Herrera Mejia.')}{nav('sobre')}
<main id="contenido" style="--role:var(--amber)">
<section class="role-hero">{BACK}<p class="tabname">sobre_mi.md</p><h1>Sobre mí</h1>
<p class="pitch">Estudio Estadística, enseño IA a equipos de empresa y construyo proyectos de datos que se pueden revisar.</p>
<p>Soy Juan Manuel Herrera Mejia y vivo en Medellín. Me interesa el punto donde la estadística se encuentra con decisiones reales: cuánto vale un modelo en dinero,
cuándo deja de servir y cómo explicárselo a alguien que no programa. Hablo español, inglés y portugués, y estoy aprendiendo alemán e italiano.</p>
<p class="actions"><a class="btn" href="{CV}" download>Descargar hoja de vida (PDF)</a><a class="btn ghost" href="mailto:{EMAIL}">Escribirme</a></p>
</section>
<section class="block"><h2>Trayectoria</h2><ol class="timeline">{tl}</ol></section>
<section class="block"><h2>Habilidades</h2><div class="skill-grid">{sk}</div></section>
<section class="block"><h2>Software que uso</h2><div class="sw-grid">{"".join(f'<div class="sw" style="--role:{COLOR[c]}"><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>' for n, c, items in SOFTWARE)}</div></section>
<section class="block"><h2>Idiomas</h2><ul class="langs">{"".join(f'<li><span>{e(l)}</span>{e(v)}</li>' for l, v in LANGS)}</ul></section>
<section class="block" id="certificados"><h2>Certificados de formación</h2>{certs}</section>
<section class="block contact-block"><h2>Hablemos</h2>
<p>Estoy abierto a prácticas, empleos y proyectos de análisis de datos, ciencia de datos e IA, en Medellín, híbridos o remotos.</p>
<ul class="contact-list">
<li><span>Correo</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><span>LinkedIn</span><a href="{LINKEDIN}">linkedin.com/in/juanmhmejia</a></li>
<li><span>GitHub</span><a href="{GH}">github.com/jmanuelhe</a></li>
<li><span>Hoja de vida</span><a href="{CV}" download>Descargar PDF</a></li>
</ul></section>
</main>
{FOOT}"""
    (ROOT / "sobre-mi.html").write_text(body, encoding="utf-8")

    # ---------- Notas ----------
    items = "".join(
        f'<li style="--role:{COLOR[n["role"]]}"><p class="when">{e(n["date"])}</p><h2><a href="{n["slug"]}.html">{e(n["title"])}</a></h2><p>{e(n["summary"])}</p></li>'
        for n in NOTES)
    body = f"""{head(f'Notas · {NAME}', 'Artículos cortos sobre lo que aprendí construyendo proyectos de datos e IA.')}{nav('notas')}
<main id="contenido" style="--role:var(--amber)">
<section class="role-hero">{BACK}<p class="tabname">notas/</p><h1>Notas</h1>
<p class="pitch">Lo que aprendí construyendo cada proyecto, contado sin código.</p>
<p>Cada nota sale de un proyecto real del portafolio. Si quieres ver los detalles técnicos, al final de cada una está el enlace al repositorio.</p></section>
<ul class="notes">{items}</ul>
</main>
{FOOT}"""
    (ROOT / "notas.html").write_text(body, encoding="utf-8")

    for n in NOTES:
        prose = "".join(f"<h2>{e(x)}</h2>" if k == "h" else f"<p>{e(x)}</p>" for k, x in n["body"])
        proj = next(p for p in PROJECTS.values() if p["repo"] == n["project"])
        others = "".join(f'<li><a href="{o["slug"]}.html">{e(o["title"])}</a></li>' for o in NOTES if o is not n)
        body = f"""{head(f'{n["title"]} · {NAME}', n['summary'])}{nav('notas')}
<main id="contenido" style="--role:{COLOR[n['role']]}">
<article class="note">
<p class="crumbs"><a href="notas.html">Notas</a></p>
<h1>{e(n['title'])}</h1>
<p class="note-meta">{e(n['date'])}. Juan Manuel Herrera Mejia</p>
<p class="note-lede">{e(n['summary'])}</p>
{prose}
<aside class="note-proj"><p>Proyecto relacionado</p><h3>{e(proj['title'])}</h3>
<p class="links"><a href="{GH}/{proj['repo']}">Ver código en GitHub</a></p></aside>
<nav class="more" aria-label="Otras notas"><h2>Otras notas</h2><ul>{others}</ul></nav>
</article>
</main>
{FOOT}"""
        (ROOT / f"{n['slug']}.html").write_text(body, encoding="utf-8")

    build_cv(g)


def build_cv(g):
    e, PROJECTS, EMAIL, LINKEDIN, GH = g["e"], g["PROJECTS"], g["EMAIL"], g["LINKEDIN"], g["GH"]
    proj = "".join(
        f'<li><b>{e(p["title"])}</b>. {e(p["question"])} <span class="k">{e(p["number"])} {e(p["number_label"])}</span></li>'
        for p in PROJECTS.values())
    skills = "".join(f'<p><b>{e(n)}:</b> {e(", ".join(items))}.</p>' for n, c, items in SKILLS)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Hoja de vida, Juan Manuel Herrera Mejia</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Public+Sans:wght@400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font:400 9.9pt/1.5 "Public Sans",sans-serif;color:#1d2433}}
header{{background:#0E1420;color:#E3E9F3;padding:26px 40px 22px}}
h1{{font:800 24pt/1 "Bricolage Grotesque",sans-serif;margin:0;letter-spacing:-.02em}}
.sub{{margin:8px 0 10px;color:#94A2B9;font-size:10.5pt}}
.ct{{font:8.4pt "JetBrains Mono",monospace;color:#F2C45F;display:flex;flex-wrap:wrap;gap:4px 18px}}
.ct a{{color:inherit;text-decoration:none}}
.bar{{height:4px;background:linear-gradient(90deg,#6CB2FF 0 33%,#4FD1B5 33% 66%,#B79CFF 66%)}}
main{{padding:18px 40px 24px;display:grid;grid-template-columns:1.75fr 1fr;gap:26px}}
h2{{font:700 11.5pt "Bricolage Grotesque",sans-serif;margin:14px 0 6px;padding-bottom:4px;border-bottom:1.5px solid #d7dde8;color:#0E1420}}
h2:first-child{{margin-top:0}}
h3{{font:600 10.2pt "Public Sans",sans-serif;margin:8px 0 1px}}
.when{{font:8pt "JetBrains Mono",monospace;color:#5f6d86;margin:0 0 3px}}
ul{{margin:3px 0 0;padding-left:14px}} li{{margin:2px 0}}
p{{margin:4px 0}}
.k{{display:block;color:#0d7d68;font-size:8.6pt}}
aside p{{font-size:9pt}}
</style></head><body>
<header><h1>Juan Manuel Herrera Mejia</h1>
<p class="sub">Estudiante de Estadística (UdeA). Análisis de datos, machine learning e IA generativa. Medellín, Colombia.</p>
<p class="ct"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{LINKEDIN}">linkedin.com/in/juanmhmejia</a><a href="https://jmanuelhe.github.io">jmanuelhe.github.io</a><a href="{GH}">github.com/jmanuelhe</a></p></header>
<div class="bar"></div>
<main><div>
<h2>Perfil</h2>
<p>Estudiante de Estadística con dos años diseñando formación en IA generativa para empresas y un año como consultor independiente en análisis de datos.
Construyo proyectos que se evalúan en términos de negocio, con código, datos y tests públicos.</p>
<h2>Experiencia</h2>
<p class="when">Nov. 2025 – actualidad</p><h3>Consultor independiente en análisis de datos y documentación</h3>
<ul><li>Limpieza y análisis de datos en Python (pandas, SciPy) y Excel, con pruebas estadísticas y gráficos.</li>
<li>Informes y documentos corporativos en Word y Excel: estructura, diseño y consolidación de versiones.</li>
<li>Traducción y digitalización de documentos con OCR; uso de IA con control de calidad.</li></ul>
<p class="when">Nov. 2024 – actualidad</p><h3>Diseñador de formación en IA para empresas</h3>
<ul><li>Curso completo sobre el uso de Claude en procesos de negocio: casos de uso, prompts y flujos de trabajo.</li>
<li>Materiales de presentación con sistema de diseño profesional y revisión visual de calidad.</li>
<li>Traducción al español de guías técnicas de certificación en IA.</li></ul>
<h2>Proyectos</h2><ul>{proj}</ul>
</div><aside>
<h2>Educación</h2><p class="when">2024 – 2029 (esperado)</p><h3>Pregrado en Estadística</h3><p>Universidad de Antioquia, Medellín.</p>
<h2>Habilidades</h2>{skills}
<h2>Software</h2>{"".join(f"<p><b>{e(n)}:</b> {e(chr(44).join(chr(32)+x for x in items).strip())}.</p>" for n, c, items in SOFTWARE)}
<h2>Idiomas</h2>{"".join(f"<p>{e(l)}, {e(v[0].lower() + v[1:])}.</p>" for l, v in LANGS)}
<h2>Portafolio</h2><p>Seis proyectos organizados por rol (analista, científico de datos, ingeniero de IA) en jmanuelhe.github.io.</p>
</aside></main></body></html>"""
    src = ROOT / "assets" / "cv.html"
    src.write_text(html, encoding="utf-8")
    import asyncio
    from playwright.async_api import async_playwright

    async def run():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page()
            await pg.goto(src.resolve().as_uri())
            await pg.wait_for_timeout(1500)
            await pg.pdf(path=str(ROOT / g["CV"]), format="A4", print_background=True)
            await b.close()
    asyncio.run(run())
    src.unlink()
