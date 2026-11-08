"""Genera el sitio estático (index + 3 portafolios) desde un solo lugar con los datos de los proyectos.

Uso: python build.py   → escribe index.html, analista.html, cientifico.html, ingeniero-ia.html
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
GH = "https://github.com/jmanuelhe"
NAME = "Juan Manuel Herrera Mejia"
EMAIL = "jherreramej@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/juanmhmejia"

PROJECTS = {
    "mdd": {
        "title": "My Data Diary Analytics",
        "repo": "my-data-diary-analytics",
        "question": "¿Cómo cambió en tres meses el contenido de un canal educativo de IA?",
        "seed": None,
        "number": "9 % → 48 %",
        "number_label": "de publicaciones sobre carrera profesional, de agosto a octubre",
        "did": [
            "Extraje las tablas de mis tres informes mensuales en Word a un dataset de 82 publicaciones.",
            "Limpié fechas, detecté reenvíos y distinguí series recurrentes de duplicados reales.",
            "Clasifiqué cada publicación por formato y tema con reglas auditables, validadas con tests.",
            "Construí gráficos y un dashboard interactivo con filtro de texto.",
        ],
        "finding": "El canal pasó de enseñar a construir (41 % de proyectos guiados en agosto) a preparar para el empleo. "
                   "Agosto sirve para aprender a construir; septiembre y octubre, para buscar trabajo.",
        "stack": "Python, pandas, python-docx, expresiones regulares, matplotlib, Plotly, pytest",
        "img": "temas_por_mes.png",
        "img_alt": "Mapa de calor de temas por mes: carrera profesional sube de 9 % a 48 %, LLMs baja de 31 % a 8 %.",
        "dashboard": "dashboards/my-data-diary.html",
    },
    "telco": {
        "title": "Telco Churn · Análisis SQL",
        "repo": "telco-churn-sql-analysis",
        "question": "¿Quién se va, cuánto ingreso se pierde y dónde conviene actuar primero?",
        "seed": None,
        "number": "38 %",
        "number_label": "del ingreso perdido viene de un segmento que es solo el 13 % de los clientes",
        "did": [
            "Modelé los datos en capas: CSV crudo, vista de staging tipada y consultas de negocio.",
            "Escribí 9 consultas SQL con CTE, funciones de ventana y FILTER, y reglas de calidad de datos.",
            "Controlé una variable de confusión: el aparente efecto de los servicios adicionales era sobre todo antigüedad.",
            "Convertí los hallazgos en cinco recomendaciones accionables.",
        ],
        "finding": "Contrato mes a mes + fibra + menos de un año: 70 % de churn. Es el segmento donde la retención rinde más.",
        "stack": "SQL, DuckDB, Python, pandas, matplotlib, pytest",
        "img": "matriz_riesgo.png",
        "img_alt": "Matriz de churn por contrato y tipo de internet: mes a mes con fibra llega a 55 %.",
        "dashboard": None,
    },
    "churn": {
        "title": "Churn Prediction Pipeline",
        "repo": "churn-prediction-pipeline",
        "question": "¿A qué clientes conviene ofrecerles retención, si cada oferta cuesta dinero?",
        "seed": ("2026-08-30", "How to Build an ML Pipeline With Python and SQL"),
        "number": "+19 %",
        "number_label": "de beneficio frente al umbral por defecto de 0,5",
        "did": [
            "Extraje las features con SQL, con una regla explícita contra la fuga de datos.",
            "Comparé regresión logística, Random Forest y Gradient Boosting con validación cruzada de 5 folds.",
            "Elegí el umbral de decisión maximizando el beneficio con predicciones out-of-fold, no con el test.",
            "Verifiqué la calibración y medí la importancia de las variables por permutación.",
        ],
        "finding": "El modelo más simple empató con los complejos (PR-AUC 0,659 vs. 0,657) y ganó por interpretable. "
                   "Con el umbral de negocio se encuentra al 80 % de los clientes que se iban.",
        "stack": "Python, scikit-learn, DuckDB, SQL, joblib, matplotlib, pytest",
        "img": "curva_beneficio.png",
        "img_alt": "Curva de beneficio según el umbral: el máximo está cerca de 0,25.",
        "dashboard": None,
    },
    "drift": {
        "title": "Model Drift Monitoring",
        "repo": "model-drift-monitoring",
        "question": "¿Cómo sé que mi modelo dejó de servir y cuándo debo reentrenarlo?",
        "seed": ("2026-09-13", "I Built an ML Pipeline That Retrains a Model When Performance Drops"),
        "number": "Semana 6",
        "number_label": "primera alerta de drift; la caída fuerte del rendimiento llegó en la semana 8",
        "did": [
            "Simulé 16 semanas de producción con data drift y concept drift controlados y reproducibles.",
            "Implementé PSI por variable, pruebas KS y chi-cuadrado, y monitoreo de calibración.",
            "Diseñé una política de reentrenamiento con disparadores por datos y por rendimiento, y enfriamiento.",
            "Documenté también lo que no funcionó: un reentrenamiento temprano que empeoró el modelo.",
        ],
        "finding": "El concept drift no aparece en el PSI: solo se ve en el rendimiento. Monitorear solo los datos no basta.",
        "stack": "Python, scikit-learn, SciPy, pandas, Plotly, matplotlib, pytest",
        "img": "psi_heatmap.png",
        "img_alt": "Mapa de calor del PSI por variable y semana: MonthlyCharges y Contract se vuelven críticos desde la semana 7.",
        "dashboard": "dashboards/drift-monitoring.html",
    },
    "rag": {
        "title": "RAG Document Q&A",
        "repo": "rag-document-qa",
        "question": "¿Puedo preguntarle a mis propios informes y recibir respuestas con fuente?",
        "seed": ("2026-08-26", "Building a Document Q&A System"),
        "number": "0,933",
        "number_label": "de acierto en la primera posición, sobre 45 preguntas escritas a mano",
        "did": [
            "Diseñé un chunking estructural: una publicación por fragmento, 105 fragmentos en total.",
            "Implementé BM25 desde cero, TF-IDF de caracteres y fusión híbrida (RRF).",
            "Agregué filtros por fecha y por mes, que corrigieron todas las preguntas de tipo fecha.",
            "Generación con Claude con citas verificables y detección de fuentes inventadas.",
        ],
        "finding": "El híbrido supera a cada método por separado. El punto débil medido es la búsqueda semántica, "
                   "y por eso el siguiente paso son los embeddings.",
        "stack": "Python, scikit-learn, Claude API, Streamlit, python-docx, pytest",
        "img": None,
        "img_alt": "",
        "dashboard": None,
    },
    "agent": {
        "title": "AI CSV Analyst Agent",
        "repo": "ai-csv-analyst-agent",
        "question": "¿Puede un agente analizar un CSV sin ejecutar código peligroso ni gastar sin control?",
        "seed": ("2026-10-28", "Build an AI Data Analyst That Turns CSV Files into Insights"),
        "number": "6",
        "number_label": "herramientas validadas: el modelo nunca ejecuta código arbitrario",
        "did": [
            "Construí un bucle de tool use con Claude, con límites de pasos y de presupuesto en USD.",
            "Hice que los errores de las herramientas vuelvan al modelo como datos, para que se corrija solo.",
            "Implementé un tracker de costo y latencia (tokens, p50/p95, log JSONL por llamada).",
            "Creé un cliente offline que imita la API, para correr el agente y sus tests sin costo.",
        ],
        "finding": "En la demo, el agente encontró solo que el contrato es la variable que más separa el churn "
                   "(42,7 % vs. 2,8 %), igual que el análisis SQL hecho a mano.",
        "stack": "Python, Claude API (tool use), pandas, matplotlib, pytest",
        "img": "agente_chart.png",
        "img_alt": "Gráfico generado por el agente: tasa de churn por tipo de contrato.",
        "dashboard": None,
    },
}

ROLES = {
    "analista": {
        "file": "analista.html", "name": "Analista de datos", "short": "análisis de datos", "color": "var(--analista)",
        "pitch": "Convierto datos desordenados en respuestas que alguien puede usar para decidir.",
        "intro": "Estos proyectos muestran el trabajo de punta a punta: sacar datos de donde están (incluso de un Word), "
                 "limpiarlos con criterio, consultarlos con SQL y contar lo que encontré con gráficos y recomendaciones.",
        "main": ["mdd", "telco"], "also": ["agent", "churn"],
        "skills": ["SQL (CTE, funciones de ventana, calidad de datos)", "Python y pandas", "Visualización con matplotlib y Plotly",
                   "Dashboards", "Limpieza y validación de datos", "Comunicación de hallazgos y recomendaciones"],
    },
    "cientifico": {
        "file": "cientifico.html", "name": "Científico de datos", "short": "ciencia de datos", "color": "var(--cientifico)",
        "pitch": "Construyo modelos que se evalúan en dinero, no solo en accuracy, y los vigilo cuando están en producción.",
        "intro": "Dos proyectos conectados: un modelo de churn con umbral elegido por beneficio de negocio, "
                 "y el sistema que detecta cuándo ese modelo deja de funcionar.",
        "main": ["churn", "drift"], "also": ["telco", "rag"],
        "skills": ["scikit-learn (Pipelines, validación cruzada)", "Métricas para clases desbalanceadas", "Calibración de probabilidades",
                   "Estadística (PSI, KS, chi-cuadrado)", "Variables de confusión", "Monitoreo de modelos"],
    },
    "ingeniero-ia": {
        "file": "ingeniero-ia.html", "name": "Ingeniero de IA", "short": "ingeniería de IA", "color": "var(--ia)",
        "pitch": "Construyo aplicaciones con LLMs que se pueden medir, auditar y operar con presupuesto.",
        "intro": "Un sistema RAG evaluado con preguntas propias y un agente con herramientas seguras. "
                 "En los dos, la prioridad es la confiabilidad: citas verificables, límites, costos y tests sin red.",
        "main": ["rag", "agent"], "also": ["drift", "mdd"],
        "skills": ["Claude API: tool use y prompts de sistema", "RAG: chunking, BM25, búsqueda híbrida", "Evaluación de LLMs (hit@k, MRR, abstención)",
                   "Seguridad en agentes", "Seguimiento de costo y latencia", "Tests con clientes simulados"],
    },
}

e = html.escape


def head(title, desc):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
"""


