(() => {
    const DESKTOP_QUERY = window.matchMedia('(min-width: 1081px)');

    document.addEventListener('DOMContentLoaded', () => {
        const body = document.body;
        const sidebar = document.getElementById('wiki-sidebar');
        const openButton = document.getElementById('wiki-sidebar-toggle');
        const closeButton = document.getElementById('wiki-sidebar-close');
        const scrim = document.getElementById('wiki-sidebar-scrim');
        const spaceSwitcher = document.getElementById('wiki-space-switcher');

        if (!sidebar || !openButton || !closeButton || !scrim) {
            return;
        }

        const focusableSelector = [
            'a[href]',
            'button:not([disabled])',
            'summary',
            '[tabindex]:not([tabindex="-1"])'
        ].join(',');

        const isDrawerOpen = () => body.classList.contains('wiki-sidebar-open');

        const setSidebarAvailable = (available) => {
            if (available) {
                sidebar.removeAttribute('inert');
                sidebar.removeAttribute('aria-hidden');
            } else {
                sidebar.setAttribute('inert', '');
                sidebar.setAttribute('aria-hidden', 'true');
            }
        };

        const openDrawer = () => {
            setSidebarAvailable(true);
            body.classList.add('wiki-sidebar-open');
            scrim.hidden = false;
            openButton.setAttribute('aria-expanded', 'true');
            closeButton.focus();
        };

        const closeDrawer = (restoreFocus = true) => {
            body.classList.remove('wiki-sidebar-open');
            scrim.hidden = true;
            openButton.setAttribute('aria-expanded', 'false');

            if (restoreFocus && !DESKTOP_QUERY.matches) {
                openButton.focus();
            }

            setSidebarAvailable(DESKTOP_QUERY.matches);
        };

        openButton.addEventListener('click', openDrawer);
        closeButton.addEventListener('click', () => closeDrawer());
        scrim.addEventListener('click', () => closeDrawer());

        sidebar.querySelectorAll('a[href]').forEach((link) => {
            link.addEventListener('click', () => {
                if (!DESKTOP_QUERY.matches) {
                    closeDrawer(false);
                }
            });
        });

        document.addEventListener('click', (event) => {
            if (spaceSwitcher && spaceSwitcher.open && !spaceSwitcher.contains(event.target)) {
                spaceSwitcher.open = false;
            }
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') {
                if (spaceSwitcher && spaceSwitcher.open) {
                    spaceSwitcher.open = false;
                    spaceSwitcher.querySelector('summary')?.focus();
                    return;
                }

                if (isDrawerOpen()) {
                    closeDrawer();
                }
                return;
            }

            if (event.key !== 'Tab' || !isDrawerOpen() || DESKTOP_QUERY.matches) {
                return;
            }

            const focusable = Array.from(sidebar.querySelectorAll(focusableSelector))
                .filter((element) => !element.hasAttribute('hidden') && element.offsetParent !== null);

            if (!focusable.length) {
                return;
            }

            const first = focusable[0];
            const last = focusable[focusable.length - 1];

            if (event.shiftKey && document.activeElement === first) {
                event.preventDefault();
                last.focus();
            } else if (!event.shiftKey && document.activeElement === last) {
                event.preventDefault();
                first.focus();
            }
        });

        const handleViewportChange = (event) => {
            if (event.matches) {
                closeDrawer(false);
            }
        };

        if (typeof DESKTOP_QUERY.addEventListener === 'function') {
            DESKTOP_QUERY.addEventListener('change', handleViewportChange);
        } else {
            DESKTOP_QUERY.addListener(handleViewportChange);
        }

        closeDrawer(false);
    });
})();
