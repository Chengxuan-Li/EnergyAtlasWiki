# Archetype Assignment Rule

Reference documentation for Archetype Assignment Rule objects in EnergyAtlas.

## Overview

Archetype Assignment Rules define how buildings are matched to archetypes based on building characteristics. Rules use conditions to determine which archetype should be assigned to each building.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the rule
- Format: UUID or custom identifier

**name** (string, required)
- Human-readable rule name
- Example: "Residential Pre-1980 Rule"

**description** (string, optional)
- Rule description and purpose

**conditions** (array, required)
- List of conditions that must be met
- See condition structure below

**archetype_id** (string, required)
- ID of archetype to assign when conditions are met

**priority** (integer, required)
- Rule priority (higher number = higher priority)
- Used when multiple rules match
- Typical range: 1-100

**active** (boolean, required)
- Whether rule is active
- Default: true

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Condition Structure

### Condition Object

```json
{
  "field": "building_type",
  "operator": "equals",
  "value": "Residential"
}
```

### Operators

**equals**
- Field equals value exactly
- Example: `building_type equals "Residential"`

**not_equals**
- Field does not equal value
- Example: `building_type not_equals "Commercial"`

**contains**
- Field contains substring
- Example: `building_type contains "Res"`

**greater_than**
- Numeric field greater than value
- Example: `year_built greater_than 1980`

**less_than**
- Numeric field less than value
- Example: `year_built less_than 2000`

**greater_than_or_equal**
- Numeric field greater than or equal to value
- Example: `floor_area greater_than_or_equal 1000`

**less_than_or_equal**
- Numeric field less than or equal to value
- Example: `floor_area less_than_or_equal 5000`

**in**
- Field value in list
- Example: `building_type in ["Residential", "MixedUse"]`

**not_in**
- Field value not in list
- Example: `building_type not_in ["Commercial"]`

**between**
- Numeric field between two values
- Example: `year_built between 1980 and 2000`

## Rule Logic

### Multiple Conditions

When multiple conditions are specified:
- **AND logic**: All conditions must be met (default)
- **OR logic**: Any condition can be met (specify in rule)

### Example Rule

```json
{
  "id": "rule_001",
  "name": "Residential Pre-1980 Medium",
  "description": "Assigns residential pre-1980 medium archetype",
  "conditions": [
    {
      "field": "building_type",
      "operator": "equals",
      "value": "Residential"
    },
    {
      "field": "year_built",
      "operator": "less_than",
      "value": 1980
    },
    {
      "field": "floor_area",
      "operator": "between",
      "value": [800, 2000]
    }
  ],
  "archetype_id": "Residential_Pre1980_Medium",
  "priority": 10,
  "active": true
}
```

## Operations

### Create Rule

```json
POST /api/archetype-assignment-rules
{
  "name": "Residential Pre-1980",
  "conditions": [...],
  "archetype_id": "Residential_Pre1980_Medium",
  "priority": 10
}
```

### Get Rule

```json
GET /api/archetype-assignment-rules/{id}
```

### Update Rule

```json
PUT /api/archetype-assignment-rules/{id}
{
  "conditions": [...],
  "priority": 15
}
```

### Delete Rule

```json
DELETE /api/archetype-assignment-rules/{id}
```

### List Rules

```json
GET /api/archetype-assignment-rules?active=true
```

### Apply Rules

```json
POST /api/archetype-assignment-rules/apply
{
  "building_ids": ["B001", "B002"],
  "rule_ids": ["rule_001", "rule_002"]
}
```

## Usage Examples

### Creating a Simple Rule

1. Navigate to Archetype Assignment section
2. Click "Create New Rule"
3. Enter rule name
4. Add conditions:
   - Building type equals "Residential"
   - Year built less than 1980
5. Select target archetype
6. Set priority
7. Save rule

### Creating a Complex Rule

1. Create rule with multiple conditions
2. Use AND logic for all conditions
3. Set appropriate priority
4. Test rule on sample buildings
5. Refine conditions if needed

### Rule Priority Example

**Rule 1** (Priority: 20):
- Building type = "Residential"
- Year built < 1980
- Floor area > 2000
- → Assigns "Residential_Pre1980_Large"

**Rule 2** (Priority: 10):
- Building type = "Residential"
- Year built < 1980
- → Assigns "Residential_Pre1980_Medium"

If a building matches both rules, Rule 1 (higher priority) applies.

## Best Practices

1. **Start simple**: Begin with basic conditions
2. **Test rules**: Apply to sample buildings first
3. **Use priorities**: Order rules by specificity
4. **Document logic**: Explain rule purpose
5. **Review coverage**: Ensure all buildings are covered

## Common Patterns

### By Building Type

```json
{
  "conditions": [
    {"field": "building_type", "operator": "equals", "value": "Residential"}
  ]
}
```

### By Vintage

```json
{
  "conditions": [
    {"field": "year_built", "operator": "less_than", "value": 1980}
  ]
}
```

### By Size

```json
{
  "conditions": [
    {"field": "floor_area", "operator": "between", "value": [1000, 3000]}
  ]
}
```

### Combined

```json
{
  "conditions": [
    {"field": "building_type", "operator": "equals", "value": "Commercial"},
    {"field": "year_built", "operator": "greater_than", "value": 2000},
    {"field": "floor_area", "operator": "greater_than", "value": 5000}
  ]
}
```

## Related Objects

- [Archetype](archetype.md) - Target archetype
- [Datahub](datahub.md) - Building data source

## References

- [Template Definition Workflow](../workflows/template-definition-assignment.md) - Using rules
- [Archetype Library](../../resources/archetype-library.md) - Available archetypes
