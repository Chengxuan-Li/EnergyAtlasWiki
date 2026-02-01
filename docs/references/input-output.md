# Input Output Guide

Comprehensive guide to data import, export, and file formats in EnergyAtlas.

## Overview

EnergyAtlas supports multiple data formats for input and output. This guide details supported formats, import procedures, export options, and data structures.

## Input Formats

### Building Data

#### GeoJSON

**Format**: GeoJSON FeatureCollection
**Extension**: `.geojson`
**Best for**: Geospatial building data with attributes

**Structure**:
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[lon, lat], ...]]
      },
      "properties": {
        "building_id": "unique_id",
        "building_type": "Residential",
        "year_built": 1985,
        "floor_area": 1200
      }
    }
  ]
}
```

#### CSV

**Format**: Comma-separated values
**Extension**: `.csv`
**Best for**: Tabular data with coordinates

**Required columns**:
- `building_id`, `latitude`, `longitude`, `building_type`, `year_built`

**Example**:
```csv
building_id,latitude,longitude,building_type,year_built,floor_area
B001,40.7128,-74.0060,Residential,1985,1200
```

#### Shapefile

**Format**: ESRI Shapefile
**Extensions**: `.shp`, `.shx`, `.dbf`, `.prj`
**Best for**: GIS workflows

**Requirements**:
- All associated files must be present
- Attribute table must contain required fields
- Coordinate reference system should be specified

### Weather Data

#### EPW Format

**Format**: EnergyPlus Weather File
**Extension**: `.epw`
**Best for**: EnergyPlus simulations

**Source**: EnergyPlus weather data repository or custom files

#### TMY3 Format

**Format**: Typical Meteorological Year 3
**Extension**: `.tmy3` or `.csv`
**Best for**: Representative year simulations

### Archetype Data

#### JSON Format

**Format**: JSON object definitions
**Extension**: `.json`
**Best for**: Custom archetype definitions

**Structure**:
```json
{
  "archetype_id": "Residential_Pre1980_Small",
  "building_type": "Residential",
  "vintage": "Pre1980",
  "size": "Small",
  "parameters": {
    "wall_u_value": 1.2,
    "roof_u_value": 0.8,
    "window_u_value": 5.0
  }
}
```

## Output Formats

### Simulation Results

#### CSV Export

**Format**: Comma-separated values
**Extension**: `.csv`
**Contains**: Building-level results, time series data

**Columns**:
- Building identifiers
- Energy consumption (heating, cooling, total)
- Peak demand values
- Monthly/annual summaries

#### GeoJSON Export

**Format**: GeoJSON FeatureCollection
**Extension**: `.geojson`
**Contains**: Spatial results with building geometries

**Use cases**:
- Mapping results in GIS software
- Web visualization
- Spatial analysis

#### JSON Export

**Format**: Structured JSON
**Extension**: `.json`
**Contains**: Complete simulation results

**Structure**:
```json
{
  "simulation_id": "sim_001",
  "buildings": [
    {
      "building_id": "B001",
      "results": {
        "annual_energy": 15000,
        "monthly": [...]
      }
    }
  ]
}
```

### Reports

#### PDF Reports

**Format**: Portable Document Format
**Extension**: `.pdf`
**Contains**: Formatted summary reports

**Includes**:
- Executive summary
- Key findings
- Charts and visualizations
- Methodology notes

#### HTML Reports

**Format**: Interactive HTML
**Extension**: `.html`
**Contains**: Web-viewable reports with interactive charts

## Import Procedures

### Building Data Import

1. **Prepare Data**: Ensure data meets format requirements
2. **Upload File**: Use import interface to upload file
3. **Field Mapping**: Map your fields to EnergyAtlas fields
4. **Preview**: Review imported data preview
5. **Validate**: Run data validation checks
6. **Import**: Complete import process

### Weather Data Import

1. **Select Location**: Choose weather station or upload custom file
2. **Verify Format**: Ensure file is valid EPW or TMY3
3. **Import**: Upload and process weather data
4. **Link**: Associate weather data with project

### Archetype Import

1. **Prepare Definition**: Create archetype JSON definition
2. **Upload**: Import archetype file
3. **Validate**: Check parameter completeness
4. **Add to Library**: Save to archetype library

## Export Procedures

### Exporting Results

1. **Select Buildings**: Choose buildings to export
2. **Choose Format**: Select CSV, GeoJSON, or JSON
3. **Select Variables**: Choose which results to include
4. **Export**: Download exported file

### Exporting Reports

1. **Generate Report**: Create report from results
2. **Customize**: Select sections and visualizations
3. **Export**: Download PDF or HTML report

## Data Structures

### Building Object Structure

```json
{
  "building_id": "string",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[number, number]]]
  },
  "properties": {
    "building_type": "string",
    "year_built": "number",
    "floor_area": "number",
    "num_floors": "number"
  }
}
```

### Results Structure

```json
{
  "building_id": "string",
  "simulation_id": "string",
  "annual_energy": {
    "heating": "number",
    "cooling": "number",
    "total": "number"
  },
  "monthly": [
    {
      "month": "number",
      "heating": "number",
      "cooling": "number"
    }
  ]
}
```

## File Size Limits

- **Building Data**: Up to 100,000 buildings per import
- **Weather Files**: Standard EPW/TMY3 size (~1MB)
- **Archetype Files**: No practical limit
- **Export Files**: Limited by available disk space

## Best Practices

1. **Use GeoJSON**: Preferred format for geospatial data
2. **Validate Before Import**: Check data quality first
3. **Backup Exports**: Keep copies of exported results
4. **Document Formats**: Note which format version used
5. **Compress Large Files**: Use ZIP for large datasets

## Troubleshooting

### Import Errors

- **Format Issues**: Verify file format matches specification
- **Missing Fields**: Check all required fields are present
- **Invalid Geometry**: Repair geometries before import
- **Encoding Issues**: Ensure UTF-8 encoding for text files

### Export Issues

- **Large Files**: Use filters to reduce export size
- **Format Errors**: Verify selected format is supported
- **Missing Data**: Check simulation completed successfully

## Related Documentation

- [Data Preparation](data-prep.md) - Preparing data for import
- [Workflows Guide](workflows.md) - Step-by-step workflows
- [Objects Reference](objects/datahub.md) - Data model documentation
