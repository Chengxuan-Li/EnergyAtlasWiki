(() => {
    const DEFAULT_SUBTITLE_STYLE = 'font-size: 0.85em; color: #9aa0a6;';

    const parseSpec = (raw) => {
        if (!raw) {
            return null;
        }

        const trimmed = raw.trim();
        if (!trimmed) {
            return null;
        }

        if (window.jsyaml) {
            try {
                return window.jsyaml.load(trimmed);
            } catch (error) {
                // Fall back to JSON parsing below.
            }
        }

        try {
            return JSON.parse(trimmed);
        } catch (error) {
            return null;
        }
    };

    const applyTitleAndSubtitle = (spec, layout) => {
        const titleValue = spec.title ?? layout.title ?? '';
        const subtitleValue = spec.subtitle ?? layout.subtitle ?? '';
        const subtitleStyle = spec.subtitle_style ?? DEFAULT_SUBTITLE_STYLE;

        if (!titleValue && !subtitleValue) {
            return;
        }

        let titleText = '';
        if (typeof titleValue === 'string') {
            titleText = titleValue;
        } else if (titleValue && typeof titleValue === 'object') {
            titleText = titleValue.text ?? '';
        }

        if (subtitleValue) {
            layout.title = {
                ...((typeof titleValue === 'object' && titleValue) ? titleValue : {}),
                text: `${titleText}<br><span style="${subtitleStyle}">${subtitleValue}</span>`
            };
        } else if (titleValue) {
            layout.title = titleValue;
        }
    };

    const applyDefaults = (layout) => {
        if (!layout.paper_bgcolor) {
            layout.paper_bgcolor = 'rgba(0,0,0,0)';
        }

        if (!layout.plot_bgcolor) {
            layout.plot_bgcolor = 'rgba(0,0,0,0)';
        }

        const defaultFont = {
            color: '#e5e5e5',
            family: '"Roboto Flex", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
        };

        if (!layout.font) {
            layout.font = { ...defaultFont };
        } else {
            layout.font = { ...defaultFont, ...layout.font };
        }

        const axisDefaults = {
            color: '#e5e5e5',
            gridcolor: 'rgba(255,255,255,0.12)',
            zerolinecolor: 'rgba(255,255,255,0.2)'
        };

        if (!layout.xaxis) {
            layout.xaxis = { ...axisDefaults };
        } else {
            layout.xaxis = { ...axisDefaults, ...layout.xaxis };
        }

        if (!layout.yaxis) {
            layout.yaxis = { ...axisDefaults };
        } else {
            layout.yaxis = { ...axisDefaults, ...layout.yaxis };
        }

        if (!layout.legend) {
            layout.legend = { orientation: 'h', y: -0.2, x: 0, yanchor: 'top' };
        }

        if (!layout.margin) {
            layout.margin = { t: 60, r: 24, b: 72, l: 60 };
        }
    };

    const normalizeLayout = (spec) => {
        const layout = { ...(spec.layout || {}) };

        if (spec.background) {
            layout.paper_bgcolor = spec.background;
            layout.plot_bgcolor = spec.background;
        }

        applyDefaults(layout);
        applyTitleAndSubtitle(spec, layout);

        return layout;
    };

    const normalizeConfig = (spec) => {
        return {
            responsive: true,
            ...(spec.config || {})
        };
    };

    const normalizeData = (spec) => {
        return spec.data || spec.traces || [];
    };

    const findBlocks = () => {
        return document.querySelectorAll(
            'code.language-plotly, code.plotly, code[class*="language-plotly"], code[class*="plotly"], pre.plotly code, div.plotly code'
        );
    };

    const renderPlotlyBlocks = () => {
        if (!window.Plotly) {
            return false;
        }

        const blocks = findBlocks();
        blocks.forEach((codeBlock, index) => {
            const spec = parseSpec(codeBlock.textContent);
            if (!spec) {
                return;
            }

            const pre = codeBlock.closest('pre');

            const container = document.createElement('div');
            container.className = 'plotly-chart';
            container.dataset.plotlyIndex = String(index);

            if (spec.id) {
                container.id = spec.id;
            }

            if (spec.height) {
                const heightValue = typeof spec.height === 'number' ? `${spec.height}px` : spec.height;
                container.style.height = heightValue;
            }

            if (spec.width) {
                const widthValue = typeof spec.width === 'number' ? `${spec.width}px` : spec.width;
                container.style.width = widthValue;
            }

            if (pre) {
                pre.replaceWith(container);
            } else {
                codeBlock.replaceWith(container);
            }

            const data = normalizeData(spec);
            const layout = normalizeLayout(spec);
            const config = normalizeConfig(spec);

            window.Plotly.newPlot(container, data, layout, config);
        });

        return true;
    };

    const renderPlaygrounds = () => {
        if (!window.Plotly) {
            return false;
        }

        const playgrounds = document.querySelectorAll('[data-plotly-playground]');
        if (!playgrounds.length) {
            return true;
        }

        playgrounds.forEach((container) => {
            if (container.dataset.plotlyInitialized === 'true') {
                return;
            }

            const initial = container.querySelector('textarea');
            const output = container.querySelector('.plotly-playground-chart');
            const error = container.querySelector('.plotly-playground-error');

            if (!initial || !output) {
                return;
            }

            const renderSpec = (raw) => {
                const spec = parseSpec(raw);
                if (!spec) {
                    if (error) {
                        error.textContent = 'Invalid JSON. Fix the syntax to render.';
                    }
                    return;
                }

                if (error) {
                    error.textContent = '';
                }

                const data = normalizeData(spec);
                const layout = normalizeLayout(spec);
                const config = normalizeConfig(spec);
                window.Plotly.newPlot(output, data, layout, config);
            };

            renderSpec(initial.value);

            initial.addEventListener('input', () => renderSpec(initial.value));
            container.dataset.plotlyInitialized = 'true';
        });

        return true;
    };

    const attemptRender = (tries = 0) => {
        const success = renderPlotlyBlocks() && renderPlaygrounds();
        if (success || tries >= 5) {
            return;
        }
        setTimeout(() => attemptRender(tries + 1), 200);
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => attemptRender());
    } else {
        attemptRender();
    }

    window.addEventListener('load', () => attemptRender());
})();
