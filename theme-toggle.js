(function(){
  const THEME_KEY = 'site-theme';
  const btn = document.querySelector('.theme-toggle');
  const root = document.documentElement;

  const ICONS = {
    moon: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" fill="currentColor"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M6.76 4.84l-1.8-1.79-1.41 1.41 1.79 1.8 1.42-1.42zM1 13h3v-2H1v2zm10 9h2v-3h-2v3zM20.24 4.84l1.79 1.8 1.41-1.41-1.8-1.79-1.4 1.4zM17 11v2h3v-2h-3zM4.22 19.78l1.41-1.41-1.8-1.79-1.41 1.41 1.8 1.79zM12 6a6 6 0 100 12A6 6 0 0012 6zM19.78 19.78l-1.79-1.8-1.41 1.41 1.8 1.79 1.4-1.4z" fill="currentColor"/></svg>'
  };

  function setButtonIcon(theme){
    if(!btn) return;
    if(theme === 'dark'){
      btn.innerHTML = ICONS.sun;
      btn.setAttribute('aria-pressed','true');
      btn.setAttribute('title','Basculer en thème clair');
    } else {
      btn.innerHTML = ICONS.moon;
      btn.setAttribute('aria-pressed','false');
      btn.setAttribute('title','Basculer en thème sombre');
    }
  }

  function applyTheme(theme){
    if(theme === 'dark'){
      root.setAttribute('data-theme','dark');
    } else {
      root.removeAttribute('data-theme');
    }
    setButtonIcon(theme);
  }

  const saved = localStorage.getItem(THEME_KEY);
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  let theme = saved || (prefersDark ? 'dark' : 'light');
  applyTheme(theme);

  if(btn){
    btn.addEventListener('click', function(){
      theme = (theme === 'dark') ? 'light' : 'dark';
      localStorage.setItem(THEME_KEY, theme);
      applyTheme(theme);
    });
    // keyboard accessibility: allow Space/Enter to toggle
    btn.addEventListener('keydown', function(e){
      if(e.key === ' ' || e.key === 'Enter'){
        e.preventDefault();
        btn.click();
      }
    });
  }
})();
