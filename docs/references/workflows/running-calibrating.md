# Running and Calibrating

Workflow for executing energy simulations and calibrating models to match measured consumption data.

## Overview

Running simulations generates energy consumption estimates for your building stock. Calibration adjusts model parameters to better match observed consumption patterns, improving model accuracy.

## Prerequisites

- Building data imported
- Archetypes assigned to buildings
- Weather data available
- (Optional) Measured consumption data for calibration

## Step 1: Configure Simulation Parameters

### Select Buildings

1. Navigate to **Simulation** section
2. Select buildings or building groups to simulate
3. Verify selected buildings have assigned archetypes
4. Review building count and characteristics

### Set Simulation Period

Choose simulation timeframe:

- **Annual**: Full calendar year (recommended)
- **Monthly**: Specific months
- **Custom**: Define start and end dates

### Select Weather Data

1. Choose weather file:
   - Use default weather for location
   - Select from weather library
   - Upload custom weather file
2. Verify weather file covers simulation period
3. Check weather file location matches project area

### Configure Simulation Options

Set simulation parameters:

- **Time step**: Hourly (default) or sub-hourly
- **Output variables**: Select desired outputs
- **Convergence criteria**: Set tolerance levels
- **Simulation engine**: EnergyPlus or simplified model

## Step 2: Review Configuration

### Check Settings

1. Review selected buildings
2. Verify archetype assignments
3. Confirm weather data selection
4. Check simulation parameters

### Estimate Runtime

1. Review building count
2. Check estimated simulation time
3. Consider computational resources
4. Plan for simulation completion

## Step 3: Submit Simulation

### Start Simulation

1. Click **Run Simulation** or **Submit**
2. Confirm simulation parameters
3. Monitor simulation queue status
4. Note simulation job ID

### Monitor Progress

1. Check simulation status
2. Review progress indicators
3. Monitor for errors or warnings
4. Wait for completion

## Step 4: Review Initial Results

### Check Completion

1. Verify simulation completed successfully
2. Review any warnings or errors
3. Check result file availability
4. Validate output data

### Initial Analysis

1. Review summary statistics
2. Check energy consumption ranges
3. Identify any outliers
4. Compare with expectations

## Step 5: Compare with Measured Data (If Available)

### Import Measured Data

1. Prepare measured consumption data
2. Import into EnergyAtlas
3. Link to corresponding buildings
4. Verify data alignment

### Compare Results

1. Calculate differences:
   - **CV(RMSE)**: Coefficient of Variation of RMSE
   - **NMBE**: Normalized Mean Bias Error
   - **R²**: Coefficient of determination
2. Identify systematic differences
3. Note buildings with large discrepancies
4. Analyze patterns in differences

## Step 6: Calibrate Model

### Identify Calibration Needs

Determine what to adjust:

- **Archetype parameters**: U-values, efficiencies
- **Building characteristics**: Floor area, occupancy
- **Operational parameters**: Schedules, setpoints
- **System parameters**: HVAC efficiency, equipment loads

### Adjust Parameters

1. Select buildings or archetypes to calibrate
2. Modify relevant parameters
3. Document parameter changes
4. Save calibration adjustments

### Re-run Simulation

1. Submit calibrated simulation
2. Wait for completion
3. Compare new results with measured data
4. Evaluate improvement

## Step 7: Validate Calibration

### Check Calibration Metrics

Target values for calibrated models:

- **CV(RMSE)**: < 30% for monthly, < 15% for annual
- **NMBE**: < 10%
- **R²**: > 0.75

### Review Results

1. Compare calibrated vs. measured
2. Check for improved agreement
3. Verify calibration is reasonable
4. Identify remaining discrepancies

### Iterate if Needed

If calibration not satisfactory:

1. Analyze remaining differences
2. Adjust additional parameters
3. Re-run simulation
4. Re-validate

## Step 8: Document Calibration

### Record Changes

Document:

- Original parameter values
- Calibrated parameter values
- Rationale for changes
- Calibration metrics achieved

### Save Configuration

1. Save calibrated archetype parameters
2. Export calibration report
3. Document in project notes
4. Create calibration summary

## Common Issues and Solutions

### Issue: Simulation Fails

**Solutions**:
- Check archetype assignments are complete
- Verify weather file is valid
- Review error messages
- Check computational resources

### Issue: Results Seem Unreasonable

**Solutions**:
- Verify archetype assignments
- Check building data accuracy
- Review weather data
- Validate simulation parameters

### Issue: Poor Calibration Fit

**Solutions**:
- Check measured data quality
- Review archetype appropriateness
- Consider building-specific factors
- Adjust multiple parameters

### Issue: Calibration Overfitting

**Solutions**:
- Use reasonable parameter ranges
- Validate on independent data
- Avoid excessive parameter adjustments
- Document all changes

## Best Practices

1. **Start with defaults**: Use default parameters initially
2. **Calibrate incrementally**: Make small, documented changes
3. **Validate independently**: Test on data not used for calibration
4. **Document everything**: Record all parameter changes
5. **Be reasonable**: Keep parameters within realistic ranges

## Calibration Strategies

### Whole-Building Calibration

- Adjust archetype-level parameters
- Apply to all buildings of type
- Good for consistent building stock

### Building-Specific Calibration

- Adjust individual building parameters
- More accurate but time-consuming
- Use for important or outlier buildings

### Hybrid Approach

- Calibrate archetypes for typical buildings
- Manually adjust outliers
- Balance accuracy and efficiency

## Next Steps

After calibration:

- [Scenario Design and Simulation](scenario-design-simulation.md) - Create retrofit scenarios
- [Results View](results-view.md) - Analyze and visualize results
- [Workflows Guide](../workflows.md) - Other workflows

## Related Documentation

- [Archetype Object](../objects/archetype.md) - Archetype parameters
- [Weather File](../objects/weather-file.md) - Weather data specifications
- [FAQ](../../resources/faq.md) - Common questions
