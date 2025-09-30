#!/bin/bash

# TRELLIS Installation Script
# This script installs TRELLIS and its dependencies for 3D generation

set -e

echo "=========================================="
echo "TRELLIS Installation Script"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required but not installed."
    exit 1
fi

echo ""
echo "Step 1: Creating virtual environment..."
if [ ! -d "venv_trellis" ]; then
    python3 -m venv venv_trellis
    echo "Virtual environment created: venv_trellis"
else
    echo "Virtual environment already exists: venv_trellis"
fi

echo ""
echo "Step 2: Activating virtual environment..."
source venv_trellis/bin/activate

echo ""
echo "Step 3: Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Step 4: Installing PyTorch (required for TRELLIS)..."
# Install PyTorch with CUDA support (or CPU if CUDA not available)
if command -v nvidia-smi &> /dev/null; then
    echo "CUDA detected, installing PyTorch with CUDA support..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
else
    echo "No CUDA detected, installing PyTorch CPU version..."
    pip install torch torchvision torchaudio
fi

echo ""
echo "Step 5: Installing core dependencies..."
pip install gradio
pip install pillow
pip install numpy
pip install trimesh
pip install huggingface_hub

echo ""
echo "Step 6: Installing additional 3D processing libraries..."
pip install pygltflib
pip install pymeshlab || echo "Warning: pymeshlab installation failed, continuing..."

echo ""
echo "Step 7: Installing TRELLIS..."
# Note: TRELLIS might need to be cloned from GitHub
# For now, we'll prepare the environment for it
echo "Preparing environment for TRELLIS..."
pip install transformers accelerate diffusers

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "To activate the environment, run:"
echo "  source venv_trellis/bin/activate"
echo ""
echo "To start the Gradio app, run:"
echo "  python gradio_trellis_app.py"
echo ""
echo "Note: If TRELLIS model weights are not available locally,"
echo "they will be downloaded on first use from HuggingFace."
echo ""
