# Template Definition and Assignment

Workflow for creating building archetypes (templates) and assigning them to buildings in your dataset.

## Overview

Template definition and assignment is a critical step that maps your building data to representative energy models (archetypes). This workflow covers creating archetypes, defining assignment rules, and applying them to buildings.

## Prerequisites

- Building data imported into EnergyAtlas
- Understanding of building types in your dataset
- Knowledge of building characteristics (vintage, size, use)

## Step 1: Review Building Data

### Analyze Your Dataset

1. Navigate to **Datahub**
2. Review building type distribution
3. Identify vintage ranges
4. Check size distributions
5. Note any special characteristics

### Identify Archetype Needs

Determine what archetypes you need:

- **Building types**: Residential, commercial, mixed-use, etc.
- **Vintages**: Pre-1980, 1980-2000, post-2000, etc.
- **Sizes**: Small, medium, large
- **Other dimensions**: As needed for your project

## Step 2: Select or Create Archetypes

### Option A: Use Library Archetypes

1. Navigate to **Archetype Library**
2. Browse available archetypes
3. Search by building type, vintage, size
4. Review archetype parameters
5. Select appropriate archetypes

### Option B: Create Custom Archetypes

1. Navigate to **Archetypes** section
2. Click **Create New Archetype**
3. Define archetype properties:
   - **ID**: Unique identifier
   - **Name**: Descriptive name
   - **Building Type**: Classification
   - **Vintage**: Construction era
   - **Size**: Size category
4. Set energy parameters:
   - Wall U-value
   - Roof U-value
   - Window U-value
   - HVAC efficiency
   - Internal loads
5. Save archetype

## Step 3: Define Assignment Rules

### Rule Structure

Assignment rules determine which archetype applies to each building based on building characteristics.

### Create Rules

1. Navigate to **Archetype Assignment**
2. Click **Create Rule**
3. Define rule conditions:
   - **Building Type**: Match specific types
   - **Year Built**: Range or specific years
   - **Floor Area**: Size ranges
   - **Other attributes**: As available
4. Select target archetype
5. Set rule priority (if multiple rules apply)
6. Save rule

### Rule Examples

**Example 1**: Residential Pre-1980
- Condition: `building_type == "Residential" AND year_built < 1980`
- Archetype: `Residential_Pre1980_Medium`

**Example 2**: Large Commercial
- Condition: `building_type == "Commercial" AND floor_area > 5000`
- Archetype: `Commercial_Large`

## Step 4: Apply Assignment Rules

### Automatic Assignment

1. Navigate to **Archetype Assignment**
2. Select buildings or building groups
3. Click **Apply Rules**
4. Review assignment preview
5. Confirm assignments

### Manual Assignment

For specific buildings:

1. Select individual buildings
2. Choose archetype from list
3. Apply assignment
4. Verify assignment

## Step 5: Review Assignments

### Check Coverage

1. Verify all buildings have assigned archetypes
2. Identify unassigned buildings
3. Review assignment distribution
4. Check for unexpected assignments

### Validate Assignments

1. Review sample buildings
2. Verify archetype matches building characteristics
3. Check for logical consistency
4. Identify any misassignments

## Step 6: Refine Assignments

### Adjust Rules

If assignments are incorrect:

1. Review rule logic
2. Modify rule conditions
3. Adjust rule priorities
4. Re-apply rules

### Manual Overrides

For specific cases:

1. Identify buildings needing different archetypes
2. Manually reassign archetypes
3. Document reason for override
4. Update rules if pattern emerges

## Step 7: Document Decisions

### Record Assumptions

Document:

- Archetype selection rationale
- Rule logic and priorities
- Manual overrides and reasons
- Any special cases

### Save Configuration

1. Save assignment configuration
2. Export assignment mapping
3. Document in project notes

## Common Issues and Solutions

### Issue: Buildings Not Assigned

**Solutions**:
- Check rule conditions cover all cases
- Add default rule for unmatched buildings
- Manually assign remaining buildings
- Review building data for missing fields

### Issue: Incorrect Assignments

**Solutions**:
- Review rule logic
- Check rule priority order
- Verify building data accuracy
- Adjust rule conditions

### Issue: Too Many Archetypes

**Solutions**:
- Consolidate similar archetypes
- Use more general archetypes
- Group buildings by key characteristics
- Simplify rule structure

## Best Practices

1. **Start with library**: Use existing archetypes when possible
2. **Keep it simple**: Begin with basic archetypes, refine later
3. **Document rules**: Record rule logic and assumptions
4. **Validate assignments**: Review assignments before simulation
5. **Iterate**: Refine assignments based on results

## Advanced Topics

### Custom Parameters

- Modify archetype parameters for specific buildings
- Create building-specific overrides
- Adjust parameters based on local conditions

### Rule Optimization

- Analyze assignment patterns
- Optimize rule order
- Consolidate similar rules
- Improve rule efficiency

## Next Steps

After assigning archetypes:

- [Running and Calibrating](running-calibrating.md) - Run energy simulations
- [Archetype Object](../objects/archetype.md) - Learn about archetype structure
- [Archetype Assignment Rule](../objects/archetype-assignment-rule.md) - Rule specifications

## Related Documentation

- [Archetype Library](../../resources/archetype-library.md) - Available archetypes
- [Archetype Object](../objects/archetype.md) - Archetype data model
- [Workflows Guide](../workflows.md) - Other workflows
