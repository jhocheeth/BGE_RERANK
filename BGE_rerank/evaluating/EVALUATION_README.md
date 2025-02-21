# Evaluation Scripts for Clinical Trial-PubMed Linking Pipeline

This folder contains notebooks for evaluating the complete retrieval and reranking pipeline that links clinical trials to their corresponding PubMed publications.

## Scripts Overview

### `CLS_complete_pp.ipynb`

This notebook implements and evaluates a two-stage retrieval pipeline:

1. **First Stage: BGE Embedding and FAISS Retrieval**
   - Uses `BAAI/bge-large-en-v1.5` for embedding generation
   - Implements CLS token pooling strategy
   - Utilizes FAISS for efficient similarity search
   - Stores embeddings in HDF5 format for quick access

2. **Second Stage: BGE Reranker**
   - Uses fine-tuned BGE reranker model
   - Reranks the top-k candidates from the first stage
   - Produces final rankings with confidence scores

## Performance Metrics

The evaluation measures:
- Top-10 accuracy (percentage of correct articles in top 10)
- Top-1 accuracy (percentage of correct articles ranked first)
- Processing time per query and total runtime

## Implementation Details


### Embedding Generation
- Model: `BAAI/bge-large-en-v1.5`
- FP16 precision for efficiency
- GPU acceleration
- CLS token pooling strategy
- Embeddings stored in HDF5 format

### Retrieval Pipeline
- Initial retrieval: Top 30 candidates using FAISS
- L2 normalization for cosine similarity
- Reranking: Reduces to top 10 candidates
- Final ranking: Produces single best match

## Usage

The notebook is designed to run on GPU hardware and requires:
- CUDA-capable GPU
- PyTorch with CUDA support
- Transformers library
- FAISS-GPU
- H5py for embedding storage

