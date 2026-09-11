/**
 * Bridges the live LikeC4 viewer to the Wiki shell.
 *
 * <likec4-view> renders into a shadow root and observes `color-scheme`, so the only wiring it
 * needs is a theme value on load and on every theme change. Setting the attribute fires the
 * element's own attributeChangedCallback, which re-renders in place.
 *
 * Sizing is entirely CSS: the element carries its view's aspect ratio, and .likec4-figure
 * gives it a floor width and a scroller on narrow viewports.
 *
 * Loaded by theme/base.html on pages whose front matter sets `likec4: true`.
 */
(() => {
    const VIEW_SELECTOR = 'likec4-view';
    const THEME_CHANGE_EVENT = 'energyatlas-theme-change';

    const currentTheme = () => {
        if (window.EnergyAtlasTheme && typeof window.EnergyAtlasTheme.getTheme === 'function') {
            return window.EnergyAtlasTheme.getTheme();
        }
        return document.documentElement.dataset.theme === 'light' ? 'light' : 'dark';
    };

    const applyTheme = (theme) => {
        document.querySelectorAll(VIEW_SELECTOR).forEach((view) => {
            // Skip no-op writes so a theme event does not churn an already-correct view.
            if (view.getAttribute('color-scheme') !== theme) {
                view.setAttribute('color-scheme', theme);
            }
        });
    };

    const start = () => {
        if (!document.querySelector(VIEW_SELECTOR)) {
            return;
        }

        applyTheme(currentTheme());

        window.addEventListener(THEME_CHANGE_EVENT, (event) => {
            applyTheme((event.detail && event.detail.theme) || currentTheme());
        });
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
})();
