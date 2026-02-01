# Archetype Library

Comprehensive library of building archetypes available in EnergyAtlas.

## Overview

The Archetype Library provides pre-defined building archetypes for common building types, vintages, and sizes. These archetypes can be used directly or customized for specific projects.

## Library Structure

Archetypes are organized by:

- **Building Type**: Residential, Commercial, Mixed-Use, Institutional
- **Vintage**: Pre-1980, 1980-2000, Post-2000
- **Size**: Small, Medium, Large

## Residential Archetypes

### Pre-1980 Residential

**Residential_Pre1980_Small**
- Typical single-family homes
- Floor area: < 1500 sq ft
- Uninsulated or minimal insulation
- Older HVAC systems

**Residential_Pre1980_Medium**
- Typical single-family homes
- Floor area: 1500-2500 sq ft
- Minimal wall insulation (R-11)
- Standard efficiency HVAC

**Residential_Pre1980_Large**
- Large single-family homes
- Floor area: > 2500 sq ft
- Variable insulation levels
- Multiple HVAC zones

### 1980-2000 Residential

**Residential_1980-2000_Small**
- Modern construction standards
- Improved insulation (R-13 to R-19)
- Standard efficiency HVAC
- Better windows

**Residential_1980-2000_Medium**
- Typical suburban homes
- R-19 wall insulation
- Standard HVAC systems
- Double-pane windows

**Residential_1980-2000_Large**
- Large modern homes
- Good insulation levels
- Multiple HVAC systems
- Energy-efficient windows

### Post-2000 Residential

**Residential_Post2000_Small**
- Energy-efficient construction
- High insulation (R-21+)
- High-efficiency HVAC
- Low-E windows

**Residential_Post2000_Medium**
- Modern energy standards
- Excellent insulation
- High-efficiency systems
- Advanced windows

**Residential_Post2000_Large**
- Luxury/energy-efficient homes
- Maximum insulation
- Premium HVAC systems
- Best available windows

## Commercial Archetypes

### Pre-1980 Commercial

**Commercial_Pre1980_Small**
- Small commercial buildings
- Minimal insulation
- Older HVAC systems
- Single-pane windows

**Commercial_Pre1980_Medium**
- Medium office buildings
- Some insulation
- Standard HVAC
- Basic windows

**Commercial_Pre1980_Large**
- Large commercial buildings
- Variable insulation
- Central HVAC systems
- Mixed window types

### 1980-2000 Commercial

**Commercial_1980-2000_Small**
- Modern small commercial
- Improved insulation
- Standard efficiency HVAC
- Double-pane windows

**Commercial_1980-2000_Medium**
- Typical office buildings
- Good insulation
- Efficient HVAC
- Energy-efficient windows

**Commercial_1980-2000_Large**
- Large office buildings
- Excellent insulation
- High-efficiency HVAC
- Advanced windows

### Post-2000 Commercial

**Commercial_Post2000_Small**
- Energy-efficient small commercial
- High insulation
- High-efficiency HVAC
- Premium windows

**Commercial_Post2000_Medium**
- LEED-certified buildings
- Maximum insulation
- Premium HVAC systems
- Best windows

**Commercial_Post2000_Large**
- High-performance buildings
- Optimal insulation
- Advanced HVAC
- State-of-the-art windows

## Mixed-Use Archetypes

### Pre-1980 Mixed-Use

**MixedUse_Pre1980_Medium**
- Older mixed-use buildings
- Residential + commercial
- Variable insulation
- Older systems

### 1980-2000 Mixed-Use

**MixedUse_1980-2000_Medium**
- Modern mixed-use
- Improved construction
- Better systems
- Energy-efficient features

### Post-2000 Mixed-Use

**MixedUse_Post2000_Medium**
- Energy-efficient mixed-use
- High-performance design
- Advanced systems
- Premium features

## Institutional Archetypes

### Schools

**School_Pre1980**
- Older school buildings
- Large floor areas
- Older HVAC systems
- Basic insulation

**School_1980-2000**
- Modern schools
- Improved systems
- Better insulation
- Energy-efficient features

**School_Post2000**
- High-performance schools
- Advanced systems
- Maximum efficiency
- Sustainable design

### Hospitals

**Hospital_Pre1980**
- Older hospitals
- Complex systems
- High energy use
- Older equipment

**Hospital_1980-2000**
- Modern hospitals
- Improved efficiency
- Better systems
- Energy management

**Hospital_Post2000**
- High-performance hospitals
- Advanced systems
- Maximum efficiency
- Sustainable design

## Using the Library

### Selecting Archetypes

1. Navigate to Archetype Library
2. Filter by building type, vintage, size
3. Review archetype parameters
4. Select appropriate archetypes
5. Use in assignment rules

### Customizing Archetypes

1. Select library archetype
2. Click "Create Copy"
3. Modify parameters as needed
4. Save as custom archetype
5. Use in project

## Parameter Ranges

### Wall U-Values

- **Pre-1980**: 1.0 - 2.0 W/(m²·K)
- **1980-2000**: 0.5 - 1.0 W/(m²·K)
- **Post-2000**: 0.2 - 0.5 W/(m²·K)

### Window U-Values

- **Pre-1980**: 4.0 - 6.0 W/(m²·K)
- **1980-2000**: 2.0 - 4.0 W/(m²·K)
- **Post-2000**: 1.0 - 2.0 W/(m²·K)

### HVAC Efficiency

- **Pre-1980**: Low efficiency
- **1980-2000**: Standard efficiency
- **Post-2000**: High efficiency

## Best Practices

1. **Start with library**: Use existing archetypes when possible
2. **Match characteristics**: Select archetypes matching your buildings
3. **Customize carefully**: Modify only when necessary
4. **Document changes**: Record any customizations
5. **Validate**: Test archetypes before wide use

## Contributing

To contribute new archetypes:

1. Create archetype definition
2. Validate parameters
3. Document sources
4. Submit for review
5. Add to library

## References

- [Archetype Object](../references/objects/archetype.md) - Archetype structure
- [Template Definition Workflow](../references/workflows/template-definition-assignment.md) - Using archetypes
