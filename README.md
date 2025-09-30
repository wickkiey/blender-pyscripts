# blender-pyscripts
Blender Python integrations for creative workflows

## Overview

This repository contains Python scripts for Blender that enable various creative workflows:
- **Image Animation**: Create cinematic camera animations from static images
- **3D Generation**: Generate 3D models from text/images using AI (TRELLIS integration)
- **Model Viewing**: Automated 3D model viewing with turntable animations

## Scripts

### image_camera_roll.py
A Blender Python script that creates a cinematic camera animation rolling from top to bottom of an image placed in 3D space.

**Features:**
- Automatically inserts an image into Blender's 3D space as a plane
- Creates a camera with cinematic settings
- Animates the camera to smoothly roll from top to bottom of the image
- Optional depth of field (DOF) for enhanced focus effect
- Configurable animation duration and camera settings

**Usage:**
1. Open Blender
2. Go to Scripting workspace (top menu bar)
3. Click "Open" and select `image_camera_roll.py`
4. Edit the `IMAGE_PATH` variable at the top of the script to point to your image file
5. Optional: Adjust other configuration variables (animation frames, camera distance, etc.)
6. Click "Run Script" button or press `Alt+P`
7. Press `Spacebar` to preview the animation
8. Press `Ctrl+F12` to render the animation

**Configuration Options:**
- `IMAGE_PATH`: Path to your image file (required)
- `ANIMATION_FRAMES`: Total number of frames for the animation (default: 250)
- `CAMERA_DISTANCE`: Distance of camera from the image plane (default: 10.0)
- `CAMERA_FOV`: Camera field of view in degrees (default: 50.0)
- `ENABLE_DOF`: Enable depth of field for cinematic focus effect (default: True)

**Requirements:**
- Blender 2.8 or later (tested with Blender 3.x+)

---

### model_viewer_blender.py
A Blender Python script that loads 3D models (GLB/OBJ) and creates professional turntable animations with lighting.

**Features:**
- Imports GLB/GLTF and OBJ format models
- Automatically centers and scales models
- Creates 360° turntable animation
- Multiple lighting presets (studio, outdoor, dramatic)
- Optional depth of field for cinematic look
- Configurable camera positioning and animation

**Usage:**
1. Open Blender
2. Go to Scripting workspace
3. Click "Open" and select `model_viewer_blender.py`
4. Edit the `MODEL_PATH` variable to point to your 3D model file
5. Optional: Adjust configuration (lighting style, camera distance, etc.)
6. Run the script (Alt+P)
7. Preview with Spacebar or render with Ctrl+F12

**Configuration Options:**
- `MODEL_PATH`: Path to your 3D model file (required)
- `ANIMATION_FRAMES`: Frames for full rotation (default: 250)
- `CAMERA_DISTANCE`: Distance from model (default: 10.0)
- `CAMERA_HEIGHT`: Camera height above model (default: 5.0)
- `LIGHTING_STYLE`: "studio", "outdoor", or "dramatic" (default: "studio")
- `ROTATE_MODEL`: Rotate model vs. camera (default: False)
- `ENABLE_DOF`: Enable depth of field (default: True)

**Requirements:**
- Blender 2.8 or later

---

### TRELLIS 3D Generation Integration

**NEW**: AI-powered text-to-3D and image-to-3D generation using Microsoft's TRELLIS model!

#### gradio_trellis_app.py
A Gradio web application for generating 3D models from text prompts or images.

**Features:**
- Text-to-3D: Generate models from text descriptions
- Image-to-3D: Convert 2D images to 3D models
- Web-based interface (no Blender required for generation)
- Export to GLB/OBJ formats compatible with Blender
- Configurable generation parameters

**Quick Start:**
```bash
# Install dependencies
./install_trellis.sh

# Start the Gradio app
source venv_trellis/bin/activate
python gradio_trellis_app.py
```

Then open http://localhost:7860 in your browser!

**For Complete Setup Instructions**: See [TRELLIS_SETUP.md](TRELLIS_SETUP.md)

**Requirements:**
- Python 3.8+
- 8GB+ RAM (16GB recommended)
- GPU with CUDA (optional, for faster generation)

#### Complete Workflow Example:
1. Generate a 3D model using `gradio_trellis_app.py`
2. Download the generated GLB/OBJ file
3. Use `model_viewer_blender.py` to view it in Blender with automatic setup

---

## Installation & Setup

### For Image Animation (image_camera_roll.py)
No additional installation required - just Blender!

### For 3D Generation (TRELLIS)
See [TRELLIS_SETUP.md](TRELLIS_SETUP.md) for complete installation instructions.

Quick install:
```bash
chmod +x install_trellis.sh
./install_trellis.sh
```

### For Model Viewing (model_viewer_blender.py)
No additional installation required - just Blender!

## Documentation

- [QUICKSTART.md](QUICKSTART.md) - Quick start guide for image_camera_roll.py
- [TRELLIS_SETUP.md](TRELLIS_SETUP.md) - Complete TRELLIS setup and usage guide
- [TECHNICAL_OVERVIEW.md](TECHNICAL_OVERVIEW.md) - Technical details

## Examples

### Example 1: Animate an Image
```python
# In image_camera_roll.py
IMAGE_PATH = "/path/to/photo.jpg"
# Run in Blender → Creates cinematic vertical scroll
```

### Example 2: Generate 3D from Text
```bash
# Start Gradio app
python gradio_trellis_app.py
# In browser: Enter "a red dragon" → Download model.glb
```

### Example 3: View Generated Model
```python
# In model_viewer_blender.py
MODEL_PATH = "/path/to/model.glb"
# Run in Blender → Creates turntable animation
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

See individual script headers for license information.
