# Archetype

Reference documentation for the Archetype object in EnergyAtlas.

## Overview

An Archetype represents a typical building with specific characteristics. Archetypes define energy-related parameters that are used to model energy consumption for buildings assigned to that archetype.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the archetype
- Format: `{building_type}_{vintage}_{size}`
- Example: `Residential_Pre1980_Medium`

**name** (string, required)
- Human-readable name
- Example: "Residential Pre-1980 Medium"

**building_type** (string, required)
- Building classification
- Values: `Residential`, `Commercial`, `MixedUse`, `Institutional`

**vintage** (string, required)
- Construction era
- Values: `Pre1980`, `1980-2000`, `Post2000`

**size** (string, required)
- Size category
- Values: `Small`, `Medium`, `Large`

**parameters** (object, required)
- Energy-related parameters (see below)

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Parameters

### Envelope Parameters

**wall_u_value** (number, required)
- Wall U-value in W/(m²·K)
- Typical range: 0.2 - 2.0

**roof_u_value** (number, required)
- Roof U-value in W/(m²·K)
- Typical range: 0.1 - 1.5

**floor_u_value** (number, optional)
- Floor U-value in W/(m²·K)
- Typical range: 0.2 - 1.5

**window_u_value** (number, required)
- Window U-value in W/(m²·K)
- Typical range: 1.0 - 6.0

**window_shgc** (number, required)
- Solar Heat Gain Coefficient
- Typical range: 0.2 - 0.8

**window_wall_ratio** (number, required)
- Window-to-wall ratio
- Typical range: 0.1 - 0.5

### HVAC Parameters

**heating_system_type** (string, required)
- Values: `GasFurnace`, `HeatPump`, `ElectricResistance`, `District`

**heating_efficiency** (number, required)
- AFUE or COP
- Typical range: 0.7 - 4.0

**cooling_system_type** (string, required)
- Values: `CentralAC`, `HeatPump`, `WindowAC`, `District`

**cooling_efficiency** (number, required)
- SEER or EER
- Typical range: 10 - 25

### Internal Loads

**occupancy_density** (number, required)
- People per unit area (people/m²)
- Typical range: 0.01 - 0.1

**lighting_power_density** (number, required)
- Lighting power per unit area (W/m²)
- Typical range: 3 - 15

**equipment_power_density** (number, required)
- Equipment power per unit area (W/m²)
- Typical range: 2 - 10

### Schedules

**occupancy_schedule** (string, required)
- Reference to occupancy schedule
- Format: Schedule ID or default schedule name

**lighting_schedule** (string, required)
- Reference to lighting schedule
- Format: Schedule ID or default schedule name

**equipment_schedule** (string, required)
- Reference to equipment schedule
- Format: Schedule ID or default schedule name

## Example

```json
{
  "id": "Residential_Pre1980_Medium",
  "name": "Residential Pre-1980 Medium",
  "building_type": "Residential",
  "vintage": "Pre1980",
  "size": "Medium",
  "parameters": {
    "wall_u_value": 1.2,
    "roof_u_value": 0.8,
    "window_u_value": 5.0,
    "window_shgc": 0.6,
    "window_wall_ratio": 0.15,
    "heating_system_type": "GasFurnace",
    "heating_efficiency": 0.78,
    "cooling_system_type": "CentralAC",
    "cooling_efficiency": 10,
    "occupancy_density": 0.03,
    "lighting_power_density": 8,
    "equipment_power_density": 3,
    "occupancy_schedule": "Residential_Default",
    "lighting_schedule": "Residential_Default",
    "equipment_schedule": "Residential_Default"
  }
}
```

## Operations

### Create Archetype

```json
POST /api/archetypes
{
  "id": "Residential_Pre1980_Medium",
  "name": "Residential Pre-1980 Medium",
  "building_type": "Residential",
  "vintage": "Pre1980",
  "size": "Medium",
  "parameters": {...}
}
```

### Get Archetype

```json
GET /api/archetypes/{id}
```

### Update Archetype

```json
PUT /api/archetypes/{id}
{
  "parameters": {...}
}
```

### List Archetypes

```json
GET /api/archetypes?building_type=Residential&vintage=Pre1980
```

## Usage

### Creating Custom Archetype

1. Navigate to Archetypes section
2. Click "Create New Archetype"
3. Fill in basic information
4. Set parameter values
5. Save archetype

### Modifying Archetype

1. Select archetype
2. Click "Edit"
3. Modify parameters
4. Save changes

### Using in Assignment

1. Create assignment rule
2. Select archetype
3. Apply to buildings
4. Verify assignments

## Best Practices

1. **Use library first**: Check library before creating custom
2. **Document sources**: Note parameter sources
3. **Validate parameters**: Check values are reasonable
4. **Version control**: Track parameter changes
5. **Test before use**: Validate archetype in test simulation

## Related Objects

- [Archetype Assignment Rule](archetype-assignment-rule.md) - Rules for assigning archetypes
- [Datahub](datahub.md) - Where archetypes are stored

## References

- [Archetype Library](../../resources/archetype-library.md) - Available archetypes
- [Template Definition Workflow](../workflows/template-definition-assignment.md) - Using archetypes
