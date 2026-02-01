# Energy Atlas Objects

Comprehensive reference guide to all object types in the EnergyAtlas data model.

## Overview

EnergyAtlas uses a structured data model composed of various object types. Understanding these objects and their relationships is essential for effective use of the platform. This guide provides an overview of all object types and their purposes.

## Core Objects

### Datahub

**Purpose**: Central repository for all project data

**Contains**:
- Building data entries
- Weather files
- Geospatial data
- Other project assets

**Key Features**:
- Organizes all project data in one place
- Supports multiple entry types
- Enables data management and versioning

**See**: [Datahub Object](objects/datahub.md)

### Archetype

**Purpose**: Defines representative building energy models

**Key Properties**:
- Building type, vintage, size
- Envelope parameters (U-values, windows)
- HVAC system specifications
- Internal load parameters

**Usage**:
- Assigned to buildings for energy modeling
- Used in simulation calculations
- Basis for energy consumption estimates

**See**: [Archetype Object](objects/archetype.md)

### Archetype Assignment Rule

**Purpose**: Defines how buildings are matched to archetypes

**Key Features**:
- Conditional logic for matching
- Priority-based rule application
- Flexible condition operators

**Usage**:
- Automates archetype assignment
- Ensures consistent assignments
- Supports complex matching logic

**See**: [Archetype Assignment Rule Object](objects/archetype-assignment-rule.md)

## Data Entry Objects

### Geospatial Data

**Purpose**: Stores geographic and spatial information

**Contains**:
- Building footprints (polygons)
- Geographic coordinates
- Spatial attributes

**Formats**:
- GeoJSON
- Shapefile
- CSV with coordinates

**See**: [Geospatial Data Object](objects/geospatial-data.md)

### Weather File

**Purpose**: Stores weather data for simulations

**Formats**:
- EPW (EnergyPlus Weather)
- TMY3 (Typical Meteorological Year 3)
- Custom CSV formats

**Contains**:
- Temperature data
- Solar radiation
- Wind data
- Other meteorological parameters

**See**: [Weather File Object](objects/weather-file.md)

## Scenario Objects

### Retrofit Measure

**Purpose**: Defines energy efficiency improvements

**Categories**:
- Insulation measures
- Window upgrades
- HVAC improvements
- Lighting retrofits
- Renewable energy
- Envelope improvements

**Key Properties**:
- Energy impact parameters
- Cost information
- Applicability conditions

**See**: [Retrofit Measure Object](objects/retrofit-measure.md)

### Scenario

**Purpose**: Defines energy retrofit scenarios for analysis

**Contains**:
- Baseline simulation reference
- Selected buildings
- Retrofit measures to apply
- Application parameters

**Types**:
- Single measure scenarios
- Package scenarios
- Phased scenarios
- Policy scenarios

**See**: [Scenario Object](objects/scenario.md)

## Object Relationships

### Data Flow

```
Datahub
  ├── Geospatial Data (buildings)
  ├── Weather File
  └── Other entries
        │
        ↓
  Archetype Assignment
        │
        ↓
  Archetype
        │
        ↓
  Simulation
        │
        ↓
  Scenario (optional)
        │
        ↓
  Results
```

### Relationships

**Datahub → Entries**
- Datahub contains multiple entry types
- Entries are organized within datahub
- Entries can reference each other

**Buildings → Archetypes**
- Buildings are assigned archetypes
- Assignment uses rules
- One archetype per building

**Archetypes → Simulations**
- Archetypes define simulation parameters
- Simulations use archetype properties
- Results depend on archetype accuracy

**Scenarios → Measures**
- Scenarios apply retrofit measures
- Measures define energy impacts
- Multiple measures can be combined

**Scenarios → Buildings**
- Scenarios target specific buildings
- Buildings can be in multiple scenarios
- Scenarios compare with baseline

## Object Lifecycle

### Creation

1. **Data Import**: Create datahub entries from external data
2. **Archetype Definition**: Create or select archetypes
3. **Rule Creation**: Define assignment rules
4. **Scenario Setup**: Create scenarios with measures

### Usage

1. **Assignment**: Apply archetypes to buildings
2. **Simulation**: Run energy simulations
3. **Analysis**: Create and run scenarios
4. **Results**: View and export results

