# Dataset Descriptions

This document provides descriptions of all datasets used and generated in the parsing scripts.

## Input Datasets

### Clinical Trials Data
- **File**: `ctg-studies.json`
- **Location**: `/home/jh537/Clinical_Trial_Embending/Clinical_Trial_data/Retrievial/v2_/ctg-studies (5).json`
- **Description**: Raw clinical trial data from ClinicalTrials.gov containing trial information including:
  - Official and brief titles
  - Trial summaries
  - Detailed descriptions
  - Keywords
  - NCT IDs
  - Conditions and interventions

### PubMed Data
- **File**: `NEW_PM_id_text.json`
- **Location**: `/home/jh537/Clinical_Trial_Embending/Clinical_Trial_data/Retrievial/v2_/NEW_PM_id_text.json`
- **Description**: PubMed abstracts from the benchmark dataset containing:
  - Article IDs
  - Abstract text
  - Publication metadata

### Trial-Publication Mappings
- **File**: `paired_CT_PM.csv`
- **Location**: `/home/jh537/Clinical_Trial_Embending/Clinical_Trial_data/Retrievial/v2_/paired_CT_PM.csv`
- **Description**: Ground truth mappings between clinical trials and their published results (from the benchmark dataset):
  - NCT IDs
  - Corresponding PubMed IDs
  - Mapping confidence scores

## Processed Datasets

### Clinical Trial Summaries
- **File**: `LONG_CTG_id_text.json`
- **Description**: Processed clinical trial data containing:
  - Combined trial summaries (title + brief summary + detailed description)
  - NCT IDs
  - Keywords as additional context

### Clinical Trial References
- **File**: `LONG_CTG_id_text_refs.json`
- **Description**: Enhanced clinical trial data including:
  - All fields from LONG_CTG_id_text.json
  - Mapped PubMed reference IDs
  - Used for training and evaluation

### Training/Testing Splits
1. **Training Data**
   - **File**: `LONG_CTG_id_text_refs_train.json`
   - **Location**: `/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/`
   - **Description**: 80% of the data used for model training

2. **Testing Data**
   - **File**: `LONG_CTG_id_text_refs_test.json`
   - **Location**: `/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/`
   - **Description**: 20% of the data used for model evaluation

### PubMed Processing Files
- **File**: `NEW_PM_id_list.json`
- **Description**: List of all PubMed article IDs in the dataset

- **File**: `NEW_PM_id_url.json`
- **Description**: Mapping between PubMed IDs and their corresponding URLs

### Reranking Training Data
- **File**: `rerank_training_HN_10_17.jsonl`
- **Location**: `/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/`
- **Description**: Training data for the reranker model:
  - Queries: Clinical trial summaries
  - Positive examples: Correct PubMed abstracts
  - Hard negatives: Similar but incorrect abstracts (ranks 10-17)

## Data Flow
1. Raw clinical trials and PubMed data are processed into structured JSON formats
2. Trial-publication mappings are added to create reference datasets
3. Data is split into training and testing sets
4. Training data is enhanced with hard negatives for reranker training
5. Final datasets are used for model training and evaluation 