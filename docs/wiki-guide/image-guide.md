# Image Guide for EnergyAtlas Wiki

## Best Practices

### 1. **Where to Store Images**

Place images in `docs/assets/images/` directory:
```
docs/
  assets/
    images/
      screenshot-1.png
      diagram.svg
      logo.png
```

### 2. **Basic Image Syntax**

Standard markdown image:
```markdown
![Alt text](assets/images/image.png)
```

### 3. **Image Sizing Classes**

Use CSS classes for sizing:

```markdown
![Small image](assets/images/image.png){.small}
![Medium image](assets/images/image.png){.medium}
![Large image](assets/images/image.png){.large}
![Full width](assets/images/image.png){.full-width}
```

### 4. **Image Alignment**

Float images left or right:
```markdown
![Left aligned](assets/images/image.png){.float-left}
![Right aligned](assets/images/image.png){.float-right}
```

### 5. **Image with Caption**

Using HTML for better control:
```html
<div class="image-container">
  <img src="assets/images/image.png" alt="Description" />
  <p>Caption text here</p>
</div>
```

Or using markdown with emphasis:
```markdown
![Description](assets/images/image.png)

*Caption text here*
```

### 6. **External Images**

External images work the same way:
```markdown
![External image](https://example.com/image.jpg)
```

### 7. **Image Styling Features**

- **Automatic centering**: Images in paragraphs are centered
- **Borders**: All images have subtle borders
- **Responsive**: Images scale down on smaller screens
- **Rounded corners**: Images have border-radius

### 8. **Examples**

**Centered medium image:**
```markdown
![EnergyAtlas Dashboard](assets/images/dashboard.png){.medium}
```

**Left-aligned thumbnail:**
```markdown
![Icon](assets/images/icon.svg){.small .float-left}
```

**Full-width hero image:**
```markdown
![Hero Image](assets/images/hero.jpg){.full-width}
```

**Image with caption:**
```html
<div class="image-container">
  <img src="assets/images/diagram.svg" alt="Process diagram" />
  <p>Figure 1: Energy modeling workflow</p>
</div>
```

## Tips

1. **Optimize images**: Use compressed formats (WebP, optimized PNG/JPG)
2. **Descriptive alt text**: Always include meaningful alt text
3. **Consistent naming**: Use descriptive, lowercase filenames with hyphens
4. **SVG for icons**: Use SVG for logos and icons (scalable, small file size)
5. **PNG for screenshots**: Use PNG for screenshots with text
6. **JPG for photos**: Use JPG for photographs
