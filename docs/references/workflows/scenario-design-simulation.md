# Scenario Design and Simulation

Workflow for creating energy retrofit scenarios and running comparative simulations.

## Overview

Scenario design allows you to model the impact of energy efficiency interventions across your building stock. This workflow covers creating scenarios, defining retrofit measures, running scenario simulations, and comparing results.

## Prerequisites

- Baseline simulation completed
- Understanding of retrofit measures to evaluate
- Access to retrofit measures library (optional)

## Step 1: Define Scenario Objectives

### Identify Goals

Determine what you want to evaluate:

- **Energy savings**: Potential reduction in consumption
- **Cost-effectiveness**: Payback periods, ROI
- **Emissions reduction**: CO₂ and other emissions
- **Peak demand**: Impact on peak electricity demand
- **Policy scenarios**: Test policy interventions

### Set Scope

Define scenario scope:

- **Buildings**: Which buildings to include
- **Measures**: What retrofit measures to evaluate
- **Timeframe**: Analysis period
- **Penetration**: Adoption rate (100% or partial)

## Step 2: Select Retrofit Measures

### Browse Library

1. Navigate to **Retrofit Measures Library**
2. Browse available measures
3. Review measure parameters
4. Select appropriate measures

### Available Measure Types

- **Insulation**: Wall, roof, floor insulation upgrades
- **Windows**: High-performance window replacement
- **HVAC**: Heating and cooling system upgrades
- **Lighting**: LED lighting retrofits
- **Renewable Energy**: Solar PV, solar thermal
- **Building Envelope**: Air sealing, reflective roofs

### Create Custom Measures

If needed:

1. Navigate to **Retrofit Measures**
2. Click **Create New Measure**
3. Define measure properties:
   - **Name**: Descriptive name
   - **Type**: Measure category
   - **Parameters**: Energy impact parameters
   - **Cost**: Implementation cost
4. Save measure

## Step 3: Create Scenario

### Scenario Configuration

1. Navigate to **Scenarios** section
2. Click **Create New Scenario**
3. Define scenario properties:
   - **Name**: Descriptive scenario name
   - **Description**: Scenario purpose
   - **Baseline**: Select baseline simulation
4. Select buildings or building groups
5. Choose retrofit measures to apply
6. Set measure parameters:
   - **Penetration**: Percentage of buildings
   - **Implementation**: All at once or phased
   - **Measure combinations**: If multiple measures

### Scenario Types

**Single Measure Scenario**:
- Test one retrofit measure
- Simple comparison
- Good for initial evaluation

**Package Scenario**:
- Combine multiple measures
- More realistic
- Evaluate synergies

**Deep Retrofit Scenario**:
- Comprehensive upgrades
- Maximum energy savings
- Higher cost

**Policy Scenario**:
- Model policy interventions
- Mandatory vs. voluntary
- Incentive programs

## Step 4: Configure Scenario Parameters

### Measure Application

Set how measures apply:

- **Building selection**: Which buildings receive measures
- **Measure selection**: Which measures to apply
- **Parameter values**: Measure-specific settings
- **Timing**: When measures are implemented

### Cost Parameters

If evaluating economics:

- **Measure costs**: Implementation costs
- **Maintenance**: Ongoing costs
- **Financing**: Interest rates, terms
- **Incentives**: Rebates, tax credits

## Step 5: Review Scenario Configuration

### Validate Settings

1. Review selected buildings
2. Verify measure selections
3. Check parameter values
4. Confirm cost inputs (if applicable)

### Estimate Impact

1. Review expected energy savings
2. Check cost estimates
3. Verify scenario is feasible
4. Identify any issues

## Step 6: Run Scenario Simulation

### Submit Simulation

1. Click **Run Scenario** or **Submit**
2. Confirm scenario configuration
3. Monitor simulation queue
4. Note scenario job ID

### Monitor Progress

1. Check simulation status
2. Review progress indicators
3. Monitor for errors
4. Wait for completion

## Step 7: Compare Scenarios

### Review Results

1. Navigate to **Results** section
2. Select scenario to view
3. Review summary statistics
4. Check key metrics

### Compare with Baseline

Calculate differences:

- **Energy savings**: Reduction in consumption
- **Cost savings**: Reduction in energy costs
- **Emissions reduction**: CO₂ and other emissions
- **Peak demand**: Change in peak demand

### Compare Multiple Scenarios

If running multiple scenarios:

1. Select scenarios to compare
2. View side-by-side comparison
3. Compare key metrics
4. Identify best-performing scenarios

## Step 8: Analyze Results

### Energy Analysis

Review energy impacts:

- **Annual savings**: Total energy reduction
- **Monthly patterns**: Seasonal variations
- **By building type**: Savings by category
- **Peak reduction**: Demand reduction

### Economic Analysis

If cost data provided:

- **Payback period**: Time to recover costs
- **NPV**: Net present value
- **ROI**: Return on investment
- **Cost per saved energy**: Efficiency metric

### Spatial Analysis

View geographic patterns:

- **Maps**: Spatial distribution of savings
- **Hotspots**: Areas with highest potential
- **Clusters**: Building groups with similar results

## Step 9: Generate Reports

### Create Summary Report

1. Select scenario results
2. Choose report format
3. Customize report sections
4. Generate and export report

### Report Contents

Include:

- Executive summary
- Scenario description
- Key findings
- Energy savings summary
- Economic analysis (if applicable)
- Visualizations
- Recommendations

## Common Issues and Solutions

### Issue: Scenario Fails to Run

**Solutions**:
- Verify baseline simulation exists
- Check building selections
- Review measure definitions
- Check simulation parameters

### Issue: Unexpected Results

**Solutions**:
- Verify measure parameters
- Check building characteristics
- Review measure application logic
- Validate input data

### Issue: Scenarios Not Comparable

**Solutions**:
- Ensure same baseline
- Use consistent building sets
- Apply same time period
- Use same weather data

## Best Practices

1. **Start simple**: Begin with single measures
2. **Document scenarios**: Record assumptions and parameters
3. **Validate inputs**: Check measure parameters are reasonable
4. **Compare fairly**: Use consistent baselines and building sets
5. **Consider context**: Account for local conditions and constraints

## Advanced Topics

### Sensitivity Analysis

- Vary measure parameters
- Test different penetration rates
- Evaluate parameter uncertainty
- Identify key drivers

### Optimization

- Find optimal measure combinations
- Maximize savings within budget
- Minimize cost per unit saved
- Balance multiple objectives

## Next Steps

After scenario analysis:

- [Results View](results-view.md) - Detailed results analysis
- [Retrofit Measures Library](../../resources/retrofit-measures-library.md) - Available measures
- [Scenario Object](../objects/scenario.md) - Scenario specifications

## Related Documentation

- [Running and Calibrating](running-calibrating.md) - Baseline simulation
- [Retrofit Measure Object](../objects/retrofit-measure.md) - Measure specifications
- [Workflows Guide](../workflows.md) - Other workflows
