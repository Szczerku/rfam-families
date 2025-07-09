# rfam-families

This repository contains curated lists of RNA families from the Rfam database, selected for downstream modeling and analysis.

## Overview

The goal is to create a **whitelist of Rfam families** that meet the following criteria:  
- **At least 128 sequences per family** (to ensure a minimum of two batches per epoch with a batch size of 64).
- **Maximum sequence length of 300 nucleotides**.

## Files

- **`rfam-families.xlsx`** — contains **all** families from Rfam.
- **`rfam-whitelist.xlsx`** — contains only the families that satisfy the filtering criteria.

## Usage

All sequences for each family can be **downloaded and unzipped** using the provided script in this repository.