def nav(active=None):
    links = "".join(
        f'<a href="{r["file"]}" style="--role:{r["color"]}"{" aria-current=page" if k == active else ""}>{r["name"]}</a>'
        for k, r in ROLES.items())
    return f"""<header class="top"><a class="me" href="index.html">{NAME}</a><nav aria-label="Portafolios">{links}</nav></header>"""


FOOT = f"""<footer class="foot"><p>{NAME} · Medellín, Colombia</p>
<p class="contact"><a href="mailto:{EMAIL}">{EMAIL}</a> <a href="{LINKEDIN}">LinkedIn</a> <a href="{GH}">GitHub</a></p>
<p class="small">Todos los proyectos tienen código, datos y tests en sus repositorios.</p></footer>
</body></html>"""


def entry(key, role_color):
    p = PROJECTS[key]
    seed = ""
    if p["seed"]:
        d, t = p["seed"]
        seed = f'<p class="seed">Idea tomada de “{e(t)}”, publicada el {int(d[8:])} de {["", "", "", "", "", "", "", "", "agosto", "septiembre", "octubre"][int(d[5:7])]}.</p>'
    fig = (f'<figure><a href="assets/img/{p["img"]}" title="Ver imagen en tamaño completo"><img src="assets/img/{p["img"]}" alt="{e(p["img_alt"])}" loading="lazy"></a></figure>'
           if p["img"] else '<figure class="eval"><table><caption>Recuperación, 45 preguntas</caption>'
                            '<thead><tr><th>Método</th><th>Hit@1</th><th>MRR</th></tr></thead><tbody>'
                            '<tr><td>BM25</td><td>0,844</td><td>0,875</td></tr><tr><td>TF-IDF</td><td>0,889</td><td>0,904</td></tr>'
                            '<tr><td>Híbrido</td><td>0,911</td><td>0,922</td></tr>'
                            '<tr class="best"><td>Híbrido + filtros</td><td>0,933</td><td>0,944</td></tr></tbody></table></figure>')
    dash = f'<a href="{p["dashboard"]}">Abrir dashboard</a>' if p["dashboard"] else ""
    did = "".join(f"<li>{e(x)}</li>" for x in p["did"])
    return f"""<article class="entry" id="{p['repo']}" style="--role:{role_color}">
<div class="entry-text">
<h2>{e(p['title'])}</h2>
<p class="question">{e(p['question'])}</p>
{seed}
<p class="number"><strong>{e(p['number'])}</strong> <span>{e(p['number_label'])}</span></p>
<h3>Qué hice</h3><ul>{did}</ul>
<h3>Qué encontré</h3><p>{e(p['finding'])}</p>
<p class="stack"><span>Herramientas:</span> {e(p['stack'])}</p>
<p class="links"><a href="{GH}/{p['repo']}">Ver código en GitHub</a>{dash}</p>
</div>
{fig}
</article>"""


