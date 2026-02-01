# Urban Data Integration

Step-by-step workflow for importing and integrating urban building data into EnergyAtlas.

## Overview

Urban data integration is the first step in any EnergyAtlas project. This workflow guides you through importing building data, validating it, and preparing it for archetype assignment and simulation.

## Prerequisites

Before starting, ensure you have:

- Building data in a supported format (GeoJSON, CSV, or Shapefile)
- Required fields populated (building_id, location, building_type, year_built)
- Data quality checked and cleaned
- Access to EnergyAtlas platform

## Step 1: Prepare Your Data

### Data Format

Choose an appropriate format:

- **GeoJSON**: Best for geospatial data with complex geometries
- **CSV**: Simple tabular data with coordinates
- **Shapefile**: Standard GIS format

### Required Fields

Verify your data includes:

- `building_id`: Unique identifier
- Location data: Either coordinates (lat/lon) or geometry
- `building_type`: Building classification
- `year_built`: Construction year

### Data Quality

Perform quality checks:

- No duplicate building IDs
- Valid coordinates or geometries
- Consistent building type values
- Reasonable year built values
- Complete required fields

## Step 2: Access Data Import

1. Log into EnergyAtlas
2. Navigate to **Datahub** section
3. Click **Import Data** or **Add Data**
4. Select **Building Data** import type

## Step 3: Upload Data File

1. Click **Choose File** or drag-and-drop file
2. Select your prepared data file
3. Wait for upload to complete
4. Verify file appears in upload list

## Step 4: Configure Import Settings

### Field Mapping

Map your data fields to EnergyAtlas fields:

- Match `building_id` field
- Map location fields (lat/lon or geometry)
- Map `building_type` field
- Map `year_built` field
- Map optional fields (floor_area, num_floors, etc.)

### Import Options

Configure import behavior:

- **Duplicate handling**: Skip, update, or create new
- **Validation level**: Strict or lenient
- **Default values**: For missing optional fields
- **Coordinate system**: Specify CRS if needed

## Step 5: Preview Data

1. Review data preview table
2. Check sample records
3. Verify field mappings are correct
4. Identify any issues or warnings

## Step 6: Validate Data

Run validation checks:

- **Completeness**: All required fields present
- **Format**: Values match expected formats
- **Ranges**: Numeric values within reasonable ranges
- **Spatial**: Valid geometries or coordinates
- **Consistency**: No conflicting values

### Address Validation Issues

If validation finds issues:

1. Review error messages
2. Fix issues in source data if possible
3. Adjust import settings if appropriate
4. Re-validate after fixes

## Step 7: Complete Import

1. Review import summary
2. Confirm number of buildings to import
3. Click **Import** or **Confirm Import**
4. Wait for import to complete
5. Review import results

## Step 8: Verify Imported Data

### Check Datahub

1. Navigate to **Datahub**
2. Locate imported dataset
3. Verify building count matches expected
4. Review sample records

### Visual Inspection

1. Open map view
2. Verify buildings appear in correct locations
3. Check for spatial issues
4. Identify any missing or misplaced buildings

## Step 9: Link Additional Data (Optional)

### Weather Data

1. Import or select weather file
2. Link weather data to project
3. Verify weather data covers project area

### Other Datasets

- Link energy consumption data for calibration
- Add building attribute data
- Import retrofit measure definitions

## Common Issues and Solutions

### Issue: Import Fails

**Solutions**:
- Check file format matches specification
- Verify all required fields are present
- Check file size limits
- Review error messages for specific issues

### Issue: Missing Buildings

**Solutions**:
- Check for duplicate building IDs
- Verify coordinate ranges are valid
- Check for invalid geometries
- Review import logs for skipped records

### Issue: Incorrect Locations

**Solutions**:
- Verify coordinate system (CRS)
- Check for coordinate order (lat/lon vs lon/lat)
- Validate coordinate ranges
- Review geometry validity

### Issue: Field Mapping Errors

**Solutions**:
- Verify field names match exactly
- Check for case sensitivity
- Review data preview for actual field names
- Adjust field mappings

## Best Practices

1. **Prepare data thoroughly**: Clean data before import saves time
2. **Validate early**: Check data quality before processing
3. **Document sources**: Keep track of data sources and assumptions
4. **Backup originals**: Keep original data files before import
5. **Test with sample**: Import small sample first to verify process

## Next Steps

After successfully importing data:

- [Template Definition and Assignment](template-definition-assignment.md) - Assign archetypes to buildings
- [Data Preparation](../data-prep.md) - Learn more about data requirements
- [Objects Reference](../objects/datahub.md) - Understand data model

## Related Documentation

- [Input Output Guide](../input-output.md) - File formats and structures
- [Datahub Object](../objects/datahub.md) - Datahub documentation
- [Geospatial Data](../objects/geospatial-data.md) - Geospatial data specifications
