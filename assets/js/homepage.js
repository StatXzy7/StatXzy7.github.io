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

  const researchSection = document.querySelector('.research-section');
  if (researchSection) {
    const filters = researchSection.querySelector('.research-filters');
    const buttons = [...researchSection.querySelectorAll('[data-research-filter]')];
    const papers = [...researchSection.querySelectorAll('[data-paper-topics]')];
    const status = researchSection.querySelector('.research-filter-status');
    const topics = new Map(papers.map(paper => [paper, new Set(paper.dataset.paperTopics.split(/\s+/))]));
    const matches = (paper, topic) => topic === 'all' || topics.get(paper).has(topic);

    if (filters && buttons.length && papers.length) {
      const selectTopic = selectedButton => {
        const topic = selectedButton.dataset.researchFilter;
        let visibleCount = 0;
        papers.forEach(paper => {
          paper.hidden = !matches(paper, topic);
          if (!paper.hidden) visibleCount += 1;
        });
        buttons.forEach(button => button.setAttribute('aria-pressed', String(button === selectedButton)));
        if (status) {
          const label = selectedButton.childNodes[0].textContent.trim();
          status.textContent = topic === 'all'
            ? `Showing all ${visibleCount} publications.`
            : `${label}: ${visibleCount} of ${papers.length} publications shown.`;
        }
      };

      buttons.forEach(button => {
        const count = button.querySelector('.filter-count');
        if (count) count.textContent = papers.filter(paper => matches(paper, button.dataset.researchFilter)).length;
        button.addEventListener('click', () => selectTopic(button));
      });
      selectTopic(buttons.find(button => button.dataset.researchFilter === 'all') || buttons[0]);
      filters.hidden = false;
    }
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
