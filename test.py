from datasets import load_dataset

# If the dataset is gated/private, make sure you have run huggingface-cli login
dataset = load_dataset("uc-merced-pyedtools/test")

print(dataset)