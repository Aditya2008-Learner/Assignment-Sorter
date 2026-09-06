import React, { useRef, useEffect, useId, useMemo } from "react";

export default function App() {
  const gradientRef = useRef<SVGSVGElement>(null);
  const gradientHeight = 420;
  const restingReveal = 0.06;
  const idBase = useId();
  const blurId = `blur-${idBase}`;
  const gradientId = `grad-${idBase}`;

  const cols = useMemo(() => {
    const heights = [420, 360, 280, 320, 210, 160, 120, 80];
    return [
      { h: heights[0], c: "#0a1122" },
      { h: heights[1], c: "#0040ff" },
      { h: heights[2], c: "#00c8ff" },
      { h: heights[3], c: "#f0f8ff" },
      { h: heights[4], c: "#bbff00" },
      { h: heights[5], c: "#ff6b5b" },
      { h: heights[6], c: "#ff9988" },
      { h: heights[7], c: "transparent" },
    ];
  }, []);

  useEffect(() => {
    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const el = gradientRef.current;
    if (!el || prefersReduced) {
      if (el) el.style.transform = "scaleY(1)";
      return;
    }
    let raf: number;
    const onScroll = () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const doc = document.documentElement;
        const scrollBottom = doc.scrollTop + doc.clientHeight;
        const docHeight = doc.scrollHeight;
        const remain = docHeight - scrollBottom;
        const reveal = Math.max(0, Math.min(1, 1 - remain / gradientHeight));
        const scale = restingReveal + (1 - restingReveal) * reveal;
        el.style.transform = `scaleY(${scale})`;
        el.style.transformOrigin = "bottom center";
      });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    onScroll();
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      cancelAnimationFrame(raf);
    };
  }, [gradientHeight, restingReveal]);

  const brandName = "Lumina";
  const desc = "Tools for focused study and deep work.";

  return (
    <div className="min-h-[120dvh] relative bg-[#faf8f3] text-[#1c1917] font-sans selection:bg-amber-200/30">
      {/* Intro */}
      <main className="flex flex-col items-center justify-center text-center px-6 pt-32 pb-24 md:pt-48 md:pb-32 max-w-3xl mx-auto">
        <h1 className="text-5xl md:text-7xl lg:text-8xl font-extrabold tracking-tighter leading-[0.92] text-[#1c1917] mb-8">
          Scroll toward<br />
          <span className="text-[#0040ff]">light.</span>
        </h1>
        <p className="text-lg md:text-xl text-[#6b6358] leading-relaxed max-w-xl mb-10">
          A calm landing experience with a chromatic gradient rising from the bottom — smooth, precise, and directly tied to your scroll.
        </p>
        <a href="#footer" className="inline-flex items-center gap-3 text-[#1c1917]/40 text-sm uppercase tracking-[0.2em] font-medium hover:text-[#0040ff] transition-colors">
          Continue <span aria-hidden="true" className="inline-block animate-bounce">↓</span>
        </a>
      </main>

      {/* Gradient layer — fixed bottom, hidden until scroll */}
      <div className="fixed bottom-0 left-0 w-full h-[420px] z-0 pointer-events-none" aria-hidden="true">
        <svg
          ref={gradientRef}
          className="w-full h-full block"
          viewBox="0 0 1440 420"
          preserveAspectRatio="none"
          style={{ transform: `scaleY(${0.06})`, transformOrigin: "bottom center", transition: "transform 0.05s linear" }}
        >
          <defs>
            <filter id={blurId} x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="28" />
            </filter>
            <linearGradient id={gradientId} x1="0" y1="1" x2="0" y2="0">
              <stop offset="0%" stopColor="#0a1122" />
              <stop offset="15%" stopColor="#0040ff" />
              <stop offset="30%" stopColor="#00c8ff" />
              <stop offset="50%" stopColor="#f0f8ff" />
              <stop offset="65%" stopColor="#bbff00" />
              <stop offset="80%" stopColor="#ff6b5b" />
              <stop offset="95%" stopColor="#ff9988" />
              <stop offset="100%" stopColor="transparent" />
            </linearGradient>
          </defs>
          <rect x="0" y="0" width="1440" height="420" fill={`url(#${gradientId})`} filter={`url(#${blurId})`} />
          {/* Overlapping vertical columns for dome shape */}
          {cols.map((c, i) => {
            const w = 72 + (i % 2) * 36;
            const x = 72 + i * 160 + (i * 8);
            const h = c.h;
            const y = 420 - h;
            return (
              <rect
                key={i}
                x={x}
                y={y}
                width={w}
                height={h}
                rx={w / 2}
                ry={w / 3}
                fill={c.c}
                filter={`url(#${blurId})`}
                opacity={0.92}
              />
            );
          })}
        </svg>
      </div>

      {/* Footer */}
      <footer id="footer" className="relative z-10 bg-[#121212] text-[#f4f1ea]">
        <div className="max-w-7xl mx-auto px-8 md:px-12 pb-12 pt-24">
          {/* Top row */}
          <div className="flex flex-col lg:flex-row gap-16 lg:gap-24 mb-16">
            {/* Brand + newsletter */}
            <div className="flex-1 lg:max-w-md">
              <a href="#" aria-label="Lumina" className="inline-flex items-center gap-3 mb-6 group" onClick={e => { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); }}>
                <span className="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#0040ff] via-[#0090ff] to-[#bbff00] flex items-center justify-center shadow-[0_0_24px_rgba(37,99,235,0.35)]">
                  <span className="text-white font-extrabold text-lg leading-none">L</span>
                </span>
                <span className="font-extrabold text-xl tracking-[-0.03em] text-[#f4f1ea] group-hover:text-[#bbff00] transition-colors">{brandName}</span>
              </a>
              <p className="text-[#a8a28e] leading-relaxed mb-6 text-sm">{desc}</p>
              <form
                className="flex items-center gap-2"
                onSubmit={e => { e.preventDefault(); const btn = (e.currentTarget.querySelector('button') as HTMLButtonElement); btn.textContent = 'Subscribed'; btn.disabled = true; }}
              >
                <label htmlFor="email" className="sr-only">Email for newsletter</label>
                <input
                  id="email"
                  type="email"
                  placeholder="your@email.com"
                  required
                  className="flex-1 bg-white/10 border border-white/10 rounded-full px-5 py-2.5 text-sm text-[#f4f1ea] placeholder:text-[#a8a28e]/60 focus:outline-none focus:border-[#bbff00]/50 transition-colors"
                />
                <button
                  type="submit"
                  className="bg-[#bbff00] text-[#121212] rounded-full px-5 py-2.5 text-sm font-bold hover:bg-[#d4ff40] hover:-translate-y-px transition-all shadow-[0_0_16px_rgba(187,255,0,0.25)]"
                >
                  Subscribe
                </button>
              </form>
            </div>

            {/* Navigation columns */}
            <nav aria-label="Footer" className="flex-1 grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-12">
              {[
                { title: "Product", links: ["Features", "Notes", "Assignments", "Quizzes"] },
                { title: "Resources", links: ["Study Material", "Practice Problems", "Previous Papers", "Flashcards"] },
                { title: "Company", links: ["About", "Careers", "Blog", "Contact"] },
                { title: "Legal", links: ["Privacy", "Terms", "Security", "Status"] },
              ].map(col => (
                <div key={col.title}>
                  <h3 className="text-[11px] font-extrabold uppercase tracking-[0.15em] text-[#a8a28e] mb-4">{col.title}</h3>
                  <ul className="space-y-2.5">
                    {col.links.map(l => (
                      <li key={l}><a href="#" className="text-sm text-[#cfc8b6] hover:text-[#f4f1ea] transition-colors" onClick={e => e.preventDefault()}>{l}</a></li>
                    ))}
                  </ul>
                </div>
              ))}
            </nav>
          </div>

          {/* Bottom bar */}
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pt-8 border-t border-white/[0.08]">
            <div className="flex items-center gap-6 text-xs text-[#7a7468]">
              <span>© 2026 Lumina</span>
              <span className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#bbff00] shadow-[0_0_6px_rgba(187,255,0,0.6)]" aria-hidden="true"></span>
                System online
              </span>
              <span>Remote — Worldwide</span>
            </div>
            <div className="text-xs text-[#7a7468] tracking-wide">Built for focused study.</div>
          </div>
        </div>
      </footer>
    </div>
  );
}
