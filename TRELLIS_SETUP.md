# TRELLIS 3D Generation Setup Guide

## Overview

TRELLIS is a state-of-the-art text-to-3D and image-to-3D generation model that creates high-quality 3D assets. This integration allows you to generate 3D models and import them directly into Blender.

Reference: [Microsoft TRELLIS](https://github.com/microsoft/TRELLIS)

## Features

- **Text-to-3D**: Generate 3D models from text descriptions
- **Image-to-3D**: Convert 2D images into 3D models
- **Gradio Interface**: User-friendly web interface for generation
- **Blender Integration**: Export formats compatible with Blender (GLB, OBJ)
- **Viewer Script**: Blender script to automatically load and setup generated models

## Prerequisites

- Python 3.8 or higher
- 8GB+ RAM (16GB recommended for better performance)
- GPU with CUDA support (optional, but recommended for faster generation)
- Blender 2.8 or later (for viewing generated models)

## Installation

### Quick Install (Linux/macOS)

```bash
# Make the installation script executable
chmod +x install_trellis.sh

# Run the installation script
./install_trellis.sh
```

### Manual Installation

If you prefer manual installation or are on Windows:

```bash
# 1. Create virtual environment
python3 -m venv venv_trellis

# 2. Activate virtual environment
# On Linux/macOS:
source venv_trellis/bin/activate
# On Windows:
venv_trellis\Scripts\activate

# 3. Install PyTorch (choose based on your system)
# For CUDA 11.8:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# For CPU only:
pip install torch torchvision torchaudio

# 4. Install dependencies
pip install gradio pillow numpy trimesh pygltflib
pip install transformers accelerate diffusers huggingface_hub
```

## Usage

### Starting the Gradio Application

```bash
# Activate the virtual environment
source venv_trellis/bin/activate  # Linux/macOS
# or
venv_trellis\Scripts\activate  # Windows

# Start the Gradio app
python gradio_trellis_app.py
```

The application will start and provide a URL (typically http://localhost:7860) that you can open in your web browser.

### Using the Gradio Interface

1. **Text-to-3D Mode**:
   - Enter a text description (e.g., "a red dragon", "modern chair", "futuristic spaceship")
   - Click "Generate 3D Model"
   - Wait for generation to complete
   - Download the model in GLB or OBJ format

2. **Image-to-3D Mode**:
   - Upload an image
   - Click "Generate 3D Model from Image"
   - Wait for generation to complete
   - Download the model

### Loading Models in Blender

#### Option 1: Manual Import

1. Open Blender
2. Go to `File > Import > glTF 2.0 (.glb/.gltf)` or `File > Import > Wavefront (.obj)`
3. Select your generated model file
4. The model will be imported into your scene

#### Option 2: Automatic Setup (Using model_viewer_blender.py)

1. Open Blender
2. Go to the Scripting workspace
3. Open `model_viewer_blender.py`
4. Update the `MODEL_PATH` variable to point to your generated model
5. Run the script (Alt+P)

The script will:
- Clear the scene
- Import the model
- Set up proper lighting
- Configure the camera for optimal viewing
- Add a turntable animation

## Output Formats

### GLB (GL Transmission Format Binary)
- **Recommended for Blender**
- Single file format
- Includes textures and materials
- Widely supported

### OBJ (Wavefront)
- Universal 3D format
- Separate material files (.mtl)
- Good for editing and modification

## Tips for Best Results

### Text Prompts
- Be specific and descriptive
- Include material/texture details (e.g., "metallic", "wooden", "glossy")
- Mention style if important (e.g., "low-poly", "realistic", "stylized")
- Keep prompts clear and concise

### Image Inputs
- Use clear, well-lit images
- Avoid cluttered backgrounds
- Higher resolution images may yield better results
- Single objects work better than complex scenes

### Performance Optimization
- GPU acceleration significantly speeds up generation (5-10x faster)
- Generation typically takes 30 seconds to 5 minutes depending on complexity
- Consider reducing quality settings for faster preview generation

## Configuration

You can customize the generation parameters in `gradio_trellis_app.py`:

```python
# Generation settings
NUM_INFERENCE_STEPS = 50  # Higher = better quality, slower
GUIDANCE_SCALE = 7.5      # Controls prompt adherence (7-15 recommended)
OUTPUT_FORMAT = "glb"     # "glb" or "obj"
```

## Troubleshooting

### Issue: "CUDA out of memory"
**Solution**: 
- Reduce batch size or resolution in the configuration
- Close other GPU-intensive applications
- Use CPU mode (slower but doesn't require GPU)

### Issue: "Model weights not found"
**Solution**:
- Ensure you have internet connection for first run
- Model weights will be downloaded from HuggingFace (may take time)
- Check `~/.cache/huggingface/` directory

### Issue: "Import error in Blender"
**Solution**:
- Verify the file format (GLB recommended)
- Check file size (very large files may need time to load)
- Try OBJ format if GLB has issues

### Issue: "Gradio app won't start"
**Solution**:
- Verify virtual environment is activated
- Check port 7860 is not in use
- Try specifying a different port: `python gradio_trellis_app.py --port 7861`

## File Structure

```
blender-pyscripts/
├── install_trellis.sh           # Installation script
├── gradio_trellis_app.py        # Gradio web application
├── model_viewer_blender.py      # Blender viewer script
├── TRELLIS_SETUP.md            # This file
├── outputs/                     # Generated models (created automatically)
│   └── *.glb, *.obj
└── venv_trellis/               # Virtual environment (created by install script)
```

## Examples

### Example 1: Generate a Simple Object
```
Text prompt: "a blue ceramic coffee mug"
Settings: Default
Output: coffee_mug.glb
```

### Example 2: Complex Scene
```
Text prompt: "a medieval castle with towers and walls, stone texture"
Settings: NUM_INFERENCE_STEPS = 75, GUIDANCE_SCALE = 9.0
Output: castle.glb
```

### Example 3: From Image
```
Input: photo of a sneaker
Settings: Default
Output: sneaker_3d.glb
```

## Advanced Usage

### Batch Generation
Modify `gradio_trellis_app.py` to process multiple prompts:

```python
prompts = ["object1", "object2", "object3"]
for i, prompt in enumerate(prompts):
    model = generate_3d(prompt)
    save_model(model, f"output_{i}.glb")
```

### Custom Post-Processing
Use the generated models with Python:

```python
import trimesh

# Load generated model
mesh = trimesh.load("output.glb")

# Apply transformations
mesh.apply_scale(2.0)
mesh.export("scaled_output.glb")
```

## Resources

- [TRELLIS GitHub Repository](https://github.com/microsoft/TRELLIS)
- [Gradio Documentation](https://gradio.app/docs/)
- [Blender Python API](https://docs.blender.org/api/current/)
- [GLB Format Specification](https://www.khronos.org/gltf/)

## Support

For issues specific to:
- **TRELLIS model**: Check the official TRELLIS repository
- **Blender integration**: See `model_viewer_blender.py` comments
- **Gradio interface**: See `gradio_trellis_app.py` documentation

## License

This integration follows the licenses of the respective components:
- TRELLIS: Check [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS) for license
- This integration code: Same as the blender-pyscripts repository

---

**Happy 3D Generation!** 🎨🖼️➡️🎭
