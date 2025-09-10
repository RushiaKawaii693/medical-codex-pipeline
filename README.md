# medical-codex-pipeline

Assignment for HHA 507

## Overview

This project provides scripts and tools to process and standardize various medical codex datasets (LOINC, HCPCS, ICD-10, NPI, SNOMED, RxNorm, etc.) into a unified format for analysis and integration.

## Standardized Output Format

All processed codexes are output as tables with these columns:
- `code`: The primary identifier
- `description`: Human-readable description
- `last_updated`: Processing timestamp

## Usage

1. Place raw data files in the `input/` directory.
2. Run the relevant processor script from the `scripts/` directory, for example:
   ```sh
   python scripts/loinc_processor.py
   ```
3. Standardized outputs will be saved in the `output/` directory.

## Requirements

- Python 3.8+
- [pandas](https://pandas.pydata.org/) and/or [polars](https://pola.rs/)
- See `requirements.txt` for details

## Scripts

- `scripts/loinc_processor.py` – Process LOINC codes
- `scripts/hcpcs_processor.py` – Process HCPCS codes
- `scripts/icd10cm_processor.py` – Process ICD-10-CM codes
- `scripts/icd10who_processor.py` – Process ICD-10-WHO codes
- `scripts/npi_processor.py` – Process NPI data
- `scripts/snow_med.py` – Process SNOMED CT data
- `scripts/rxnorm_processor.py` – Process RxNorm data

## Notes

- Large raw data files are not tracked in this repository. See `.gitignore`.

