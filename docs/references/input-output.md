# GeoJSON Feature Collection — Input / Output Reference

This document describes every property that the energy simulation model reads from
(and writes to) a GeoJSON **FeatureCollection**. Each feature in the collection
represents a single building footprint.


## Inputs

Inputs are grouped into three categories:

| Category | When used | Purpose |
|---|---|---|
| **Compulsory** | Always | The model cannot run without these fields. |
| **Geometric overrides** | Before simulation (during geometric preprocessing) | Lets you override computed geometry-derived quantities like area, perimeter, facade areas, and floors. |
| **Optional** | After geometric preprocessing | Additional archetype, envelope, HVAC, and calibration inputs. |

See the [Enums Reference](enums.md) for all enum value sets used by the fields in this document.






### Compulsory Inputs

| Property Key | Type | Unit | Default | Description |
|---|---|---:|---|---|
| `SelectForSim_ESL` | boolean | — | `true` | If `false`, the feature is skipped. |
| `YearBuilt_ESL` | int | year | — | Year the building was built (used for archetype / construction assumptions). |
| `BldgHeight_M_ESL` | double | m | — | Building height. Required for geometric preprocessing. |

### Optional Overrides for Geometric Preprocessing
Geometric preprocessing derives building geometry quantities from the footprint geometry and height.
These quantities are used heavily by the energy model (e.g., heat loss depends on exposed surface areas).
If you already have more accurate values, you can provide them to override the preprocessing results.

| Property Key | Type | Unit | Default | Description |
|---|---|---:|---|---|
| `Area_SQM_ESL` | double | m² | — | Footprint area override. |
| `Perimeter_M_ESL` | double | m | — | Footprint perimeter override. |
| `ExposedFacadeArea_SQM_ESL` | double | m² | — | Exterior (exposed) facade area override. |
| `AdiabaticFacadeArea_SQM_ESL` | double | m² | — | Adiabatic (non-exposed / party wall) facade area override. |
| `Floors_ESL` | double | floors | — | Number of floors override. |
### Optional Inputs

#### Identifiers

