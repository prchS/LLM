import os
import subprocess

# Set temp directory to E:
os.makedirs(r"E:\temp", exist_ok=True)
os.environ["TEMP"] = r"E:\temp"
os.environ["TMP"] = r"E:\temp"

# Upgrade pip
subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)

# Install PyTorch with CUDA
subprocess.run([
    "pip", "install",
    "torch", "torchvision", "torchaudio",
    "--index-url", "https://download.pytorch.org/whl/cu126"
], check=True)

#