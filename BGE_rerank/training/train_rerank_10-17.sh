#!/bin/bash
#SBATCH -c 8
#SBATCH -t 1-00:00
#SBATCH -p gpu_quad
#SBATCH -o log_file/train_bge_rerank_%j.out
#SBATCH -e log_file/train_bge_rerank_%j.err
#SBATCH --gres=gpu:2



module load gcc/9.2.0

module load cuda/12.4

module load miniconda3


# === CHANGE THESE ===

source activate /home/jh537/.conda/envs/test_env



python git_bge_rerank_train_10-17.py 


# Example : sbatch slurm_mil_moe.sh leukemia_FLT3_mil_NTU2