| Property Key | Type | Unit | Default | Description |
|---|---|---:|---|---|
| `ID_ESL` | string | — | — | Unique feature/building identifier within the FeatureCollection. |
| `ubid` | string | — | — | Optional [UBID](https://www.energy.gov/cmei/buildings/unique-building-identifier-ubid) for building identification. |
| `RESULTGROUP_ID_ESL` | string | — | — | Optional grouping key (e.g., feeder line id, zip code). |

#### Building Info

| Property Key | Type | Unit | Default | Description |
|---|---|---:|---|---|
| `DOEBuildingType` | `DOEBuildingType` | — | `UNDEFINED` | Building program / archetype selector. See [`DOEBuildingType`](enums.md#doebuildingtype). |
| `PostalCode` | string | — | — | Postal / ZIP code. |
| `AddressLine1` | string | — | — | Address line 1. |
| `AddressLine2` | string | — | — | Address line 2. |
| `CityOrCommunity` | string | — | — | City/community name. |
| `Zoning_ESL` | string | — | — | Zoning label/code (free text). |


#### Envelope / Construction

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `roof_UVal[W_m2K]_ESL` | double | W/(m²·K) | `0.4` | Roof U-value. |
| `wall_UVal[W_m2K]_ESL` | double | W/(m²·K) | `0.4` | Exterior wall U-value. |
| `WWR_E_S_W_N_R_ESL` | double[5] | ratio | `[0.4, 0.4, 0.4, 0.4, 0]` | Window-to-wall ratio per orientation: East, South, West, North, Roof. |
| `Glazing_ESL` | `GlazingOptions` | — | `DoublePaneClr` | Glazing type preset. |
| `GlazingUVal_ESL` | double | W/(m²·K) | `2` | Custom glazing U-value (overrides preset). |
| `GlazingSHGC_ESL` | double | — | `0.5` | Solar heat gain coefficient. |
| `infiltr[ACH]_ESL` | double | ACH | `0.5` | Air infiltration rate. |
| `infiltr[m3_s_m2]_ESL` | double | m³/s/m² | `0` | Air infiltration flow rate per exterior surface area. |
| `thermalMassClass_ESL` | `CapacityClass` | — | `Medium` | Thermal mass class of the construction. |

Enum values: see [GlazingOptions](enums.md#glazingoptions) and [CapacityClass](enums.md#capacityclass).



#### HVAC Systems

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `HeatType_ESL` | `SystemOptions` | — | `CustomSystem` | Heating system type. |
| `HeatCOP_ESL` | double | — | `0.8` | Heating coefficient of performance. |
| `HeatFuel_ESL` | `Fuel` | — | `Gas` | Fuel used by the heating system. |
| `CoolType_ESL` | `SystemOptions` | — | `CustomSystem` | Cooling system type. |
| `CoolCOP_ESL` | double | — | `3` | Cooling coefficient of performance. |

Enum values: see [SystemOptions](enums.md#systemoptions) and [Fuel](enums.md#fuel).


#### Domestic Hot Water

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `WaterHeatType_ESL` | string | — | `"Boiler"` | DHW system type label. |
| `DomHotWaterCOP_ESL` | double | — | `0.8` | DHW system COP. |
| `DomHotWaterFuel_ESL` | `Fuel` | — | `Gas` | DHW fuel type. |
| `flowDHW[m3_h_P]_ESL` | double | m³/h/person | `0.0004` | DHW flow rate per person. |
| `dhwFuel_ESL` | `Fuel` | — | `Gas` | Alternate DHW fuel property (overrides `DomHotWaterFuel` when present). |

Enum values: see [Fuel](enums.md#fuel).



#### Space Loads & Setpoints

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `equipPowDen[W_m2]_ESL` | double | W/m² | `10` | Equipment power density. |
| `lightPowDen[W_m2]_ESL` | double | W/m² | `10` | Lighting power density. |
| `peopleDen[P_m2]_ESL` | double | P/m² | `0.1` | Occupant density (people per m²). |
| `gasPowDen[W_m2]_ESL` | double | W/m² | `0` | Gas equipment power density. |
| `heatingSetPoint[degC]_ESL` | double | °C | `21` | Heating thermostat setpoint. |
| `coolingSetPoint[degC]_ESL` | double | °C | `25` | Cooling thermostat setpoint. |




### Photovoltaics [Obsolete]

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `PVGenBenchmark1100[kWh][Yr]` | double | kWh/yr | `0` | Annual PV generation benchmark (at 1100 kWh/m²). |
| `PVAreaBenchmark1100[m2]` | double | m² | `0` | Total PV panel area (at 1100 kWh/m²). |

### Metadata & Permits [Obsolete]

| Property Key | Type | Default | Description |
|---|---|---|---|
| `Construction_ESL` | string | `""` | Construction class label. |
| `Foundation_ESL` | string | `""` | Foundation type. |
| `Roof_ESL` | string | `""` | Roof type label. |
| `Siding_ESL` | string | `""` | Siding material. |
| `PermitPhotovoltaic_ESL` | bool | `false` | Has an active PV permit. |
| `PermitNewWindows_ESL` | bool | `false` | Has a window replacement permit. |
| `PermitHeatPump_ESL` | bool | `false` | Has a heat-pump permit. |
| `PermitInsulation_ESL` | bool | `false` | Has an insulation permit. |
| `Historic_ESL` | bool | `false` | Building is on a historic register. |
| `AnnualHouseholdIncome[$]` | double | `74314` | Annual household income (USD). |

#### Calibration / Validation

Monthly metered data for model calibration. If both arrays are present and pass
quality checks (electricity EUI > 1 kWh/m², gas EUI ≥ 0), the model will run an
auto-calibration step.

| Property Key | Type | Unit | Default | Description |
|---|---|---|---|---|
| `GasMonthlyValidationData_ESL` | double[12] | kWh | `[1×12]` | Monthly metered gas consumption. |
| `ElecMonthlyValidationData_ESL` | double[12] | kWh | `[1×12]` | Monthly metered electricity consumption. |

---

## Output Properties

Outputs are written back onto each feature after simulation. The naming convention
encodes quantity, unit, and temporal resolution: `Name[Unit][Resolution]`.

### Summary

| Output Key | Unit | Resolution | Description |
|---|---|---|---|
| `FloorArea[Sqm]` | m² | — | Computed conditioned floor area. |
| `MaxOcc[P]` | persons | — | Peak occupancy. |

### Billed Energy

| Output Key | Unit | Resolution | Description |
|---|---|---|---|
| `BilledGas[kWh_m2][Yr]` | kWh/m² | annual | Gas EUI (site). |
| `BilledElec[kWh_m2][Yr]` | kWh/m² | annual | Electricity EUI (site). |
| `BilledGas[kWh][Yr]` | kWh | annual | Total billed gas. |
| `BilledElec[kWh][Yr]` | kWh | annual | Total billed electricity. |
| `GasError[%][Yr]` | % | annual | Calibration error — gas. |
| `ElecError[%][Yr]` | % | annual | Calibration error — electricity. |
| `Cost[$][Yr]` | $ | annual | Annual energy cost. |

### CO₂ Emissions

| Output Key | Unit | Resolution |
|---|---|---|
| `CO2[kg][Mth]` | kg | monthly |
| `CO2_Gas[kg][Mth]` | kg | monthly |
| `CO2_Electricity[kg][Mth]` | kg | monthly |
| `CO2_Propane[kg][Mth]` | kg | monthly |
| `CO2_Oil[kg][Mth]` | kg | monthly |
| `CO2_Wood[kg][Mth]` | kg | monthly |
| `CO2_Diesel[kg][Mth]` | kg | monthly |
| `CO2_District[kg][Mth]` | kg | monthly |
| `CO2[kg][Yr]` | kg | annual |
| `CO2_Gas[kg][Yr]` | kg | annual |
| `CO2_Electricity[kg][Yr]` | kg | annual |
| `CO2_Propane[kg][Yr]` | kg | annual |
| `CO2_Oil[kg][Yr]` | kg | annual |
| `CO2_Wood[kg][Yr]` | kg | annual |
| `CO2_Diesel[kg][Yr]` | kg | annual |
| `CO2_District[kg][Yr]` | kg | annual |
| `CO2[kg_m2][Yr]` | kg/m² | annual |

### Fuel Consumption

| Output Key | Unit | Resolution |
|---|---|---|
| `Gas[kWh][Mth]` | kWh | monthly |
| `Electricity[kWh][Mth]` | kWh | monthly |
| `Propane[kWh][Mth]` | kWh | monthly |
| `Oil[kWh][Mth]` | kWh | monthly |
| `Wood[kWh][Mth]` | kWh | monthly |
| `Diesel[kWh][Mth]` | kWh | monthly |
| `District[kWh][Mth]` | kWh | monthly |
| `Gas[kWh][Yr]` | kWh | annual |
| `Electricity[kWh][Yr]` | kWh | annual |
| `Propane[kWh][Yr]` | kWh | annual |
| `Oil[kWh][Yr]` | kWh | annual |
| `Wood[kWh][Yr]` | kWh | annual |
| `Diesel[kWh][Yr]` | kWh | annual |
| `District[kWh][Yr]` | kWh | annual |
| `Gas[kWh_m2][Yr]` | kWh/m² | annual |
| `Electricity[kWh_m2][Yr]` | kWh/m² | annual |

### End-Use Breakdown

| Output Key | Unit | Resolution |
|---|---|---|
| `Heating[KWh][Mth]` | kWh | monthly |
| `Cooling[KWh][Mth]` | kWh | monthly |
| `Equipment[KWh][Mth]` | kWh | monthly |
| `Lighting[KWh][Mth]` | kWh | monthly |
| `HotWater[KWh][Mth]` | kWh | monthly |
| `GasEquipment[KWh][Mth]` | kWh | monthly |
| `Auxiliary[KWh][Mth]` | kWh | monthly |

### Annual Energy Use

| Output Key | Unit | Resolution |
|---|---|---|
| `EnergyUse[KWh][Yr]` | kWh | annual |
| `Heating[KWh][Yr]` | kWh | annual |
| `Cooling[KWh][Yr]` | kWh | annual |
| `Equipment[KWh][Yr]` | kWh | annual |
| `Lighting[KWh][Yr]` | kWh | annual |
| `HotWater[KWh][Yr]` | kWh | annual |
| `GasEquipment[KWh][Yr]` | kWh | annual |
| `Auxiliary[KWh][Yr]` | kWh | annual |

### Energy Use Intensity (EUI)

| Output Key | Unit | Resolution |
|---|---|---|
| `EUI[KWh_m2][Yr]` | kWh/m² | annual |
| `Heating[KWh_m2][Yr]` | kWh/m² | annual |
| `Cooling[KWh_m2][Yr]` | kWh/m² | annual |
| `Equipment[KWh_m2][Yr]` | kWh/m² | annual |
| `Lighting[KWh_m2][Yr]` | kWh/m² | annual |
| `HotWater[KWh_m2][Yr]` | kWh/m² | annual |
| `GasEquipment[KWh_m2][Yr]` | kWh/m² | annual |
| `Auxiliary[KWh_m2][Yr]` | kWh/m² | annual |

### Per-Capita

| Output Key | Unit | Resolution |
|---|---|---|
| `PEPC[KWh_p][Yr]` | kWh/person | annual |
| `CO2PC[kg_p][Yr]` | kg/person | annual |

### Photovoltaics

| Output Key | Unit | Resolution |
|---|---|---|
| `PV[KWh][Yr]` | kWh | annual |
| `PV[KWh][Mth]` | kWh | monthly |
| `PV[KWh_m2][Yr]` | kWh/m² | annual |
| `PV[KWh_p][Yr]` | kWh/person | annual |
| `CO2_ElectricityProduced[kg][Mth]` | kg | monthly |
| `CO2_ElectricityProduced[kg][Yr]` | kg | annual |

### System Performance

| Output Key | Unit | Description |
|---|---|---|
| `SimulatedHeatingCOP` | — | Effective heating COP (after simulation). |
| `SimulatedCoolingCOP` | — | Effective cooling COP (after simulation). |
| `NominalHeatingCOP` | — | Nominal heating COP (input/template). |
| `NominalCoolingCOP` | — | Nominal cooling COP (input/template). |

### Peak Loads

| Output Key | Unit | Description |
|---|---|---|
| `MaxHeatingLoad[kW]` | kW | Design-day peak heating load. |
| `MaxCoolingLoad[kW]` | kW | Design-day peak cooling load. |
| `MaxElectricLoad[kW]` | kW | Peak electric demand. |
| `MaxGasLoad[kW]` | kW | Peak gas demand. |

### Finance

| Output Key | Unit | Resolution | Description |
|---|---|---|---|
| `LoanTerm[Yr]` | years | — | Retrofit loan term. |
| `InterestRate[%][Yr]` | % | annual | Loan interest rate. |
| `AnnualEnergyBillSavings[$][Yr]` | $ | annual | Annual bill savings from retrofit. |
| `MonthlyEnergyBillSavings[$][Mth]` | $ | monthly | Monthly bill savings. |
| `PaybackPeriod[Yr]` | years | — | Simple payback period. |
| `ReturnOnInvestment[%]` | % | — | ROI of retrofit investment. |
| `MonthlyLoanPayment[$][Mth]` | $ | monthly | Loan payment amount. |
| `NetMonthlyLoanPayment[$][Mth]` | $ | monthly | Loan payment minus energy savings. |
| `NetPresentValue(NPV)[$]` | $ | — | Net present value. |
| `BenefitCostRatio[kgCO2][$]` | kg CO₂/$ | — | CO₂ reduced per dollar spent. |
| `BenefitCostRatio[$][$]_LongTerm` | $/$ | — | Long-term financial benefit-cost ratio. |

### Incentives

| Output Key | Unit | Description |
|---|---|---|
| `FederalIncentive[$]` | $ | Federal incentive amount. |
| `StateIncentive[$]` | $ | State incentive amount. |
| `LocalIncentive[$]` | $ | Local/utility incentive amount. |
| `NetUpfrontCost[$]` | $ | Cost after all incentives. |

### Retrofit Costs

| Output Key | Unit | Description |
|---|---|---|
| `EnvelopeUpgradeCost[$]` | $ | Envelope retrofit cost. |
| `PlugLoadUpgradeCost[$]` | $ | Plug-load retrofit cost. |
| `HeatingUpgradeCost[$]` | $ | Heating system upgrade cost. |
| `CoolingUpgradeCost[$]` | $ | Cooling system upgrade cost. |
| `HotWaterUpgradeCost[$]` | $ | Hot water system upgrade cost. |
| `GasEquipmentUpgradeCost[$]` | $ | Gas equipment upgrade cost. |
| `PVUpgradeCost[$]` | $ | PV installation cost. |
| `TotalUpgradeCost[$]` | $ | Sum of all upgrade costs. |

### Equipment Lifetimes

| Output Key | Unit |
|---|---|
| `EnvelopeLifeTime[Yr]` | years |
| `PlugLoadLifeTime[Yr]` | years |
| `HeatingLifeTime[Yr]` | years |
| `CoolingLifeTime[Yr]` | years |
| `HotWaterLifeTime[Yr]` | years |
| `PVLifeTime[Yr]` | years |

### Valuation

| Output Key | Unit | Description |
|---|---|---|
| `TaxAmount[$]` | $ | Annual property tax. |
| `TotalAssessedValue[$]` | $ | Total assessed value. |
| `ImprovementValue[$]` | $ | Assessed improvement value. |
| `LandValue[$]` | $ | Assessed land value. |
| `ImprovementLandRatio` | — | Improvement / land value ratio. |

### Demographics

| Output Key | Description |
|---|---|
| `IsLowIncome` | Flag: household is low-income. |
| `IsMiddleIncome` | Flag: household is middle-income. |
| `IsHighIncome` | Flag: household is high-income. |
| `peopleCount[P]` | Total building occupants. |

### Resilience

| Output Key | Unit | Description |
|---|---|---|
| `ThermalComfort` | — | Thermal comfort score. |
| `BuildingResilience[Days]` | days | Passive survivability duration. |
| `AdditionalElecOnGrid[kWh][Yr]` | kWh | Net electricity exported to grid. |
| `GridResilience` | — | Grid-level resilience indicator. |

### Retrofit Effectiveness

| Output Key | Unit | Description |
|---|---|---|
| `CO2Reduced[%]` | % | CO₂ reduction from retrofit. |
| `TotalEnergySavedPerc[%]` | % | Total energy reduction from retrofit. |

### Measures Applied

| Output Key | Description |
|---|---|
| `EnvelopeMeasureApplied` | Envelope measure label (or empty). |
| `PlugLoadMeasureApplied` | Plug-load measure label. |
| `HeatingMeasureApplied` | Heating measure label. |
| `CoolingMeasureApplied` | Cooling measure label. |
| `HotWaterMeasureApplied` | Hot-water measure label. |
| `PVMeasureApplied` | PV measure label. |
| `GasEquipmentMeasureApplied` | Gas equipment measure label. |

---

## Validation Rules (Feature to Building)

| Rule | Outcome |
|---|---|
| `ID_ESL` missing | Feature skipped (error). |
| `Area_SQM_ESL` < 4 m² or `Perimeter_M_ESL` < 7 m | Feature skipped (error). |
| `BldgHeight_M_ESL` missing | Feature skipped (error). |
| `BldgHeight_M_ESL` < 2.4 m | Height reset to 2.8 m (warning). |
| Estimated floor height outside 2.4–6.0 m | Warning logged; floors kept as-is. |
| No valid template and no complete archetype hashes | Previously: Feature skipped (error). Now we implement a separate archetype assignment approach, so these fields are absent by desing. |
| Duplicate `ID_ESL` values | Later duplicates dropped (warning). |