### Management

1. **Updates**: Modify object properties
2. **Versioning**: Track object versions
3. **Deletion**: Remove unused objects
4. **Archiving**: Archive old objects

## Common Operations

### Working with Datahubs

- Create new datahub
- Import data entries
- Organize entries
- Export datahub contents

### Working with Archetypes

- Browse archetype library
- Create custom archetypes
- Modify archetype parameters
- Assign archetypes to buildings

### Working with Rules

- Create assignment rules
- Test rule logic
- Apply rules to buildings
- Refine rule conditions

### Working with Scenarios

- Create scenario configurations
- Select retrofit measures
- Configure measure application
- Run scenario simulations

## Best Practices

### Object Organization

1. **Use clear naming**: Descriptive names for all objects
2. **Organize logically**: Group related objects
3. **Document purpose**: Add descriptions to objects
4. **Version control**: Track object changes

### Data Management

1. **Validate inputs**: Check data quality before creating objects
2. **Use libraries**: Leverage pre-defined libraries when possible
3. **Customize carefully**: Modify objects only when necessary
4. **Document changes**: Record modifications and rationale

### Workflow Integration

1. **Follow sequence**: Create objects in proper order
2. **Validate relationships**: Ensure objects are properly linked
3. **Test configurations**: Verify object settings before use
4. **Iterate**: Refine objects based on results

## Object Specifications

### Required Fields

Each object type has required fields that must be specified:

- **Datahub**: id, name
- **Archetype**: id, name, building_type, vintage, size, parameters
- **Rule**: id, name, conditions, archetype_id, priority
- **Geospatial Data**: id, type, geometry, properties
- **Weather File**: id, type, file_path, location, period
- **Retrofit Measure**: id, type, name, measure_type, parameters
- **Scenario**: id, name, baseline_simulation_id, buildings, measures

### Optional Fields

Many objects support optional fields for enhanced functionality:

- Descriptions for documentation
- Metadata for additional information
- Tags for organization
- Custom properties for extensions

## API Access

All objects can be accessed via the EnergyAtlas API:

- **Create**: POST requests to create objects
- **Read**: GET requests to retrieve objects
- **Update**: PUT requests to modify objects
- **Delete**: DELETE requests to remove objects
- **List**: GET requests to list objects

See API documentation for detailed specifications.

## Examples

### Complete Workflow Example

1. **Create Datahub**
   ```json
   POST /api/datahubs
   {"name": "Project Datahub"}
   ```

2. **Import Buildings**
   ```json
   POST /api/datahubs/{id}/entries
   {"type": "geospatial_data", "geometry": {...}}
   ```

3. **Create Archetype**
   ```json
   POST /api/archetypes
   {"id": "Residential_Pre1980", "parameters": {...}}
   ```

4. **Create Assignment Rule**
   ```json
   POST /api/archetype-assignment-rules
   {"conditions": [...], "archetype_id": "..."}
   ```

5. **Run Simulation**
   ```json
   POST /api/simulations
   {"buildings": [...], "archetypes": [...]}
   ```

6. **Create Scenario**
   ```json
   POST /api/scenarios
   {"baseline_simulation_id": "...", "measures": [...]}
   ```

## Troubleshooting

### Common Issues

**Missing Required Fields**
- Check object specifications
- Verify all required fields provided
- Review error messages

**Invalid Relationships**
- Verify referenced objects exist
- Check object IDs are correct
- Validate relationship constraints

**Object Not Found**
- Check object ID spelling
- Verify object exists
- Review access permissions

## Related Documentation

- [Workflows Guide](workflows.md) - Using objects in workflows
- [Input Output Guide](input-output.md) - Object data formats
- [Data Preparation](data-prep.md) - Preparing data for objects

## Individual Object References

- [Datahub](objects/datahub.md) - Central data repository
- [Archetype](objects/archetype.md) - Building archetype definitions
- [Archetype Assignment Rule](objects/archetype-assignment-rule.md) - Assignment rules
- [Geospatial Data](objects/geospatial-data.md) - Geographic data entries
- [Weather File](objects/weather-file.md) - Weather data files
- [Retrofit Measure](objects/retrofit-measure.md) - Energy efficiency measures
- [Scenario](objects/scenario.md) - Retrofit scenarios
