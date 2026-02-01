# Retrofit Measure (Datahub Entry)

Reference documentation for Retrofit Measure entries in EnergyAtlas Datahub.

## Overview

Retrofit Measure entries define energy efficiency improvements that can be applied to buildings. These measures are used in scenario analysis to model the impact of energy retrofits.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the measure
- Format: UUID or custom identifier

**type** (string, required)
- Entry type, must be "retrofit_measure"
- Value: "retrofit_measure"

**name** (string, required)
- Human-readable measure name
- Example: "Wall Insulation Upgrade"

**description** (string, optional)
- Detailed description of the measure
- Explains what the measure does

**measure_type** (string, required)
- Category of retrofit measure
- Values: `Insulation`, `Windows`, `HVAC`, `Lighting`, `Renewable`, `Envelope`

**parameters** (object, required)
- Energy impact parameters (see below)

**cost** (object, optional)
- Cost information (see below)

**applicability** (object, optional)
- Conditions for measure applicability
- Building types, vintages, etc.

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Parameters Structure

### Insulation Measures

```json
{
  "wall_u_value": 0.3,
  "roof_u_value": 0.2,
  "floor_u_value": 0.25
}
```

### Window Measures

```json
{
  "window_u_value": 1.5,
  "window_shgc": 0.4,
  "replacement_fraction": 1.0
}
```

### HVAC Measures

```json
{
  "heating_efficiency": 0.95,
  "cooling_efficiency": 18,
  "system_type": "HeatPump"
}
```

### Lighting Measures

```json
{
  "lighting_power_density": 5,
  "replacement_fraction": 1.0
}
```

### Renewable Energy

```json
{
  "solar_capacity": 5.0,
  "solar_efficiency": 0.20,
  "roof_coverage": 0.5
}
```

## Cost Structure

```json
{
  "unit_cost": 50,
  "unit": "per_sqft",
  "installation_cost": 1000,
  "maintenance_cost": 100,
  "maintenance_frequency": "annual",
  "lifetime": 20
}
```

## Applicability Structure

```json
{
  "building_types": ["Residential", "Commercial"],
  "vintages": ["Pre1980", "1980-2000"],
  "min_floor_area": 500,
  "max_floor_area": null
}
```

## Example Entry

```json
{
  "id": "measure_001",
  "type": "retrofit_measure",
  "name": "Wall Insulation Upgrade",
  "description": "Adds R-20 insulation to exterior walls",
  "measure_type": "Insulation",
  "parameters": {
    "wall_u_value": 0.3,
    "insulation_r_value": 20,
    "application_area": "exterior_walls"
  },
  "cost": {
    "unit_cost": 2.5,
    "unit": "per_sqft",
    "installation_cost": 500,
    "lifetime": 30
  },
  "applicability": {
    "building_types": ["Residential", "Commercial"],
    "vintages": ["Pre1980", "1980-2000"]
  }
}
```

## Operations

### Create Entry

```json
POST /api/datahubs/{datahub_id}/entries
{
  "type": "retrofit_measure",
  "name": "Wall Insulation",
  "measure_type": "Insulation",
  "parameters": {...},
  "cost": {...}
}
```

### Get Entry

```json
GET /api/datahubs/{datahub_id}/entries/{entry_id}
```

### Update Entry

```json
PUT /api/datahubs/{datahub_id}/entries/{entry_id}
{
  "parameters": {...},
  "cost": {...}
}
```

### Delete Entry

```json
DELETE /api/datahubs/{datahub_id}/entries/{entry_id}
```

## Usage Examples

### Creating Insulation Measure

1. Navigate to Datahub
2. Select datahub
3. Click "Add Entry"
4. Choose "Retrofit Measure"
5. Enter measure name and description
6. Select measure type: "Insulation"
7. Set parameters (U-values, R-values)
8. Add cost information
9. Set applicability conditions
10. Save entry

### Creating Window Measure

1. Create new retrofit measure
2. Select type: "Windows"
3. Set window parameters:
   - U-value: 1.5
   - SHGC: 0.4
   - Replacement fraction: 1.0
4. Add cost per window
5. Save measure

### Using in Scenario

1. Navigate to Scenarios
2. Create new scenario
3. Select retrofit measures from datahub
4. Configure measure application
5. Run scenario simulation

## Measure Types

### Insulation

- Wall insulation
- Roof insulation
- Floor insulation
- Foundation insulation

### Windows

- Window replacement
- Window film
- Storm windows
- Window shading

### HVAC

- System replacement
- Efficiency upgrades
- Controls upgrade
- Duct sealing

### Lighting

- LED replacement
- Controls upgrade
- Daylighting

### Renewable Energy

- Solar PV
- Solar thermal
- Geothermal

### Envelope

- Air sealing
- Reflective roof
- Cool roof
- Green roof

## Best Practices

1. **Document parameters**: Clearly describe energy impacts
2. **Include costs**: Add cost data for economic analysis
3. **Set applicability**: Define when measure applies
4. **Validate impacts**: Verify parameter values are reasonable
5. **Use library**: Check library before creating custom measures

## Parameter Guidelines

### U-Values

- **Walls**: 0.2 - 2.0 W/(m²·K)
- **Roofs**: 0.1 - 1.5 W/(m²·K)
- **Windows**: 1.0 - 6.0 W/(m²·K)

### Efficiencies

- **Heating**: 0.7 - 0.98 (AFUE) or 2.0 - 4.0 (COP)
- **Cooling**: 10 - 25 (SEER) or 8 - 20 (EER)

### Costs

- **Unit costs**: Per square foot, per unit, etc.
- **Installation**: One-time costs
- **Maintenance**: Ongoing costs
- **Lifetime**: Expected measure lifetime

## Related Objects

- [Datahub](datahub.md) - Parent datahub object
- [Scenario](scenario.md) - Using measures in scenarios

## References

- [Retrofit Measures Library](../../resources/retrofit-measures-library.md) - Available measures
- [Scenario Design Workflow](../workflows/scenario-design-simulation.md) - Using measures
