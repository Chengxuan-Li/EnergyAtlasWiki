# Scenario (Datahub Entry)

Reference documentation for Scenario objects in EnergyAtlas.

## Overview

Scenario objects define energy retrofit scenarios for comparative analysis. Scenarios specify which retrofit measures to apply to which buildings, allowing evaluation of energy savings and economic impacts.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the scenario
- Format: UUID or custom identifier

**name** (string, required)
- Human-readable scenario name
- Example: "Deep Retrofit Scenario"

**description** (string, optional)
- Scenario description and purpose
- Explains scenario objectives

**baseline_simulation_id** (string, required)
- ID of baseline simulation to compare against
- Must reference completed simulation

**buildings** (array, required)
- List of building IDs or building groups
- Buildings included in scenario

**measures** (array, required)
- List of retrofit measures to apply
- See measure application structure below

**parameters** (object, optional)
- Scenario-specific parameters
- Penetration rates, timing, etc.

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Measure Application Structure

```json
{
  "measure_id": "measure_001",
  "buildings": ["B001", "B002"],
  "penetration": 1.0,
  "parameters": {
    "custom_u_value": 0.3
  },
  "timing": {
    "start_date": "2025-01-01",
    "phased": false
  }
}
```

## Example Scenario

```json
{
  "id": "scenario_001",
  "name": "Residential Insulation Upgrade",
  "description": "Adds wall insulation to all pre-1980 residential buildings",
  "baseline_simulation_id": "sim_001",
  "buildings": ["B001", "B002", "B003"],
  "measures": [
    {
      "measure_id": "measure_wall_insulation",
      "buildings": ["B001", "B002", "B003"],
      "penetration": 1.0,
      "parameters": {},
      "timing": {
        "start_date": "2025-01-01",
        "phased": false
      }
    }
  ],
  "parameters": {
    "analysis_period": 20,
    "discount_rate": 0.03
  }
}
```

## Scenario Types

### Single Measure Scenario

Applies one retrofit measure:

```json
{
  "measures": [
    {
      "measure_id": "measure_001",
      "penetration": 1.0
    }
  ]
}
```

### Package Scenario

Applies multiple measures:

```json
{
  "measures": [
    {
      "measure_id": "measure_001",
      "penetration": 1.0
    },
    {
      "measure_id": "measure_002",
      "penetration": 0.8
    }
  ]
}
```

### Phased Scenario

Applies measures over time:

```json
{
  "measures": [
    {
      "measure_id": "measure_001",
      "timing": {
        "start_date": "2025-01-01",
        "phased": true,
        "phases": [
          {"year": 2025, "penetration": 0.3},
          {"year": 2026, "penetration": 0.6},
          {"year": 2027, "penetration": 1.0}
        ]
      }
    }
  ]
}
```

## Operations

### Create Scenario

```json
POST /api/scenarios
{
  "name": "Retrofit Scenario",
  "baseline_simulation_id": "sim_001",
  "buildings": ["B001", "B002"],
  "measures": [...]
}
```

### Get Scenario

```json
GET /api/scenarios/{id}
```

### Update Scenario

```json
PUT /api/scenarios/{id}
{
  "measures": [...],
  "parameters": {...}
}
```

### Delete Scenario

```json
DELETE /api/scenarios/{id}
```

### Run Scenario

```json
POST /api/scenarios/{id}/run
{
  "options": {...}
}
```

### Get Results

```json
GET /api/scenarios/{id}/results
```

## Usage Examples

### Creating Single Measure Scenario

1. Navigate to Scenarios section
2. Click "Create New Scenario"
3. Enter scenario name and description
4. Select baseline simulation
5. Select buildings or building groups
6. Add retrofit measure
7. Configure measure application
8. Set scenario parameters
9. Save scenario

### Creating Package Scenario

1. Create new scenario
2. Select baseline simulation
3. Select buildings
4. Add multiple retrofit measures
5. Configure each measure:
   - Select measure
   - Set penetration
   - Configure parameters
6. Save scenario

### Running Scenario

1. Select scenario
2. Click "Run Scenario"
3. Review configuration
4. Confirm and submit
5. Monitor simulation progress
6. Review results when complete

## Scenario Parameters

### Analysis Period

**analysis_period** (integer)
- Years for economic analysis
- Typical: 20-30 years

### Discount Rate

**discount_rate** (number)
- Discount rate for NPV calculations
- Typical: 0.03 (3%)

### Energy Prices

**energy_prices** (object)
- Electricity and fuel prices
- Can vary over time

### Incentives

**incentives** (array)
- Rebates, tax credits
- Applied to measure costs

## Best Practices

1. **Clear naming**: Use descriptive scenario names
2. **Document purpose**: Explain scenario objectives
3. **Validate inputs**: Check buildings and measures exist
4. **Test configuration**: Review before running
5. **Compare fairly**: Use same baseline and building set

## Common Issues

### Issue: Scenario Fails to Run

**Solutions**:
- Verify baseline simulation exists
- Check building IDs are valid
- Verify measure IDs exist
- Review scenario configuration

### Issue: Unexpected Results

**Solutions**:
- Verify measure parameters
- Check building selections
- Review measure application logic
- Validate input data

## Related Objects

- [Retrofit Measure](retrofit-measure.md) - Measures used in scenario
- [Datahub](datahub.md) - Building data source

## References

- [Scenario Design Workflow](../workflows/scenario-design-simulation.md) - Creating scenarios
- [Retrofit Measures Library](../../resources/retrofit-measures-library.md) - Available measures
