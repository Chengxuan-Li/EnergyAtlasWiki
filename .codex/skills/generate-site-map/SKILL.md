---
name: generate-site-map
description: Use when updating or regenerating the EnergyAtlas Wiki site map page after documentation pages are added, removed, renamed, or reorganized.
---

# Generate Site Map

Regenerate `docs/resources/site-map.md` as an exhaustive map of every Markdown page under `docs/`.

## Output Contract

The generated page must:

- Keep this front matter:

```yaml
---
full_width: true
---
```

- Use `# Site Map` as the page title.
- Include every `docs/**/*.md` file exactly once, including `docs/resources/site-map.md`.
- Follow the folder hierarchy with headings:
  - `## Root` for files directly under `docs/`
  - `## folder-name` for first-level folders
  - `### folder-name/subfolder-name` for nested folders
- Sort folders and pages alphabetically by path.
- Render each page as a plain Markdown link on its own line.
- Do not use bullet points.
- Do not repeat file paths as visible text or inline code.

## Title Extraction

For each Markdown file:

1. Use the first level-one heading (`# Heading`) as the link text.
2. If no level-one heading exists, derive a readable title from the filename.
3. Preserve intentional title punctuation, such as parentheses.

## Link Rules

- Links must be relative from `docs/resources/site-map.md`.
- For files in `docs/resources/`, use links like `faq.md`.
- For files outside `docs/resources/`, use links like `../references/workflows.md`.
- Keep links pointing to Markdown source files, not generated HTML paths.

## Verification

Before finishing, verify:

- Every `docs/**/*.md` file appears exactly once as a site-map link.
- The site map has no bullet-link rows matching `- [Title](path.md)`.
- The site map has no repeated inline-code paths like `` `folder/page.md` ``.
- `mkdocs build` completes. Existing unrelated warnings may remain, but no new site-map link warnings should appear.
