# Weather File (Datahub Entry)

Reference documentation for Weather File entries in EnergyAtlas Datahub.

## Overview

Weather File entries store weather data used for energy simulations. EnergyAtlas supports standard weather file formats including EPW (EnergyPlus Weather) and TMY3 (Typical Meteorological Year 3).

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the weather file entry
- Format: UUID or custom identifier

**type** (string, required)
- Entry type, must be "weather_file"
- Value: "weather_file"

**name** (string, required)
- Human-readable name
- Example: "New York City TMY3"

**description** (string, optional)
- Description of the weather file
- Example: "Typical Meteorological Year 3 data for NYC"

**file_path** (string, required)
- Path to weather file
- Can be local file or URL

**file_format** (string, required)
- Weather file format
- Values: "EPW", "TMY3", "CSV"

**location** (object, required)
- Geographic location of weather station
- See location structure below

**period** (object, required)
- Time period covered by weather data
- See period structure below

**metadata** (object, optional)
- Additional metadata
- Station ID, elevation, source, etc.

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Location Structure

```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "elevation": 10,
  "timezone": "America/New_York",
  "city": "New York",
  "state": "NY",
  "country": "USA"
}
```

## Period Structure

```json
{
  "start_date": "2020-01-01",
  "end_date": "2020-12-31",
  "data_points": 8760,
  "time_step": "hourly"
}
```

## Example Entry

```json
{
  "id": "weather_001",
  "type": "weather_file",
  "name": "New York City TMY3",
  "description": "Typical Meteorological Year 3 data",
  "file_path": "/weather/us_ny_new-york.epw",
  "file_format": "EPW",
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "elevation": 10,
    "timezone": "America/New_York",
    "city": "New York",
    "state": "NY",
    "country": "USA"
  },
  "period": {
    "start_date": "2020-01-01",
    "end_date": "2020-12-31",
    "data_points": 8760,
    "time_step": "hourly"
  },
  "metadata": {
    "station_id": "725030",
    "source": "NREL",
    "wmo_number": "72503"
  }
}
```

## Supported Formats

### EPW Format

**Extension**: `.epw`
**Source**: EnergyPlus weather files
**Structure**: Comma-separated values with header

**Required Data**:
- Dry bulb temperature
- Dew point temperature
- Relative humidity
- Atmospheric pressure
- Extraterrestrial horizontal radiation
- Extraterrestrial direct normal radiation
- Horizontal infrared radiation
- Global horizontal radiation
- Direct normal radiation
- Diffuse horizontal radiation
- Wind direction
- Wind speed
- Sky cover

### TMY3 Format

**Extension**: `.tmy3` or `.csv`
**Source**: NREL Typical Meteorological Year 3
**Structure**: CSV format

**Characteristics**:
- Representative year data
- Selected from 30-year period
- Typical conditions, not actual year

### CSV Format

**Extension**: `.csv`
**Custom format**: User-defined structure

**Required Columns**:
- Timestamp or date/time
- Temperature data
- Solar radiation data
- Wind data

## Operations

### Create Entry

```json
POST /api/datahubs/{datahub_id}/entries
{
  "type": "weather_file",
  "name": "NYC Weather",
  "file_path": "/path/to/file.epw",
  "file_format": "EPW",
  "location": {...},
  "period": {...}
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
  "file_path": "/new/path/to/file.epw",
  "metadata": {...}
}
```

### Delete Entry

```json
DELETE /api/datahubs/{datahub_id}/entries/{entry_id}
```

### Validate File

```json
POST /api/datahubs/{datahub_id}/entries/{entry_id}/validate
```

## Usage Examples

### Adding Weather File from Library

1. Navigate to Datahub
2. Select datahub
3. Click "Add Entry"
4. Choose "Weather File"
5. Select "From Library"
6. Search for location
7. Select weather file
8. Save entry

### Uploading Custom Weather File

1. Navigate to Datahub
2. Select datahub
3. Click "Add Entry"
4. Choose "Weather File"
5. Select "Upload File"
6. Choose file (EPW or TMY3)
7. Enter location information
8. Save entry

### Linking Weather to Project

1. Navigate to Project Settings
2. Select "Weather Data"
3. Choose weather file from datahub
4. Link to project
5. Verify weather data covers project area

## Weather Data Sources

### NREL

**Source**: National Renewable Energy Laboratory
**Format**: EPW, TMY3
**Coverage**: United States and international
**URL**: https://www.nrel.gov/grid/solar-resource/renewable-resource-data.html

### EnergyPlus

**Source**: EnergyPlus weather data
**Format**: EPW
**Coverage**: Worldwide
**URL**: https://energyplus.net/weather

### Custom Sources

- Local weather stations
- Custom measurements
- Climate model outputs

## Best Practices

1. **Match location**: Use weather data from nearby station
2. **Verify format**: Ensure file format is supported
3. **Check period**: Verify data covers simulation period
4. **Validate data**: Check for missing or invalid values
5. **Document source**: Record weather data source

## Validation

### File Validation

- **Format check**: Verify file format matches specification
- **Data completeness**: Check for missing data points
- **Value ranges**: Validate data within reasonable ranges
- **Time continuity**: Verify time series is continuous

### Location Validation

- **Coordinate check**: Verify latitude/longitude are valid
- **Elevation**: Check elevation is reasonable
- **Timezone**: Verify timezone matches location

## Common Issues

### Issue: File Format Not Recognized

**Solutions**:
- Verify file extension
- Check file format matches specification
- Convert to supported format if needed

### Issue: Missing Data Points

**Solutions**:
- Check file completeness
- Use interpolation if acceptable
- Find alternative weather file

### Issue: Location Mismatch

**Solutions**:
- Verify weather station location
- Use nearest available station
- Consider distance impact on accuracy

## Related Objects

- [Datahub](datahub.md) - Parent datahub object
- [Geospatial Data](geospatial-data.md) - Location data

## References

- [Weather Library](../../resources/weather-library.md) - Available weather files
- [Running and Calibrating Workflow](../workflows/running-calibrating.md) - Using weather data
