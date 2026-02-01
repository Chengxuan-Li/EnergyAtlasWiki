# Datahub

Reference documentation for the Datahub object in EnergyAtlas.

## Overview

The Datahub is the central repository for all data in an EnergyAtlas project. It stores building data, geospatial information, weather files, archetypes, retrofit measures, and other project assets.

## Object Structure

### Properties

**id** (string, required)
- Unique identifier for the datahub
- Format: UUID or custom identifier

**name** (string, required)
- Human-readable name for the datahub
- Example: "New York City Building Stock"

**description** (string, optional)
- Description of the datahub contents
- Provides context about the dataset

**created_at** (datetime, required)
- Timestamp when datahub was created
- Format: ISO 8601

**updated_at** (datetime, required)
- Timestamp of last update
- Format: ISO 8601

**entries** (array, required)
- List of datahub entries (buildings, weather files, etc.)
- See entry types below

## Entry Types

### Building Entries

Stores building data:

```json
{
  "type": "building",
  "id": "building_001",
  "data": {
    "building_id": "B001",
    "geometry": {...},
    "properties": {...}
  }
}
```

### Weather File Entries

Stores weather data:

```json
{
  "type": "weather_file",
  "id": "weather_001",
  "data": {
    "file_path": "...",
    "location": {...},
    "period": {...}
  }
}
```

### Geospatial Data Entries

Stores geographic data:

```json
{
  "type": "geospatial_data",
  "id": "geo_001",
  "data": {
    "geometry": {...},
    "properties": {...}
  }
}
```

## Operations

### Create Datahub

```json
POST /api/datahubs
{
  "name": "Project Datahub",
  "description": "Main datahub for project"
}
```

### Add Entry

```json
POST /api/datahubs/{id}/entries
{
  "type": "building",
  "data": {...}
}
```

### List Entries

```json
GET /api/datahubs/{id}/entries
```

### Get Entry

```json
GET /api/datahubs/{id}/entries/{entry_id}
```

### Update Entry

```json
PUT /api/datahubs/{id}/entries/{entry_id}
{
  "data": {...}
}
```

### Delete Entry

```json
DELETE /api/datahubs/{id}/entries/{entry_id}
```

## Usage Examples

### Creating a Datahub

1. Navigate to Datahub section
2. Click "Create New Datahub"
3. Enter name and description
4. Save datahub

### Adding Building Data

1. Select datahub
2. Click "Add Entry"
3. Choose "Building" type
4. Upload or enter building data
5. Save entry

### Importing Multiple Entries

1. Select datahub
2. Click "Import"
3. Choose file format
4. Map fields
5. Import entries

## Best Practices

1. **Organize by project**: Create separate datahubs for different projects
2. **Name clearly**: Use descriptive names
3. **Document entries**: Add descriptions to entries
4. **Version control**: Keep track of datahub versions
5. **Backup regularly**: Export datahub contents

## Related Objects

- [Geospatial Data](geospatial-data.md) - Geographic data entries
- [Weather File](weather-file.md) - Weather data entries
- [Archetype](archetype.md) - Building archetype definitions

## API Reference

Full API documentation available at `/api/docs`
