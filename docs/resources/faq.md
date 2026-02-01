# Frequently Asked Questions

Common questions and troubleshooting for EnergyAtlas.

## General Questions

### What is EnergyAtlas?

EnergyAtlas is a platform for urban building energy modeling (UBEM) that helps users model energy consumption at the district or city scale.

### Who should use EnergyAtlas?

EnergyAtlas is designed for:
- Urban planners
- Energy researchers
- Policy analysts
- Building energy consultants
- Municipal energy managers

## Data Questions

### What data formats are supported?

EnergyAtlas supports:
- Shapefiles (.shp)
- GeoJSON (.geojson)
- CSV files (.csv)
- Building energy data files

### How much data do I need?

Minimum required:
- Building locations (coordinates or geometry)
- Building type
- Construction year
- Floor area (recommended)

### What if my data is incomplete?

EnergyAtlas can handle incomplete data:
- Uses default values for missing fields
- Applies archetype assignment rules
- Flags missing critical data

## Simulation Questions

### How long do simulations take?

Simulation time depends on:
- Number of buildings
- Simulation period
- Model complexity
- Server load

Typical times:
- Small dataset (<100 buildings): Minutes
- Medium dataset (100-1000): 10-30 minutes
- Large dataset (>1000): Hours

### Can I cancel a simulation?

Yes, simulations can be cancelled:
- Use the job management interface
- Cancelled jobs can be restarted
- Partial results may be available

## Calibration Questions

### How accurate are the models?

Model accuracy depends on:
- Data quality
- Archetype selection
- Calibration effort
- Building complexity

Typical accuracy:
- Uncalibrated: ±30-50%
- Calibrated: ±10-20%

### How do I improve accuracy?

- Use high-quality input data
- Calibrate to measured consumption
- Refine archetype assignments
- Adjust model parameters

## Technical Questions

### What simulation engines are used?

EnergyAtlas uses:
- EnergyPlus (detailed simulations)
- Simplified models (fast simulations)
- Hybrid approaches

### Can I export results?

Yes, results can be exported:
- CSV format for tabular data
- GeoJSON for spatial data
- PDF reports
- Interactive visualizations

## Troubleshooting

### Simulation fails to start

Check:
- Data format and completeness
- Required fields present
- File size limits
- Server status

### Results seem incorrect

Verify:
- Input data accuracy
- Archetype assignments
- Weather file selection
- Simulation parameters

### Need more help?

- Check documentation sections
- Review example projects
- Contact support
