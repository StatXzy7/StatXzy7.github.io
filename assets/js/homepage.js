(() => {
  const navigationLinks = [...document.querySelectorAll('.home-nav a[href^="#"]')];
  const sections = navigationLinks.map(link => document.querySelector(link.hash)).filter(Boolean);

  if ('IntersectionObserver' in window) {
    const visibleSections = new Set();
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) visibleSections.add(entry.target);
        else visibleSections.delete(entry.target);
      });
      const activeSection = sections.find(section => visibleSections.has(section));
      navigationLinks.forEach(link => {
        if (activeSection && link.hash === `#${activeSection.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, {rootMargin: '-96px 0px -55% 0px'});
    sections.forEach(section => observer.observe(section));
  }

  const visitorStats = document.querySelector('.visitor-stats');
  const visitorMap = document.querySelector('#visitor-map');
  if (visitorStats && visitorMap) {
    visitorStats.addEventListener('toggle', () => {
      if (!visitorStats.open || visitorMap.dataset.loaded) return;
      visitorMap.dataset.loaded = 'true';
      const script = document.createElement('script');
      script.id = 'clustrmaps';
      script.src = visitorMap.dataset.mapSrc;
      script.async = true;
      visitorMap.append(script);
    });
  }
})();
