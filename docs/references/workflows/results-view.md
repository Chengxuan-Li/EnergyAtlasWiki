# Results View

Workflow for analyzing, visualizing, and exporting simulation results in EnergyAtlas.

## Overview

The results view workflow helps you explore simulation outputs, generate insights, create visualizations, and export data for further analysis or reporting.

## Prerequisites

- Completed simulation (baseline or scenario)
- Access to results section
- Understanding of key metrics

## Step 1: Access Results

### Navigate to Results

1. Log into EnergyAtlas
2. Navigate to **Results** section
3. Select simulation or scenario
4. Choose results view type

### Available Views

- **Summary**: High-level statistics
- **Detailed**: Building-level results
- **Time Series**: Temporal data
- **Maps**: Spatial visualizations
- **Charts**: Graphical representations

## Step 2: Explore Summary Statistics

### Key Metrics

Review summary statistics:

- **Total Energy**: Annual consumption
- **Energy Intensity**: Consumption per unit area
- **Peak Demand**: Maximum demand
- **Average Consumption**: Mean values
- **Distribution**: Min, max, median, percentiles

### Breakdowns

View results by:

- **Building Type**: Residential, commercial, etc.
- **Vintage**: Construction era
- **Size**: Building size categories
- **Archetype**: Assigned archetype
- **Geographic**: Spatial regions

## Step 3: Analyze Building-Level Results

### View Building Data

1. Open building-level results table
2. Sort by various columns
3. Filter by building characteristics
4. Identify outliers or patterns

### Key Building Metrics

For each building:

- **Annual Energy**: Total consumption
- **Heating Energy**: Space heating
- **Cooling Energy**: Space cooling
- **Other Energy**: Equipment, lighting, etc.
- **Peak Demand**: Maximum demand
- **Energy Intensity**: Per unit area

## Step 4: Explore Time Series Data

### Temporal Patterns

View energy consumption over time:

- **Monthly**: Monthly consumption patterns
- **Daily**: Daily profiles
- **Hourly**: Hourly load profiles
- **Seasonal**: Seasonal variations

### Analyze Patterns

Identify:

- **Peak periods**: Times of highest consumption
- **Seasonal trends**: Summer vs. winter patterns
- **Daily patterns**: Day vs. night consumption
- **Anomalies**: Unusual consumption patterns

## Step 5: Create Visualizations

### Maps

Create spatial visualizations:

1. Select **Map View**
2. Choose variable to visualize
3. Select color scheme
4. Adjust visualization settings
5. Explore map interactively

**Map Types**:
- **Heat maps**: Density visualizations
- **Choropleth**: Color-coded by value
- **Symbol maps**: Sized symbols
- **3D maps**: Height represents values

### Charts

Generate charts:

1. Select **Chart View**
2. Choose chart type
3. Select variables
4. Configure chart options
5. Generate chart

**Chart Types**:
- **Bar charts**: Compare categories
- **Line charts**: Show trends over time
- **Scatter plots**: Explore relationships
- **Histograms**: Show distributions
- **Box plots**: Compare distributions

### Interactive Dashboards

Create dashboards:

1. Select **Dashboard** view
2. Add visualization components
3. Configure filters and controls
4. Arrange layout
5. Save dashboard

## Step 6: Compare Results

### Baseline vs. Scenario

Compare scenarios with baseline:

1. Select baseline and scenario results
2. View side-by-side comparison
3. Calculate differences
4. Analyze changes

### Multiple Scenarios

Compare multiple scenarios:

1. Select scenarios to compare
2. View comparison table or chart
3. Identify best-performing scenarios
4. Analyze trade-offs

### Metrics Comparison

Compare key metrics:

- **Energy savings**: Reduction percentages
- **Cost savings**: Economic impacts
- **Emissions**: Environmental impacts
- **Peak demand**: Demand reduction

## Step 7: Generate Reports

### Create Report

1. Select results to include
2. Choose report template
3. Customize report sections
4. Generate report

### Report Sections

Include:

- **Executive Summary**: Key findings
- **Methodology**: Approach and assumptions
- **Results Overview**: Summary statistics
- **Detailed Analysis**: Building-level results
- **Visualizations**: Charts and maps
- **Conclusions**: Insights and recommendations

### Export Formats

Export reports as:

- **PDF**: Formatted document
- **HTML**: Web-viewable report
- **Word**: Editable document
- **PowerPoint**: Presentation slides

## Step 8: Export Data

### Export Options

Export results data:

1. Select data to export
2. Choose export format
3. Configure export options
4. Download exported file

### Export Formats

**CSV**:
- Building-level results
- Time series data
- Summary statistics

**GeoJSON**:
- Spatial results
- Building geometries
- Attribute data

**JSON**:
- Complete results structure
- Machine-readable format
- API integration

**Excel**:
- Multiple sheets
- Formatted tables
- Charts included

## Step 9: Advanced Analysis

### Statistical Analysis

Perform statistical analysis:

- **Correlation**: Relationships between variables
- **Regression**: Predictive models
- **Clustering**: Group similar buildings
- **Outlier detection**: Identify anomalies

### Custom Calculations

Create custom metrics:

1. Define calculation formula
2. Apply to results
3. View calculated values
4. Export custom metrics

## Common Tasks

### Finding High Consumers

1. Sort by energy consumption
2. Filter top consumers
3. Analyze characteristics
4. Identify improvement opportunities

### Identifying Patterns

1. Group by building characteristics
2. Compare group averages
3. Identify patterns
4. Generate insights

### Validating Results

1. Compare with expectations
2. Check for outliers
3. Verify consistency
4. Validate against measured data

## Best Practices

1. **Start with summary**: Get overview before details
2. **Use filters**: Focus on relevant subsets
3. **Create visualizations**: Charts reveal patterns
4. **Document findings**: Record insights
5. **Export for backup**: Keep copies of results

## Tips for Effective Analysis

### Exploration

- **Drill down**: Start broad, then focus
- **Compare**: Always compare with baseline
- **Visualize**: Use charts and maps
- **Question**: Challenge assumptions

### Presentation

- **Simplify**: Focus on key messages
- **Visualize**: Use charts over tables
- **Context**: Provide background
- **Actionable**: Include recommendations

## Next Steps

After analyzing results:

- [Scenario Design](scenario-design-simulation.md) - Create new scenarios
- [Running and Calibrating](running-calibrating.md) - Refine models
- [Workflows Guide](../workflows.md) - Other workflows

## Related Documentation

- [Input Output Guide](../input-output.md) - Export formats
- [Objects Reference](../objects/datahub.md) - Data model
- [FAQ](../../resources/faq.md) - Common questions
