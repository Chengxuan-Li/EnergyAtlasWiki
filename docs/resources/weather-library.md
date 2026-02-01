# Weather Library

Comprehensive library of weather data files available in EnergyAtlas.

## Overview

The Weather Library provides access to standard weather files for locations worldwide. These files are used for energy simulations and are available in EPW (EnergyPlus Weather) and TMY3 (Typical Meteorological Year 3) formats.

## Library Sources

### NREL (National Renewable Energy Laboratory)

**Coverage**: United States and international locations
**Formats**: EPW, TMY3
**Quality**: High-quality, validated data
**Access**: Free, public domain

**Website**: https://www.nrel.gov/grid/solar-resource/renewable-resource-data.html

### EnergyPlus Weather Data

**Coverage**: Worldwide
**Formats**: EPW
**Quality**: Standard EnergyPlus format
**Access**: Free, public domain

**Website**: https://energyplus.net/weather

## United States Locations

### Major Cities

**New York, NY**
- Station: LaGuardia Airport
- Formats: EPW, TMY3
- Climate Zone: 4A

**Los Angeles, CA**
- Station: Los Angeles International Airport
- Formats: EPW, TMY3
- Climate Zone: 3B

**Chicago, IL**
- Station: O'Hare International Airport
- Formats: EPW, TMY3
- Climate Zone: 5A

**Houston, TX**
- Station: George Bush Intercontinental Airport
- Formats: EPW, TMY3
- Climate Zone: 2A

**Phoenix, AZ**
- Station: Sky Harbor International Airport
- Formats: EPW, TMY3
- Climate Zone: 2B

### Climate Zones

**Zone 1A**: Very Hot - Humid
- Examples: Miami, FL; Key West, FL

**Zone 2A**: Hot - Humid
- Examples: Houston, TX; New Orleans, LA

**Zone 2B**: Hot - Dry
- Examples: Phoenix, AZ; Las Vegas, NV

**Zone 3A**: Warm - Humid
- Examples: Atlanta, GA; Memphis, TN

**Zone 3B**: Warm - Dry
- Examples: Los Angeles, CA; San Diego, CA

**Zone 3C**: Warm - Marine
- Examples: San Francisco, CA; Seattle, WA

**Zone 4A**: Mixed - Humid
- Examples: New York, NY; Philadelphia, PA

**Zone 4B**: Mixed - Dry
- Examples: Denver, CO; Salt Lake City, UT

**Zone 4C**: Mixed - Marine
- Examples: Portland, OR; Vancouver, BC

**Zone 5A**: Cool - Humid
- Examples: Chicago, IL; Boston, MA

**Zone 5B**: Cool - Dry
- Examples: Boise, ID; Cheyenne, WY

**Zone 6A**: Cold - Humid
- Examples: Minneapolis, MN; Buffalo, NY

**Zone 6B**: Cold - Dry
- Examples: Billings, MT; Fargo, ND

**Zone 7**: Very Cold
- Examples: Fairbanks, AK; International Falls, MN

**Zone 8**: Subarctic
- Examples: Anchorage, AK; Barrow, AK

## International Locations

### Canada

- Toronto, ON
- Vancouver, BC
- Montreal, QC
- Calgary, AB

### Europe

- London, UK
- Paris, France
- Berlin, Germany
- Madrid, Spain
- Rome, Italy

### Asia

- Tokyo, Japan
- Beijing, China
- Mumbai, India
- Singapore
- Seoul, South Korea

### Australia

- Sydney, NSW
- Melbourne, VIC
- Brisbane, QLD
- Perth, WA

## File Formats

### EPW Format

**Extension**: `.epw`
**Structure**: Comma-separated values
**Data**: Hourly weather data
**Period**: Full year (8760 hours)

**Contents**:
- Dry bulb temperature
- Dew point temperature
- Relative humidity
- Atmospheric pressure
- Solar radiation (global, direct, diffuse)
- Wind speed and direction
- Sky cover

### TMY3 Format

**Extension**: `.tmy3` or `.csv`
**Structure**: CSV format
**Data**: Typical meteorological year
**Period**: Representative year

**Characteristics**:
- Selected from 30-year period
- Typical conditions (not actual year)
- Representative of long-term climate
- Suitable for design and planning

## Using the Library

### Searching for Weather Files

1. Navigate to Weather Library
2. Use search or filters:
   - Location name
   - State/Province
   - Country
   - Climate zone
   - Coordinates
3. Browse available files
4. Review file details

### Selecting Weather File

1. Review location information
2. Check climate zone
3. Verify file format
4. Review data period
5. Select appropriate file

### Adding to Project

1. Select weather file
2. Click "Add to Datahub"
3. Choose target datahub
4. Confirm addition
5. Link to project

## Best Practices

1. **Match location**: Use weather data from nearby station
2. **Consider distance**: Closer stations are more accurate
3. **Check elevation**: Similar elevation is preferable
4. **Verify period**: Ensure data covers simulation period
5. **Document source**: Record weather file used

## Custom Weather Files

### Uploading Custom Files

1. Navigate to Datahub
2. Select "Add Entry"
3. Choose "Weather File"
4. Upload EPW or TMY3 file
5. Enter location information
6. Save entry

### Requirements

- Valid EPW or TMY3 format
- Complete data (8760 hours for annual)
- Valid coordinate ranges
- Proper file structure

## Data Quality

### Validation

Weather files are validated for:
- Format compliance
- Data completeness
- Value ranges
- Time continuity

### Quality Indicators

- **Completeness**: Percentage of data present
- **Source**: Data origin and quality
- **Period**: Years of data used
- **Station**: Weather station information

## Climate Data Summary

### Temperature Statistics

- **Average**: Mean annual temperature
- **Minimum**: Coldest month average
- **Maximum**: Warmest month average
- **Range**: Temperature variation

### Solar Radiation

- **Annual**: Total annual solar radiation
- **Peak**: Maximum monthly radiation
- **Seasonal**: Variation by season

### Other Statistics

- Heating degree days
- Cooling degree days
- Precipitation
- Wind patterns

## References

- [Weather File Object](../references/objects/weather-file.md) - Weather file structure
- [Running and Calibrating Workflow](../references/workflows/running-calibrating.md) - Using weather data
- [Input Output Guide](../references/input-output.md) - File formats
