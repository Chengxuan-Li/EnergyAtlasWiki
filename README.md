# EnergyAtlas Wiki

A documentation wiki built with MkDocs, styled to match the EnergyAtlas design system.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure assets are in docs directory:**
   The `assets` folder must exist in the `docs/` directory for MkDocs to find CSS and images.
   If you make changes to files in the root `assets/` folder, copy them to `docs/assets/`.

3. **Serve locally:**
   ```bash
   mkdocs serve
   ```
   The wiki will be available at `http://127.0.0.1:8000`
   
   **Note:** If CSS is not loading:
   - Stop the server (Ctrl+C) and restart it
   - Hard refresh your browser (Ctrl+F5)
   - Check browser console for 404 errors on CSS files

4. **Build static site:**
   ```bash
   mkdocs build
   ```
   The static site will be generated in the `site/` directory.

## Project Structure

```
.
├── docs/                    # Documentation source files (Markdown)
│   ├── index.md            # Home page
│   ├── getting-started/   # Getting started guides
│   ├── core-topics/        # Core topic documentation
│   └── resources/          # Resources and references
├── assets/                  # Static assets (CSS, images)
│   ├── css/
│   │   ├── main.css        # Main stylesheet (EnergyAtlas design system)
│   │   └── statusBar.css   # Status bar styles
│   └── images/             # Images and icons
├── theme/                  # Custom MkDocs theme
│   ├── base.html          # Base template
│   └── main.html          # Main content template
├── mkdocs.yml             # MkDocs configuration
└── requirements.txt        # Python dependencies
```

## Design

The wiki uses a custom theme that matches the EnergyAtlas design system:

- **Dark theme** with EnergyAtlas color palette
- **Two-column layout**: Navigation sidebar + main content
- **Card-based content** sections
- **Roboto Flex** typography
- **Responsive design** for mobile and desktop

## Customization

### Adding Pages

1. Create a new Markdown file in the appropriate `docs/` subdirectory
2. Add the page to `mkdocs.yml` in the `nav` section
3. The page will automatically appear in the navigation

### Styling

- Main styles: `assets/css/main.css`
- Theme templates: `theme/base.html` and `theme/main.html`
- CSS variables are defined in `main.css` for easy customization

### Content Structure

Pages can be structured with markdown headers. The theme will automatically style:
- Headings (h1-h6)
- Links
- Code blocks
- Tables
- Lists
- Blockquotes

## Development

### Live Reload

When running `mkdocs serve`, the site will automatically reload when you make changes to:
- Markdown files in `docs/`
- Theme templates in `theme/`
- CSS files in `assets/css/`
- Configuration in `mkdocs.yml`

### Building for Production

```bash
mkdocs build
```

The static site will be in the `site/` directory, ready to deploy to any static hosting service.

## License

[Add your license here]
