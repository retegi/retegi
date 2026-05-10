(function () {
  "use strict";

  var canvas = document.getElementById("hero-ai-network");
  if (!canvas || !canvas.getContext) {
    return;
  }

  var ctx = canvas.getContext("2d");
  var parent = canvas.closest(".hero-ai-bg");
  if (!parent) {
    return;
  }

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  var mqCoarse = window.matchMedia("(max-width: 767px)");
  var running = false;
  var rafId = 0;
  var nodes = [];
  var linkDist = 118;
  var w = 0;
  var h = 0;
  var dpr = 1;

  function countNodes() {
    if (mqCoarse.matches) {
      return 14;
    }
    return 34;
  }

  function randVel() {
    return (Math.random() - 0.5) * 0.22;
  }

  function initNodes() {
    var n = countNodes();
    nodes = [];
    var i;
    for (i = 0; i < n; i += 1) {
      nodes.push({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: randVel(),
        vy: randVel(),
      });
    }
  }

  function resize() {
    var rect = parent.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = Math.max(1, Math.floor(rect.width));
    h = Math.max(1, Math.floor(rect.height));
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    initNodes();
  }

  function stepNodes() {
    var pad = 8;
    var i;
    for (i = 0; i < nodes.length; i += 1) {
      var p = nodes[i];
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < pad || p.x > w - pad) {
        p.vx *= -1;
        p.x = Math.max(pad, Math.min(w - pad, p.x));
      }
      if (p.y < pad || p.y > h - pad) {
        p.vy *= -1;
        p.y = Math.max(pad, Math.min(h - pad, p.y));
      }
    }
  }

  function drawFrame() {
    if (w < 8 || h < 8) {
      return;
    }

    var i;
    var j;
    var dx;
    var dy;
    var dist;
    var alpha;

    ctx.clearRect(0, 0, w, h);

    for (i = 0; i < nodes.length; i += 1) {
      for (j = i + 1; j < nodes.length; j += 1) {
        dx = nodes[i].x - nodes[j].x;
        dy = nodes[i].y - nodes[j].y;
        dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < linkDist) {
          alpha = (1 - dist / linkDist) * 0.14;
          ctx.strokeStyle = "rgba(29, 78, 216, " + alpha + ")";
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.stroke();
        }
      }
    }

    for (i = 0; i < nodes.length; i += 1) {
      ctx.beginPath();
      ctx.arc(nodes[i].x, nodes[i].y, 2, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(15, 23, 42, 0.18)";
      ctx.fill();
      ctx.beginPath();
      ctx.arc(nodes[i].x, nodes[i].y, 1.1, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(16, 185, 129, 0.12)";
      ctx.fill();
    }
  }

  function drawStatic() {
    resize();
    drawFrame();
  }

  function loop() {
    if (!running) {
      return;
    }
    stepNodes();
    drawFrame();
    rafId = window.requestAnimationFrame(loop);
  }

  function start() {
    if (reducedMotion.matches || document.hidden) {
      return;
    }
    running = true;
    if (rafId) {
      window.cancelAnimationFrame(rafId);
    }
    rafId = window.requestAnimationFrame(loop);
  }

  function stop() {
    running = false;
    if (rafId) {
      window.cancelAnimationFrame(rafId);
      rafId = 0;
    }
  }

  function onVisibility() {
    if (document.hidden) {
      stop();
    } else if (!reducedMotion.matches) {
      resize();
      drawFrame();
      start();
    }
  }

  reducedMotion.addEventListener("change", function () {
    stop();
    resize();
    drawFrame();
    if (!reducedMotion.matches) {
      start();
    }
  });

  mqCoarse.addEventListener("change", function () {
    stop();
    resize();
    drawFrame();
    if (!reducedMotion.matches) {
      start();
    }
  });

  window.addEventListener("resize", function () {
    stop();
    resize();
    drawFrame();
    if (!reducedMotion.matches) {
      start();
    }
  });

  document.addEventListener("visibilitychange", onVisibility);

  function boot() {
    resize();
    drawFrame();
    if (w < 32 || h < 32) {
      window.requestAnimationFrame(boot);
      return;
    }
    if (reducedMotion.matches) {
      drawFrame();
      return;
    }
    start();
  }

  window.requestAnimationFrame(function () {
    window.requestAnimationFrame(boot);
  });
})();
