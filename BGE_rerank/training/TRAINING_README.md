# Training Scripts for BGE Reranker

This folder contains scripts for fine-tuning the BGE reranker model on clinical trials and PubMed data.

## Scripts Overview

### 1. `git_bge_rerank_train_10-17.py`
Python script that configures and runs the fine-tuning process for the BGE reranker model with the following specifications:

- Base model: `BAAI/bge-reranker-v2-m3`
- Training parameters:
  - Learning rate: 4e-5
  - Training epochs: 8
  - Batch size: 1 per device
  - Group size: 8
  - Maximum sequence length: 512 (for both query and passage)
  - FP16 precision
  - Warmup ratio: 0.1
  - Weight decay: 0.01

### 2. `train_rerank_10-17.sh`
SLURM batch script for running the training on a GPU cluster:

- Resource requirements:
  - 8 CPU cores
  - 2 GPUs (gpu_quad partition)
  - 24-hour runtime limit
- Environment setup:
  - Loads required modules (gcc 9.2.0, CUDA 12.4, miniconda3)
  - Activates the conda environment `test_env`

## Usage

To start the training process:

```bash
sbatch train_rerank_10-17.sh
```

The script will:
1. Load necessary modules
2. Activate the conda environment
3. Run the training script with distributed training on 2 GPUs

## Output

- Training logs are saved to:
  - Standard output: `log_file/train_bge_rerank_%j.out`
  - Error output: `log_file/train_bge_rerank_%j.err`
- Model checkpoints and training outputs are saved to:
  `/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/NEW_reranker_HN_10_17_8epochs`

## Training Data

The model is trained on the processed dataset at:
`/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/rerank_training_HN_10_17.jsonl`

This dataset contains pairs of clinical trials and PubMed abstracts for training the reranker model. 