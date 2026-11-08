# jmanuelhe.github.io

Sitio de portafolio con tres vistas por rol: **Analista de datos**, **Científico de datos** e **Ingeniero de IA**.

- `build.py` genera `index.html` y las tres páginas a partir de un solo diccionario con los proyectos. Para editar textos, cambia `PROJECTS` o `ROLES` y ejecuta `python build.py`.
- `ribbon.js` dibuja la línea de tiempo de la portada a partir de `assets/posts.json`.
- `dashboards/` contiene los dashboards interactivos de los proyectos.

Sitio estático, sin dependencias. Se publica con GitHub Pages desde la rama `main`.
