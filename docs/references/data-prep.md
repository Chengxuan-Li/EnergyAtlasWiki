# Data Preparation

Guidelines for preparing and formatting data for use in EnergyAtlas.

## Overview

Proper data preparation is essential for accurate energy modeling. This guide covers data requirements, formats, quality checks, and preprocessing steps needed before importing data into EnergyAtlas.

## Data Requirements

### Minimum Required Fields

Every building record must include:

- **Building ID**: Unique identifier (string or integer)
- **Location**: Geographic coordinates (latitude/longitude) or geometry (GeoJSON)
- **Building Type**: Classification (residential, commercial, mixed-use, etc.)
- **Year Built**: Construction year (integer, YYYY format)

### Recommended Fields

For improved accuracy, include:

- **Floor Area**: Total floor area in square meters or square feet
- **Number of Floors**: Building height information
- **Occupancy Type**: Detailed use classification
- **Building Age**: Calculated from year built
- **Address**: Street address for verification

### Optional Fields

Additional fields that enhance modeling:

- **Roof Type**: Flat, pitched, etc.
- **Wall Material**: Masonry, wood frame, concrete, etc.
- **Window Type**: Single pane, double pane, etc.
- **HVAC Type**: Heating and cooling system information
- **Energy Consumption**: Historical consumption data for calibration

## Supported Data Formats

### GeoJSON

Preferred format for geospatial data:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[...]]
      },
      "properties": {
        "building_id": "B001",
        "building_type": "Residential",
        "year_built": 1985,
        "floor_area": 1200
      }
    }
  ]
}
```

### CSV

Tabular format with geographic coordinates:

```csv
building_id,latitude,longitude,building_type,year_built,floor_area,num_floors
B001,40.7128,-74.0060,Residential,1985,1200,2
B002,40.7130,-74.0062,Commercial,1995,5000,5
```

### Shapefile

Standard GIS format (.shp with associated files):
- Requires .shp, .shx, .dbf, and optionally .prj files
- Attribute table must contain required fields

## Data Quality Checks

### Completeness

- Verify all required fields are populated
- Check for missing values (null, empty strings)
- Identify records with incomplete data

### Consistency

- Validate coordinate ranges (latitude: -90 to 90, longitude: -180 to 180)
- Check building type values against allowed list
- Verify year built is reasonable (e.g., 1800-2025)
- Ensure floor area is positive

### Spatial Validation

- Verify geometries are valid (no self-intersections)
- Check coordinate reference system (CRS)
- Identify duplicate buildings (same location)
- Validate building footprints are reasonable sizes

### Data Cleaning

Common preprocessing steps:

1. **Remove duplicates**: Eliminate duplicate building records
2. **Fix geometries**: Repair invalid polygons
3. **Standardize formats**: Normalize building types, dates
4. **Handle missing data**: Apply defaults or flag for review
5. **Validate ranges**: Check numeric values are within expected ranges

## Preprocessing Workflow

1. **Data Collection**: Gather data from multiple sources
2. **Format Conversion**: Convert to supported format (GeoJSON recommended)
3. **Quality Check**: Run validation checks
4. **Data Cleaning**: Fix identified issues
5. **Field Mapping**: Ensure field names match EnergyAtlas requirements
6. **Export**: Save cleaned data in appropriate format

## Field Mapping

EnergyAtlas expects specific field names. Map your data fields:

| Your Field Name | EnergyAtlas Field | Required |
|----------------|------------------|----------|
| `id` or `building_id` | `building_id` | Yes |
| `lat`, `latitude` | `latitude` | Yes* |
| `lon`, `longitude` | `longitude` | Yes* |
| `type`, `building_type` | `building_type` | Yes |
| `year`, `year_built` | `year_built` | Yes |
| `area`, `floor_area` | `floor_area` | Recommended |
| `floors`, `num_floors` | `num_floors` | Recommended |

*Required if not using geometry

## Best Practices

1. **Start with clean data**: Clean data before import saves time
2. **Document sources**: Keep track of data sources and assumptions
3. **Validate early**: Check data quality before processing
4. **Use consistent formats**: Standardize field names and values
5. **Backup originals**: Keep original data files before preprocessing

## Common Issues

### Missing Coordinates

If coordinates are missing but addresses are available:
- Use geocoding service to obtain coordinates
- Verify geocoded locations are accurate

### Inconsistent Building Types

Standardize building type values:
- Create mapping table for variations
- Use consistent taxonomy (e.g., "Residential", not "Res" or "RES")

### Invalid Geometries

Fix geometry issues:
- Use GIS software to repair invalid polygons
- Simplify complex geometries if needed
- Ensure polygons are closed

## Next Steps

After preparing your data:
- [Input Output Guide](input-output.md) - Learn about data import/export
- [Urban Data Integration](../workflows/urban-data-integration.md) - Import data into EnergyAtlas
