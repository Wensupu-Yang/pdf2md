import torch

# Check if PyTorch is installed and print the version
print(f"PyTorch version: {torch.__version__}")

# Check if CUDA is available (for GPU support)
print(f"CUDA available: {torch.cuda.is_available()}")

