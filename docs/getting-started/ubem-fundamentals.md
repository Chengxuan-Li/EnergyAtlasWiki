# UBEM Fundamentals

Understanding the fundamentals of Urban Building Energy Modeling (UBEM) is essential for effective use of EnergyAtlas.

## What is UBEM?

```plotly
{
  "title": "Global CO2e Emissions",
  "data": [

    {
      "type": "bar",
      "name": "Global CO2e Emissions",

  "x": [
    1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
    1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
    1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023
  ],
  "y": [
    16760, 17480, 18424, 18372, 18400, 19418, 20019, 20520, 21090, 20769,
    20365, 20236, 20309, 20981, 21301, 21705, 22381, 23120, 23573, 23963,
    24099, 23974, 24103, 24204, 24863, 25378, 25799, 25951, 26085, 26857,
    27222, 27545, 28775, 30044, 31140, 32051, 33144, 33384, 32868, 34766,
    35777, 36130, 36799, 36888, 36703, 36685, 37245, 38041, 38034, 35984,
    37933, 38404, 38987
  ]


    }
  ],
  "layout": {
    "xaxis": {"title": "Year"},
    "yaxis": {"title": "Million Tonnes of CO2e"},
    "barmode": "group"
  }
}
```

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