def role_page(key):
    r = ROLES[key]
    also = "".join(f'<li><a href="{GH}/{PROJECTS[k]["repo"]}">{e(PROJECTS[k]["title"])}</a> · {e(PROJECTS[k]["question"])}</li>'
                   for k in r["also"])
    skills = "".join(f"<li>{e(s)}</li>" for s in r["skills"])
    body = f"""{head(f'{r["name"]} · {NAME}', r['pitch'])}{nav(key)}
<main id="contenido" style="--role:{r['color']}">
<section class="role-hero"><h1>{r['name']}</h1><p class="pitch">{e(r['pitch'])}</p><p>{e(r['intro'])}</p></section>
{''.join(entry(k, r['color']) for k in r['main'])}
<section class="aside-grid">
<div><h2>Habilidades que demuestran estos proyectos</h2><ul class="skills">{skills}</ul></div>
<div><h2>También relevante</h2><ul class="also">{also}</ul></div>
</section>
</main>
{FOOT}"""
    (ROOT / r["file"]).write_text(body, encoding="utf-8")


def index():
    posts = json.loads(Path("/tmp/posts.json").read_text()) if Path("/tmp/posts.json").exists() else \
        json.loads((ROOT / "assets" / "posts.json").read_text())
    (ROOT / "assets" / "posts.json").write_text(json.dumps(posts, ensure_ascii=False))
    seeds = {p["seed"][0]: {"t": p["title"], "repo": p["repo"],
                           "role": next(k for k, r in ROLES.items() if pk in r["main"])}
             for pk, p in PROJECTS.items() if p["seed"]}
    cols = ""
    for k, r in ROLES.items():
        items = "".join(f'<li><a href="{r["file"]}#{PROJECTS[pk]["repo"]}">{e(PROJECTS[pk]["title"])}</a>'
                        f'<span>{e(PROJECTS[pk]["number"])} {e(PROJECTS[pk]["number_label"])}</span></li>' for pk in r["main"])
        cols += f"""<section class="role-col" style="--role:{r['color']}"><h2><a href="{r['file']}">{r['name']}</a></h2>
<p>{e(r['pitch'])}</p><ul>{items}</ul><p class="go"><a href="{r['file']}">Ver los proyectos de {r['short']}</a></p></section>"""
    body = f"""{head(f'{NAME} · Datos e IA', 'Portafolio de análisis de datos, ciencia de datos e ingeniería de IA.')}{nav()}
<main id="contenido">
<section class="hero">
<h1>Durante 90 días seguí un canal sobre IA y anoté cada publicación. De esas notas salieron seis proyectos.</h1>
<p class="lede">Soy Juan Manuel, estudiante de la Universidad de Antioquia en Medellín. Trabajo con datos e IA. Este portafolio está organizado por rol: elige el que te interesa, o recorre la línea de tiempo.</p>
<figure class="ribbon" aria-labelledby="ribbon-cap">
<div id="ribbon" role="img" aria-label="Línea de tiempo de 82 publicaciones entre agosto y octubre de 2026, con las publicaciones que inspiraron proyectos marcadas."></div>
<figcaption id="ribbon-cap">Cada barra es un día, del 2 de agosto al 30 de octubre de 2026; la altura es el número de publicaciones.
Las marcas de color son las publicaciones que inspiraron un proyecto. Pasa el cursor o toca una barra para ver el título.</figcaption>
<p id="ribbon-tip" class="tip" aria-live="polite">&nbsp;</p>
</figure>
</section>
<div class="roles">{cols}</div>
</main>
<script>
const POSTS = {json.dumps(posts, ensure_ascii=False)};
const SEEDS = {json.dumps(seeds, ensure_ascii=False)};
const PAGES = {json.dumps({k: r["file"] for k, r in ROLES.items()})};
</script>
<script src="ribbon.js"></script>
{FOOT}"""
    (ROOT / "index.html").write_text(body, encoding="utf-8")


if __name__ == "__main__":
    index()
    for k in ROLES:
        role_page(k)
    print("ok")
