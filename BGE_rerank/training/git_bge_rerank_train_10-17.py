import subprocess

def run_finetuning():
    command = [
        "torchrun",
        "--nproc_per_node", "2",
        "-m", "FlagEmbedding.finetune.reranker.encoder_only.base",
        "--model_name_or_path", "BAAI/bge-reranker-v2-m3",
        "--train_data", "/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/rerank_training_HN_10_17.jsonl",
        "--train_group_size", "8",
        "--query_max_len", "512",
        "--passage_max_len", "512",
        "--knowledge_distillation", "False",
        "--output_dir", "/n/data1/hsph/biostat/celehs/lab/jh537/Retrivial_task/DATA/NEW_reranker_HN_10_17_8epochs",
        "--overwrite_output_dir",
        "--learning_rate", "4e-5",
        "--fp16",
        "--num_train_epochs", "8",
        "--per_device_train_batch_size", "1",
        "--gradient_accumulation_steps", "1",
        "--dataloader_drop_last", "True",
        "--warmup_ratio", "0.1",
        "--weight_decay", "0.01",
        "--logging_steps", "10000000",
        "--save_steps", "10000000000"
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_finetuning()

