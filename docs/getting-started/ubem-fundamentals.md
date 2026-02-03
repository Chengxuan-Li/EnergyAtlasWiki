# UBEM Fundamentals

Understanding the fundamentals of Urban Building Energy Modeling (UBEM) is essential for effective use of EnergyAtlas.

## What is UBEM?

Urban Building Energy Modeling (UBEM) is the process of modeling energy consumption and demand for groups of buildings at the urban or district scale. Unlike single-building models, UBEM approaches:

- Model multiple buildings simultaneously
- Use simplified archetype-based approaches for efficiency
- Integrate diverse data sources (GIS, building permits, surveys)
- Enable scenario analysis for policy and planning

## Key Concepts

### Building Archetypes

Archetypes are representative building models that capture the essential characteristics of a building class. Common archetype dimensions include:

- **Building Type**: Residential, commercial, mixed-use
- **Vintage**: Construction era (pre-1980, 1980-2000, post-2000)
- **Size**: Small, medium, large
- **Occupancy**: Single-family, multi-family, office, retail

### Data Integration

UBEM requires integrating multiple data sources:

- **Geographic Data**: Building footprints, locations, heights
- **Building Characteristics**: Age, type, size, use
- **Energy Data**: Consumption records, utility data
- **Weather Data**: Climate files for simulation

### Simulation Approaches

EnergyAtlas supports multiple simulation approaches:

- **Simplified Models**: Fast, suitable for large-scale analysis
- **Detailed Models**: More accurate, computationally intensive
- **Hybrid Approaches**: Balance between speed and accuracy

## Best Practices

1. **Start Simple**: Begin with basic archetypes and refine as needed
2. **Validate Results**: Compare model outputs with measured data
3. **Document Assumptions**: Keep track of modeling assumptions and data sources
4. **Iterate**: Refine models based on validation results

## Next Steps

Now that you understand UBEM fundamentals:

- **[Build Your First UBEM](first-ubem.md)** - Step-by-step tutorial
- **[UBEM Wiki](../ubem-wiki/ubem-wiki.md)** - Comprehensive UBEM guide
- **[Workflows Guide](../references/workflows.md)** - Learn EnergyAtlas workflows

## Related Documentation

### Workflows
- [Urban Data Integration](../references/workflows/urban-data-integration.md) - Import and process building data
- [Template Definition and Assignment](../references/workflows/template-definition-assignment.md) - Create and assign archetypes
- [Running and Calibrating](../references/workflows/running-calibrating.md) - Execute simulations

### Resources
- [Archetype Library](../resources/archetype-library.md) - Pre-built building archetypes
- [EnergyAtlas Library](../resources/energyatlas-library.md) - All library resources
- [Technical References](../technical-references/technical-references.md) - Advanced documentation

---

*Last updated: {{ version }}*
