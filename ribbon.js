// Línea de tiempo de publicaciones (SVG generado en el navegador a partir de POSTS).
(function () {
  const el = document.getElementById("ribbon");
  const tip = document.getElementById("ribbon-tip");
  if (!el) return;
  const NS = "http://www.w3.org/2000/svg";
  const start = new Date("2026-08-02T00:00:00"), end = new Date("2026-10-30T00:00:00");
  const days = Math.round((end - start) / 864e5) + 1;
  const byDay = {};
  POSTS.forEach(p => (byDay[p.d] = byDay[p.d] || []).push(p));
  const roleColor = { analista: "var(--analista)", cientifico: "var(--cientifico)", "ingeniero-ia": "var(--ia)" };
  const meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];

  function draw() {
    el.innerHTML = "";
    const W = el.clientWidth, H = el.clientHeight, top = 34, bottom = 22, plotH = H - top - bottom;
    const narrow = W < 640;
    const step = W / days, bw = Math.max(1.5, step * 0.62);
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
    const unit = plotH / 2; // máximo 2 publicaciones por día
    let pinIndex = 0;
    for (let i = 0; i < days; i++) {
      const d = new Date(start.getTime() + i * 864e5);
      const key = d.toISOString().slice(0, 10);
      const posts = byDay[key] || [];
      const x = i * step + (step - bw) / 2;
      if (d.getDate() === 1 || i === 0) {
        const t = document.createElementNS(NS, "text");
        t.setAttribute("x", i * step); t.setAttribute("y", H - 4); t.setAttribute("class", "month");
        t.textContent = d.getDate() === 1 ? meses[d.getMonth()] : `${d.getDate()} ${meses[d.getMonth()]}`;
        svg.appendChild(t);
      }
      const seed = SEEDS[key];
      if (!posts.length) {
        const r = document.createElementNS(NS, "rect");
        r.setAttribute("x", x); r.setAttribute("y", top + plotH - 1.5); r.setAttribute("width", bw); r.setAttribute("height", 1.5);
        r.setAttribute("fill", "var(--rule)"); svg.appendChild(r);
        continue;
      }
      const h = unit * Math.min(posts.length, 2);
      const r = document.createElementNS(NS, "rect");
      r.setAttribute("x", x); r.setAttribute("y", top + plotH - h); r.setAttribute("width", bw); r.setAttribute("height", h);
      r.setAttribute("rx", Math.min(bw / 2, 2)); r.setAttribute("class", "day"); r.style.setProperty("--i", i);
      r.setAttribute("tabindex", "0");
      const label = `${d.getDate()} ${meses[d.getMonth()]}: ` + posts.map(p => p.t).join(" · ");
      r.setAttribute("aria-label", label);
      const show = () => (tip.textContent = label + (seed ? `  →  inspiró «${seed.t}»` : ""));
      r.addEventListener("mouseenter", show); r.addEventListener("focus", show); r.addEventListener("click", show);
      if (seed) {
        const c = roleColor[seed.role];
        r.style.fill = c; r.classList.add("seed");
        const go = () => (location.href = `${PAGES[seed.role]}#${seed.repo}`);
        r.addEventListener("click", go);
        r.addEventListener("keydown", e => { if (e.key === "Enter") go(); });
        const ln = document.createElementNS(NS, "line");
        const cx = x + bw / 2, ly = narrow ? 12 : (pinIndex % 2 ? 26 : 12);
        ln.setAttribute("x1", cx); ln.setAttribute("x2", cx); ln.setAttribute("y1", ly + 4); ln.setAttribute("y2", top + plotH - h - 3);
        ln.setAttribute("stroke", c); ln.setAttribute("stroke-width", 1.2); svg.appendChild(ln);
        if (!narrow) {
          const t = document.createElementNS(NS, "text");
          const anchorEnd = cx > W - 170;
          t.setAttribute("x", anchorEnd ? cx - 5 : cx + 5); t.setAttribute("y", ly);
          t.setAttribute("text-anchor", anchorEnd ? "end" : "start");
          t.setAttribute("class", "pin-label"); t.setAttribute("fill", c); t.textContent = seed.t;
          svg.appendChild(t);
        } else {
          const dot = document.createElementNS(NS, "circle");
          dot.setAttribute("cx", cx); dot.setAttribute("cy", ly); dot.setAttribute("r", 3.5); dot.setAttribute("fill", c);
          svg.appendChild(dot);
        }
        pinIndex++;
      }
      svg.appendChild(r);
    }
    el.appendChild(svg);
  }
  draw();
  let t; window.addEventListener("resize", () => { clearTimeout(t); t = setTimeout(draw, 120); });
})();
