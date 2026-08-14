// Shifter /locations landing page clone — vanilla JS interactivity
// (mobile menu, accordion submenus, country search filter)

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initMobileAccordions();
  initDesktopDropdowns();
  initCountrySearch();
  initRoutingCityCycle();
});

function initMobileMenu() {
  const toggle = document.getElementById('mobile-menu-toggle');
  const panel = document.getElementById('mobile-menu-panel');
  if (!toggle || !panel) return;

  const open = () => {
    toggle.setAttribute('aria-expanded', 'true');
    panel.removeAttribute('inert');
    panel.classList.remove('opacity-0', '-translate-y-2', 'pointer-events-none');
    panel.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
  };

  const close = () => {
    toggle.setAttribute('aria-expanded', 'false');
    panel.setAttribute('inert', '');
    panel.classList.add('opacity-0', '-translate-y-2', 'pointer-events-none');
    panel.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
  };

  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    isOpen ? close() : open();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') close();
  });

  document.addEventListener('click', (e) => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    if (isOpen && !panel.contains(e.target) && !toggle.contains(e.target)) close();
  });
}

function initMobileAccordions() {
  const triggers = document.querySelectorAll('[data-accordion-toggle]');

  triggers.forEach((trigger) => {
    const key = trigger.getAttribute('data-accordion-toggle');
    const contentPanel = document.querySelector(`[data-accordion-panel="${key}"]`);
    const chevron = trigger.querySelector('svg');
    if (!contentPanel) return;

    trigger.addEventListener('click', () => {
      const isOpen = trigger.getAttribute('aria-expanded') === 'true';

      if (isOpen) {
        trigger.setAttribute('aria-expanded', 'false');
        contentPanel.style.gridTemplateRows = '0fr';
        contentPanel.classList.remove('opacity-100');
        contentPanel.classList.add('opacity-0');
        if (chevron) chevron.classList.remove('rotate-180');
      } else {
        trigger.setAttribute('aria-expanded', 'true');
        contentPanel.style.gridTemplateRows = '1fr';
        contentPanel.classList.remove('opacity-0');
        contentPanel.classList.add('opacity-100');
        if (chevron) chevron.classList.add('rotate-180');
      }
    });
  });
}

function initDesktopDropdowns() {
  const triggers = document.querySelectorAll('[data-dropdown-toggle]');
  if (!triggers.length) return;

  const panelFor = (trigger) => {
    const key = trigger.getAttribute('data-dropdown-toggle');
    return document.querySelector(`[data-dropdown-panel="${key}"]`);
  };

  const closeAll = () => {
    triggers.forEach((trigger) => {
      const panel = panelFor(trigger);
      const chevron = trigger.querySelector('svg');
      trigger.setAttribute('aria-expanded', 'false');
      if (panel) panel.classList.remove('open');
      if (chevron) chevron.classList.remove('nav-chevron-rotate');
    });
  };

  triggers.forEach((trigger) => {
    const panel = panelFor(trigger);
    const chevron = trigger.querySelector('svg');
    if (!panel) return;

    trigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = trigger.getAttribute('aria-expanded') === 'true';
      closeAll();
      if (!isOpen) {
        trigger.setAttribute('aria-expanded', 'true');
        panel.classList.add('open');
        if (chevron) chevron.classList.add('nav-chevron-rotate');
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAll();
  });

  document.addEventListener('click', (e) => {
    const insideAny = Array.from(triggers).some(
      (trigger) => trigger.contains(e.target) || panelFor(trigger)?.contains(e.target)
    );
    if (!insideAny) closeAll();
  });
}

function initRoutingCityCycle() {
  const cityEl = document.getElementById('routing-city');
  if (!cityEl) return;

  const latencyEl = document.getElementById('routing-latency');
  const nextEl = document.getElementById('routing-next-cities');

  const cities = [
    'Kabul', 'Kandahar', 'Herat', 'Mazar-i-Sharif', 'Kunduz',
    'Jalalabad', 'Lashkar Gah', 'Taloqan', 'Pul-e-Khumri', 'Khost'
  ];
  let index = 0;

  const renderNext = () => {
    if (!nextEl) return;
    const upcoming = [1, 2, 3, 4].map((offset) => cities[(index + offset) % cities.length]);
    nextEl.textContent = upcoming.join('  >  ');
  };

  renderNext();

  setInterval(() => {
    index = (index + 1) % cities.length;
    cityEl.style.opacity = '0';
    if (latencyEl) latencyEl.style.opacity = '0';
    if (nextEl) nextEl.style.opacity = '0';

    setTimeout(() => {
      cityEl.textContent = cities[index];
      cityEl.style.opacity = '1';
      if (latencyEl) {
        latencyEl.textContent = `${28 + Math.floor(Math.random() * 60)} ms`;
        latencyEl.style.opacity = '1';
      }
      renderNext();
      if (nextEl) nextEl.style.opacity = '1';
    }, 250);
  }, 2400);
}

function initCountrySearch() {
  const input = document.getElementById('country-search');
  if (!input) return;

  const regionBlocks = Array.from(document.querySelectorAll('h2'))
    .map((heading) => {
      const headerRow = heading.parentElement;
      const grid = headerRow ? headerRow.nextElementSibling : null;
      const wrapper = headerRow ? headerRow.parentElement : null;
      const countBadge = headerRow ? headerRow.querySelector('span') : null;
      return { grid, wrapper, countBadge };
    })
    .filter(({ grid }) => grid && grid.querySelector('a[href^="/location/"]'));

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();

    regionBlocks.forEach(({ grid, wrapper, countBadge }) => {
      let visible = 0;

      grid.querySelectorAll('a').forEach((link) => {
        const name = link.textContent.trim().toLowerCase();
        const matches = !query || name.includes(query);
        link.style.display = matches ? '' : 'none';
        if (matches) visible += 1;
      });

      if (wrapper) wrapper.style.display = visible === 0 ? 'none' : '';
      if (countBadge) countBadge.textContent = String(visible);
    });
  });
}
