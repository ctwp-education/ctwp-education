document.addEventListener('DOMContentLoaded', () => {
  // Preloader
  const preloader = document.getElementById('preloader');
  window.addEventListener('load', () => setTimeout(() => preloader.classList.add('hidden'), 500));
  setTimeout(() => preloader.classList.add('hidden'), 3000);

  // Navbar scroll
  const navbar = document.getElementById('navbar');
  const backToTop = document.getElementById('backToTop');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
    backToTop.classList.toggle('visible', window.scrollY > 500);
    updateActiveNavLink();
  }, { passive: true });

  // Back to top
  backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  // Active nav link
  function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    let current = '';
    sections.forEach(s => {
      if (window.scrollY >= s.offsetTop - 120) current = s.id;
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });
  }

  // Mobile menu
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });

  document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // Phase Slider with Timeline
  const phaseTrack = document.getElementById('phaseTrack');
  const phasePrev = document.getElementById('phasePrev');
  const phaseNext = document.getElementById('phaseNext');
  const timelineSteps = document.querySelectorAll('.timeline-step');

  if (phaseTrack) {
    const slides = phaseTrack.querySelectorAll('.phase-slide');
    let currentSlide = 3; // Start at Phase 4 (index 3 = active phase)

    // Timeline step clicks
    timelineSteps.forEach(step => {
      step.addEventListener('click', () => {
        goToSlide(parseInt(step.dataset.slide));
      });
    });

    function goToSlide(index) {
      currentSlide = index;
      const slide = slides[0];
      const slideW = slide.offsetWidth;
      const marginL = parseFloat(getComputedStyle(slide).marginLeft) || 0;
      const marginR = parseFloat(getComputedStyle(slide).marginRight) || 0;
      const slotW = slideW + marginL + marginR;
      const vpW = phaseTrack.parentElement.offsetWidth;
      const centerOffset = (vpW - slideW) / 2 - marginL;
      phaseTrack.style.transform = `translateX(${centerOffset - index * slotW}px)`;
      // Update timeline active states
      timelineSteps.forEach((step, i) => {
        step.classList.toggle('active', i === index);
      });
    }

    phasePrev.addEventListener('click', () => {
      goToSlide(currentSlide > 0 ? currentSlide - 1 : slides.length - 1);
    });
    phaseNext.addEventListener('click', () => {
      goToSlide(currentSlide < slides.length - 1 ? currentSlide + 1 : 0);
    });

    // Swipe support
    let touchStartX = 0;
    phaseTrack.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    phaseTrack.addEventListener('touchend', e => {
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        diff > 0 ? phaseNext.click() : phasePrev.click();
      }
    });

    // Initialize
    goToSlide(currentSlide);

    // Re-center on resize
    let phaseRT;
    window.addEventListener('resize', () => {
      clearTimeout(phaseRT);
      phaseRT = setTimeout(() => {
        phaseTrack.style.transition = 'none';
        goToSlide(currentSlide);
        void phaseTrack.offsetWidth;
        phaseTrack.style.transition = '';
      }, 120);
    });
  }

  // Resource tabs
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(`tab-${btn.dataset.tab}`).classList.add('active');
    });
  });

  // Gallery Infinite Circular Slider
  const galleryTrack = document.getElementById('galleryTrack');
  const galleryPrev  = document.getElementById('galleryPrev');
  const galleryNext  = document.getElementById('galleryNext');

  if (galleryTrack) {
    const CLONES = 8, GAP = 16, ANIM = 500;

    // Build clones for infinite loop
    const orig  = [...galleryTrack.children];
    const total = orig.length;
    orig.slice(-CLONES).map(s => s.cloneNode(true))
        .forEach(c => galleryTrack.insertBefore(c, galleryTrack.firstChild));
    orig.slice(0, CLONES).map(s => s.cloneNode(true))
        .forEach(c => galleryTrack.appendChild(c));

    const slides = [...galleryTrack.children];
    let idx  = CLONES;
    let busy = false;

    // Slide unit width
    function W() { return slides[0].offsetWidth + GAP; }

    // Instant no-animation position
    function snap(i) {
      galleryTrack.style.transition = 'none';
      galleryTrack.style.transform  = `translateX(${-i * W()}px)`;
      void galleryTrack.offsetWidth; // flush reflow
    }

    // Animated move — timeout handles infinite-loop correction (no transitionend needed)
    function slide(dir) {
      if (busy) return;
      busy = true;
      idx += dir;
      galleryTrack.style.transition = `transform ${ANIM}ms cubic-bezier(0.4,0,0.2,1)`;
      galleryTrack.style.transform  = `translateX(${-idx * W()}px)`;
      setTimeout(() => {
        if      (idx < CLONES)         { idx += total; snap(idx); }
        else if (idx >= CLONES + total) { idx -= total; snap(idx); }
        busy = false;
      }, ANIM + 20);
    }

    galleryPrev.addEventListener('click', () => slide(-1));
    galleryNext.addEventListener('click', () => slide(1));

    // Touch swipe
    let tx = 0;
    galleryTrack.addEventListener('touchstart', e => { tx = e.touches[0].clientX; }, { passive: true });
    galleryTrack.addEventListener('touchend',   e => {
      const d = tx - e.changedTouches[0].clientX;
      if (Math.abs(d) > 50) slide(d > 0 ? 1 : -1);
    });

    // Auto-slide, pauses on hover
    let auto = null;
    const wrap = galleryTrack.closest('.gallery-slider-wrap');
    function startAuto() { clearInterval(auto); auto = setInterval(() => slide(1), 4000); }
    function stopAuto()  { clearInterval(auto); }
    wrap.addEventListener('mouseenter', stopAuto);
    wrap.addEventListener('mouseleave', () => { if (inited) startAuto(); });

    // Init once slides have real layout width — run exactly once
    let inited = false;
    function tryInit() {
      if (inited) return;
      if (slides[0].offsetWidth > 10) {
        inited = true;
        snap(idx);
        // Delay first auto-slide so it doesn't start immediately on load
        setTimeout(startAuto, 2000);
      } else {
        setTimeout(tryInit, 60);
      }
    }
    tryInit();

    // Re-snap on resize
    let rt;
    window.addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(() => snap(idx), 120); });
  }

  // Scroll animations
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => entry.target.classList.add('visible'), parseInt(delay));
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));

  // Counter animation
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.count);
        const duration = 2000;
        const start = performance.now();
        function update(time) {
          const progress = Math.min((time - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(eased * target).toLocaleString();
          if (progress < 1) requestAnimationFrame(update);
        }
        requestAnimationFrame(update);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-count]').forEach(c => counterObserver.observe(c));

  // Contact form — opens mailto with form data (only on pages that have the form)
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name     = contactForm.querySelector('#name').value;
      const email    = contactForm.querySelector('#email').value;
      const interest = contactForm.querySelector('#interest').value;
      const message  = contactForm.querySelector('#message').value;
      const subject  = encodeURIComponent(`CTWP Contact: ${interest} — ${name}`);
      const body     = encodeURIComponent(`Name: ${name}\nEmail: ${email}\nInterest: ${interest}\n\n${message}`);
      window.location.href = `mailto:ctwp.ee@gmail.com?subject=${subject}&body=${body}`;
    });
  }

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
});
