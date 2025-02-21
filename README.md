# Clinical Trial-PubMed Linking Pipeline

A comprehensive pipeline for automatically linking clinical trials from ClinicalTrials.gov with their corresponding published results in PubMed. The system uses state-of-the-art language models and a two-stage retrieval approach.

## Project Structure

```
.
├── parsing/                 # Data preparation scripts
├── training/               # Model training scripts
└── evaluating/            # Evaluation and testing scripts
```

## System Overview

This project implements a two-stage retrieval system:
1. **Initial Retrieval**: Using BGE embeddings and FAISS for efficient similarity search
2. **Reranking**: Using a fine-tuned BGE reranker to improve precision


## Components

### 1. Data Parsing and Preparation
- Processes clinical trials from ClinicalTrials.gov
- Extracts PubMed abstracts from benchmark dataset
- Creates training/testing splits
- [Details in parsing/PARSING_README.md](parsing/PARSING_README.md)

### 2. Model Training
- Fine-tunes BGE reranker on clinical trial-PubMed pairs
- Uses distributed training on GPU cluster
- Implements hard negative mining
- [Details in training/TRAINING_README.md](training/TRAINING_README.md)

### 3. Evaluation Pipeline
- Complete end-to-end evaluation system
- Embedding generation and storage
- Two-stage retrieval and reranking
- [Details in evaluating/EVALUATION_README.md](evaluating/EVALUATION_README.md)

## Requirements

### Hardware
- CUDA-capable GPU(s)
- Minimum 16GB GPU memory recommended
- Large storage for embeddings and models

### Software
- Python 3.12+
- PyTorch with CUDA support
- Transformers library
- FAISS-GPU
- H5py
- Required modules listed in `requirements.txt`

## Models Used

1. **First Stage Retrieval**
   - Model: `BAAI/bge-large-en-v1.5`
   - Purpose: Dense passage retrieval

2. **Reranking Stage**
   - Base Model: `BAAI/bge-reranker-v2-m3`
   - Fine-tuned on clinical trial-PubMed pairs

## Data Sources

- Clinical trials from [ClinicalTrials.gov](https://clinicaltrials.gov/)
- PubMed abstracts from benchmark dataset (Liu et al.)
- Reference mappings from published research

## Citation

If you use this pipeline, please cite:
```bibtex
@article{liu2023identifying,
  title={Identifying unreported links between ClinicalTrials.gov trial registrations and their published results},
  author={Liu, Shifeng and Bourgeois, Florence T and Dunn, Adam G},
  year={2023}
}
```



## Acknowledgments

- Based on the benchmark dataset from Liu et al.
- Uses models from BAAI (BGE series)
- Developed at Harvard School of Public Health 
