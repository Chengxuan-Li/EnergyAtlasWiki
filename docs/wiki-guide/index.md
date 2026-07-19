# Wiki Guide

Guide for contributing to and maintaining the EnergyAtlas Wiki.

## Overview

This guide helps contributors understand how to create, edit, and maintain documentation in the EnergyAtlas Wiki. It covers markdown syntax, formatting guidelines, and best practices.

## Getting Started

### Accessing the Wiki

1. Navigate to the wiki repository
2. Clone or fork the repository
3. Make changes locally
4. Submit pull request or push changes

### Editing Pages

1. Find the page to edit
2. Click "Edit on GitHub" (top ribbon)
3. Make changes in markdown
4. Preview changes
5. Commit changes

## Markdown Basics

### Headings

```markdown
# Level 1 Heading
## Level 2 Heading
### Level 3 Heading
#### Level 4 Heading
```

### Text Formatting

```markdown
**Bold text**
*Italic text*
`Code text`
```

### Lists

**Unordered**:
```markdown
- Item 1
- Item 2
  - Sub-item
```

**Ordered**:
```markdown
1. First item
2. Second item
3. Third item
```

### Links

```markdown
[Link text](path/to/page.md)
[External link](https://example.com)
```

### Images

```markdown
![Alt text](path/to/image.png)
![Image with classes](path/to/image.png){.medium .float-left}
```

### Code Blocks

````markdown
```python
def example():
    return "Hello"
```
````

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Math Formulas

```markdown
Inline: \(E = mc^2\)

Block:
$$
E = mc^2
$$
```

## Content Guidelines

### Writing Style

- **Clear and concise**: Use simple, direct language
- **Structured**: Use headings and lists for organization
- **Examples**: Include practical examples
- **Links**: Link to related pages
- **Images**: Use images to illustrate concepts

### Page Structure

1. **Title**: Clear, descriptive heading
2. **Overview**: Brief introduction
3. **Sections**: Organized by topic
4. **Examples**: Practical examples
5. **References**: Links to related pages

### Documentation Standards

- **Consistency**: Use consistent terminology
- **Completeness**: Cover all important aspects
- **Accuracy**: Verify technical information
- **Updates**: Keep content current
- **Clarity**: Explain concepts clearly

## Adding New Pages

### Create New File

1. Navigate to appropriate directory
2. Create new `.md` file
3. Use descriptive filename
4. Start with heading

### Update Navigation

1. Edit `mkdocs.yml`
2. Add page to `nav` section
3. Use correct path
4. Save changes

### Add Content

1. Write page content
2. Use proper markdown syntax
3. Include examples
4. Add links to related pages
5. Review and edit

## Editing Existing Pages

### Making Changes

1. Locate page to edit
2. Click "Edit on GitHub"
3. Make changes
4. Preview if possible
5. Commit changes

### Updating Content

- **Fix errors**: Correct mistakes
- **Add information**: Expand content
- **Update examples**: Refresh outdated examples
- **Improve clarity**: Enhance explanations
- **Add links**: Connect related content

## Image Guidelines

### Adding Images

1. Place images in `docs/assets/images/`
2. Use descriptive filenames
3. Reference in markdown: `![Alt text](assets/images/image.png)`
4. Add sizing classes if needed: `{.medium}`

**See**: [Image Guide](image-guide.md) for detailed image usage instructions.

### Image Best Practices

- **Optimize**: Compress images for web
- **Descriptive alt text**: Always include alt text
- **Appropriate size**: Use sizing classes
- **Consistent style**: Maintain visual consistency
- **Relevant**: Images should support content

### When to Use Charts vs Images

- **Use Plotly charts** for:
  - Data visualization
  - Interactive exploration
  - Dynamic data updates
  - Multiple series comparisons

- **Use static images** for:
  - Screenshots
  - Diagrams
  - Photos
  - Static illustrations

**See**: [Plotting Guide](plotting-guide.md) for creating charts.

