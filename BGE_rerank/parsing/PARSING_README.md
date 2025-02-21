# Parsing Scripts for Clinical Trials and PubMed Data

This folder contains scripts for parsing and preparing training/testing data from clinical trials and PubMed abstracts.

## Data Sources

### Clinical Trials Data
The clinical trials data is parsed directly from [ClinicalTrials.gov](https://clinicaltrials.gov/). The parsing scripts extract:
- Trial titles
- Brief summaries
- Detailed descriptions
- Keywords
- Trial identifiers (NCT IDs)

### PubMed Abstracts
The PubMed abstracts are parsed from the benchmark dataset provided in the paper:
> "Identifying unreported links between ClinicalTrials.gov trial registrations and their published results"  
> by Shifeng Liu, Florence T. Bourgeois, and Adam G. Dunn

## Scripts Overview

1. `Parse_clinicaltrial_for_retrieval.ipynb`
   - Processes clinical trial data from ClinicalTrials.gov
   - Creates structured JSON files with trial information
   - Splits data into training and testing sets

2. `Parse_NEW_PUBMED.ipynb`
   - Extracts PubMed abstract text from the benchmark dataset
   - Creates mappings between PubMed IDs and their URLs
   - Generates lists of article IDs for processing

3. `Mine_Hard_Neg_for_Reranking.ipynb`
   - Processes the parsed data for reranking training
   - Handles reference mappings between clinical trials and PubMed articles

## Data Structure
The scripts generate several JSON files containing:
- Clinical trial summaries with their NCT IDs
- PubMed article texts with their article IDs
- Mappings between clinical trials and their corresponding published results
- Training and testing splits for model development

## Purpose
These parsing scripts prepare the data for training and testing retrieval and reranking models that can identify links between clinical trials and their published results in the medical literature. 