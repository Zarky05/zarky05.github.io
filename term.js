// La terminal de la portada imprime su resumen línea por línea, una sola vez.
(function () {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const lines = document.querySelectorAll(".term .ln");
  if (!lines.length) return;
  document.documentElement.classList.add("js");
  lines.forEach((ln, i) => setTimeout(() => ln.classList.add("on"), 250 + i * 230));
})();