## Formatting Guidelines

### Headings

- Use H1 for page title only
- Use H2 for main sections
- Use H3 for subsections
- Maintain hierarchy

### Code Examples

- Use code blocks for code
- Specify language when possible
- Include comments for clarity
- Keep examples simple

### Tables

- Use tables for structured data
- Keep tables simple
- Include headers
- Align columns appropriately

## Best Practices

### Content Quality

1. **Accuracy**: Verify all information
2. **Completeness**: Cover topics thoroughly
3. **Clarity**: Write clearly and simply
4. **Examples**: Include practical examples
5. **Links**: Connect related content

### Maintenance

1. **Regular updates**: Keep content current
2. **Fix errors**: Correct mistakes promptly
3. **Improve clarity**: Enhance explanations
4. **Add examples**: Include more examples
5. **Update links**: Fix broken links

### Collaboration

1. **Review changes**: Review before committing
2. **Discuss major changes**: Coordinate large edits
3. **Follow style guide**: Maintain consistency
4. **Document decisions**: Explain major changes
5. **Be respectful**: Maintain professional tone

## Common Tasks

### Adding a New Section

1. Find appropriate location
2. Add heading
3. Write content
4. Add examples
5. Link to related pages

### Updating Navigation

1. Edit `mkdocs.yml`
2. Add or modify nav entry
3. Use correct file path
4. Test navigation

### Fixing Broken Links

1. Identify broken link
2. Find correct path
3. Update link
4. Verify link works

## Adding Charts and Plots

### Plotly Charts

EnergyAtlas Wiki supports interactive Plotly charts for data visualization.

**Quick Start**:
- **[Plotting Guide](plotting-guide.md)** - Complete guide to creating charts
- **[Plotting Playground](plotting-playground.md)** - Interactive testing environment

### Basic Usage

Use Plotly JSON format in code blocks:

````markdown
```plotly
{
  "data": [{
    "type": "scatter",
    "mode": "lines+markers",
    "x": [1, 2, 3, 4],
    "y": [10, 15, 13, 17]
  }],
  "layout": {
    "title": "Example Chart"
  }
}
```
````

### Chart Types

Supported chart types include:
- Line charts (multi-series)
- Bar charts (stacked, grouped)
- Pie and donut charts
- Scatter plots

**See**: [Plotting Guide](plotting-guide.md) for detailed examples and customization options.

## Resources

### Documentation

- [Image Guide](image-guide.md) - Image usage guide
- [Plotting Guide](plotting-guide.md) - Creating interactive charts and plots
- [Plotting Playground](plotting-playground.md) - Test and experiment with charts
- [MkDocs Documentation](https://www.mkdocs.org/) - MkDocs reference
- [Markdown Guide](https://www.markdownguide.org/) - Markdown syntax

### Tools

- **Markdown editors**: Use markdown-aware editors
- **Preview**: Preview changes before committing
- **Validators**: Check markdown syntax
- **Link checkers**: Verify links work

## Getting Help

### Questions

- Check existing documentation
- Review similar pages
- Ask in discussions
- Contact maintainers

### Issues

- Report bugs
- Suggest improvements
- Request features
- Provide feedback

## Contributing

### Process

1. **Fork repository**: Create your own copy
2. **Make changes**: Edit files
3. **Test locally**: Preview changes
4. **Submit pull request**: Propose changes
5. **Review feedback**: Address comments

### Guidelines

- Follow style guide
- Write clear commit messages
- Test changes locally
- Update related pages if needed
- Be patient with reviews

## References

- [Image Guide](image-guide.md) - Image usage and styling
- [Plotting Guide](plotting-guide.md) - Creating interactive charts and visualizations
- [Plotting Playground](plotting-playground.md) - Interactive chart testing environment
- [MkDocs User Guide](https://www.mkdocs.org/user-guide/) - MkDocs documentation
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) - Quick reference
