# Enums Reference

This page centralizes the enum value sets referenced across the documentation.
For the GeoJSON input/output schema, see [Input / Output Reference](input-output.md).

## `DOEBuildingType`

Building program / archetype selector.

| Value | Notes |
|---|---|
| `UNDEFINED` | Default/unknown. |
| `NONE` | Explicitly “no archetype”. |
| `FullServiceRestaurant` |  |
| `Hospital` |  |
| `LargeHotel` |  |
| `LargeOffice` |  |
| `MediumOffice` |  |
| `MidriseApartment` | Residential; aligns with RECS `typehuq = 5` (5+ units). |
| `HighriseApartment` | Residential; aligns with RECS `typehuq = 5` (5+ units). |
| `OutPatient` |  |
| `PrimarySchool` |  |
| `QuickServiceRestaurant` |  |
| `SecondarySchool` |  |
| `SmallHotel` |  |
| `SmallOffice` |  |
| `StandaloneRetail` |  |
| `StripMall` |  |
| `SuperMarket` |  |
| `Warehouse` |  |
| `SingleFamilyDetached` | Residential; RECS `typehuq = 2`. |
| `SingleFamilyAttached` | Residential; RECS `typehuq = 3`. |
| `MultiFamilyResidential` | Residential; RECS `typehuq = 4` (2–4 units). |
| `MobileHome` | Residential; RECS `typehuq = 1`. |
| `OtherCommercial` |  |
| `OtherIndustrial` |  |

### RECS `typehuq` reference (residential)

Source: [RECS 2020 documentation (PDF)](https://back.nber.org/appendix/c14876/Davis%20NBER%20EEPE%202023%20Data%20Archive/raw%20data/RECS%20Documentation/2020_RECS-457A.pdf)

| `typehuq` | Meaning |
|---:|---|
| -1 | Non-residential use |
| 1 | Mobile home |
| 2 | Single-family detached |
| 3 | Single-family attached (duplex/row/townhome) |
| 4 | Apartment, 2–4 units |
| 5 | Apartment, 5+ units |

## `SystemOptions`

HVAC system type selector.

| Value | Int | Notes |
|---|---:|---|
| `None` | 0 | No system |
| `CustomSystem` | 1 | User-specified COP & fuel |
| `ElectricHeating` | 11 | Electric resistance |
| `BoilerOld` | 21 | Low-efficiency boiler |
| `BoilerMed` | 31 | Medium-efficiency boiler |
| `BoilerNew` | 41 | High-efficiency boiler |
| `HeatPumpAir` | 71 | Air-source heat pump |
| `HeatPumpWater` | 75 | Water-source heat pump |
| `CHP` | 78 | Combined heat & power |
| `DistrictSystem` | 79 | District heating/cooling |

## `Fuel`

Fuel type selector.

| Value | Notes |
|---|---|
| `Electricity` |  |
| `Gas` |  |
| `FuelOil` |  |
| `Coal` |  |
| `Gasoline` |  |
| `Propane` |  |
| `Diesel` |  |
| `Wood` |  |
| `District` | District energy (heating/cooling). |
| `NA` | Not applicable / unknown. |

## `CapacityClass`

Thermal mass class selector.

| Value | Notes |
|---|---|
| `VeryLight` |  |
| `Light` |  |
| `Medium` |  |
| `Heavy` |  |
| `VeryHeavy` |  |

## `GlazingOptions`

Glazing preset selector.

| Value | Notes |
|---|---|
| `SinglePaneClr` | Single pane, clear. |
| `DoublePaneClr` | Double pane, clear. |
| `DoublePaneLoEe2` | Double pane, low-e (variant e2). |
| `DoublePaneLoEe3` | Double pane, low-e (variant e3). |
| `TriplePaneLoE` | Triple pane, low-e. |