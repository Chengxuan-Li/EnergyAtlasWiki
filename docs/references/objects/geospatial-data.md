# Geospatial Data (Datahub Entry)

Reference documentation for Geospatial Data entries in EnergyAtlas Datahub.

## Overview

Geospatial Data entries store geographic and spatial information in the Datahub. These entries can represent building footprints, district boundaries, or other geographic features used in energy modeling.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the entry
- Format: UUID or custom identifier

**type** (string, required)
- Entry type, must be "geospatial_data"
- Value: "geospatial_data"

**name** (string, required)
- Human-readable name
- Example: "Building Footprint B001"

**description** (string, optional)
- Description of the geospatial data

**geometry** (object, required)
- Geographic geometry (GeoJSON format)
- See geometry structure below

**properties** (object, required)
- Attribute properties
- Can include building characteristics, IDs, etc.

**crs** (string, optional)
- Coordinate Reference System
- Format: EPSG code (e.g., "EPSG:4326")
- Default: WGS84 (EPSG:4326)

**created_at** (datetime, required)
- Creation timestamp

**updated_at** (datetime, required)
- Last update timestamp

## Geometry Structure

### Supported Geometry Types

**Point**
```json
{
  "type": "Point",
  "coordinates": [longitude, latitude]
}
```

**Polygon** (Building footprint)
```json
{
  "type": "Polygon",
  "coordinates": [[[lon1, lat1], [lon2, lat2], [lon3, lat3], [lon1, lat1]]]
}
```

**MultiPolygon**
```json
{
  "type": "MultiPolygon",
  "coordinates": [[[[lon1, lat1], ...]]]
}
```

## Example Entry

```json
{
  "id": "geo_001",
  "type": "geospatial_data",
  "name": "Building B001",
  "description": "Residential building footprint",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-74.0060, 40.7128],
      [-74.0058, 40.7128],
      [-74.0058, 40.7130],
      [-74.0060, 40.7130],
      [-74.0060, 40.7128]
    ]]
  },
  "properties": {
    "building_id": "B001",
    "building_type": "Residential",
    "year_built": 1985,
    "floor_area": 1200
  },
  "crs": "EPSG:4326"
}
```

## Operations

### Create Entry

```json
POST /api/datahubs/{datahub_id}/entries
{
  "type": "geospatial_data",
  "name": "Building B001",
  "geometry": {...},
  "properties": {...}
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
  "geometry": {...},
  "properties": {...}
}
```

### Delete Entry

```json
DELETE /api/datahubs/{datahub_id}/entries/{entry_id}
```

## Usage Examples

### Creating Building Footprint

1. Navigate to Datahub
2. Select datahub
3. Click "Add Entry"
4. Choose "Geospatial Data"
5. Enter geometry (coordinates or upload GeoJSON)
6. Add properties
7. Save entry

### Importing Multiple Entries

1. Prepare GeoJSON file with multiple features
2. Navigate to Datahub
3. Click "Import"
4. Select GeoJSON file
5. Map fields to properties
6. Import entries

### Updating Geometry

1. Select geospatial data entry
2. Click "Edit"
3. Modify geometry coordinates
4. Save changes

## Geometry Validation

### Requirements

- **Valid coordinates**: Within valid ranges
- **Closed polygons**: First and last points must match
- **No self-intersections**: Polygon edges must not cross
- **Right-hand rule**: Exterior ring counter-clockwise

### Common Issues

**Invalid Polygon**:
- Fix: Ensure first and last coordinates match
- Fix: Check coordinate order

**Self-Intersection**:
- Fix: Simplify geometry
- Fix: Repair using GIS tools

**Wrong CRS**:
- Fix: Specify correct CRS
- Fix: Transform coordinates if needed

## Best Practices

1. **Use GeoJSON**: Preferred format for geospatial data
2. **Validate geometry**: Check geometry validity
3. **Specify CRS**: Always include coordinate reference system
4. **Store properties**: Include relevant attributes
5. **Simplify when needed**: Reduce complexity for large datasets

## Coordinate Reference Systems

### Common CRS

**WGS84** (EPSG:4326)
- Geographic coordinates (lat/lon)
- Default for EnergyAtlas
- Use for most cases

**Web Mercator** (EPSG:3857)
- Web mapping standard
- Use for web visualizations

**Local CRS**
- Project-specific systems
- Specify EPSG code

## Related Objects

- [Datahub](datahub.md) - Parent datahub object
- [Weather File](weather-file.md) - Weather data entries

## References

- [Data Preparation](../data-prep.md) - Preparing geospatial data
- [Urban Data Integration Workflow](../workflows/urban-data-integration.md) - Importing data
