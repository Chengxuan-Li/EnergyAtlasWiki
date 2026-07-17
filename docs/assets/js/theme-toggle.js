(() => {
    const STORAGE_KEY = 'energyatlas-wiki-theme';
    const CHANGE_EVENT = 'energyatlas-theme-change';
    const THEMES = ['dark', 'light'];
    const SYSTEM_THEME_QUERY = window.matchMedia('(prefers-color-scheme: dark)');

    const normalizeTheme = (theme) => THEMES.includes(theme) ? theme : 'dark';

    const getSystemTheme = () => SYSTEM_THEME_QUERY.matches ? 'dark' : 'light';

    const getStoredTheme = () => {
        try {
            const storedTheme = window.localStorage.getItem(STORAGE_KEY);
            return THEMES.includes(storedTheme) ? storedTheme : null;
        } catch (error) {
            return null;
        }
    };

    const getCurrentTheme = () => {
        return normalizeTheme(document.documentElement.dataset.theme || getStoredTheme() || getSystemTheme());
    };

    const updateToggle = (theme) => {
        const toggle = document.getElementById('wiki-theme-toggle');
        if (!toggle) {
            return;
        }

        const isLight = theme === 'light';
        const nextTheme = isLight ? 'dark' : 'light';

        toggle.dataset.theme = theme;
        toggle.setAttribute('aria-pressed', String(isLight));
        toggle.setAttribute('aria-label', `Switch to ${nextTheme} mode`);
        toggle.setAttribute('title', `Switch to ${nextTheme} mode`);
    };

    const applyTheme = (theme, persist) => {
        const normalizedTheme = normalizeTheme(theme);

        document.documentElement.dataset.theme = normalizedTheme;
        document.documentElement.style.colorScheme = normalizedTheme;
        updateToggle(normalizedTheme);

        if (persist) {
            try {
                window.localStorage.setItem(STORAGE_KEY, normalizedTheme);
            } catch (error) {}
        }

        window.dispatchEvent(new CustomEvent(CHANGE_EVENT, {
            detail: { theme: normalizedTheme }
        }));
    };

    const syncThemeWithSystem = () => {
        if (!getStoredTheme()) {
            applyTheme(getSystemTheme(), false);
        }
    };

    window.EnergyAtlasTheme = {
        getTheme: getCurrentTheme,
        setTheme: (theme) => applyTheme(theme, true)
    };

    document.addEventListener('DOMContentLoaded', () => {
        applyTheme(getStoredTheme() || getSystemTheme(), false);

        const toggle = document.getElementById('wiki-theme-toggle');
        if (!toggle) {
            return;
        }

        toggle.addEventListener('click', () => {
            const nextTheme = getCurrentTheme() === 'light' ? 'dark' : 'light';
            applyTheme(nextTheme, true);
        });

        if (typeof SYSTEM_THEME_QUERY.addEventListener === 'function') {
            SYSTEM_THEME_QUERY.addEventListener('change', syncThemeWithSystem);
        } else if (typeof SYSTEM_THEME_QUERY.addListener === 'function') {
            SYSTEM_THEME_QUERY.addListener(syncThemeWithSystem);
        }
    });
})();
