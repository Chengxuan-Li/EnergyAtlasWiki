(() => {
    const STORAGE_KEY = 'energyatlas-wiki-theme';
    const CHANGE_EVENT = 'energyatlas-theme-change';
    const THEMES = ['dark', 'light'];

    const normalizeTheme = (theme) => THEMES.includes(theme) ? theme : 'dark';

    const getStoredTheme = () => {
        try {
            return normalizeTheme(window.localStorage.getItem(STORAGE_KEY));
        } catch (error) {
            return 'dark';
        }
    };

    const getCurrentTheme = () => {
        return normalizeTheme(document.documentElement.dataset.theme || getStoredTheme());
    };

    const updateToggle = (theme) => {
        const toggle = document.getElementById('wiki-theme-toggle');
        if (!toggle) {
            return;
        }

        const isLight = theme === 'light';
        const nextTheme = isLight ? 'dark' : 'light';

        toggle.setAttribute('aria-pressed', String(isLight));
        toggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
        toggle.setAttribute('title', `Switch to ${nextTheme} theme`);
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

    window.EnergyAtlasTheme = {
        getTheme: getCurrentTheme,
        setTheme: (theme) => applyTheme(theme, true)
    };

    document.addEventListener('DOMContentLoaded', () => {
        applyTheme(getCurrentTheme(), false);

        const toggle = document.getElementById('wiki-theme-toggle');
        if (!toggle) {
            return;
        }

        toggle.addEventListener('click', () => {
            const nextTheme = getCurrentTheme() === 'light' ? 'dark' : 'light';
            applyTheme(nextTheme, true);
        });
    });
})();
