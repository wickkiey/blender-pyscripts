# Quick Start Guide

## 🎬 Image Camera Roll Animation - Quick Start

### What This Script Does
Creates a cinematic camera animation that smoothly rolls from the top to the bottom of an image placed in Blender's 3D space, with professional depth-of-field effects.

### Prerequisites
- Blender 2.8 or later (Blender 3.x recommended)
- An image file (JPG, PNG, etc.)

### 5-Minute Setup

#### Step 1: Prepare Your Image
- Choose any image you want to animate
- Note the file path (e.g., `/home/user/Pictures/photo.jpg`)

#### Step 2: Open Blender
```
1. Launch Blender
2. Click on "Scripting" workspace at the top
```

#### Step 3: Load the Script
```
1. In the Text Editor panel, click "Open"
2. Navigate to and select "image_camera_roll.py"
```

#### Step 4: Configure
```python
# Find this line near the top of the script:
IMAGE_PATH = "/path/to/your/image.jpg"

# Replace with your actual image path:
IMAGE_PATH = "/home/user/Pictures/photo.jpg"
```

#### Step 5: Run
```
1. Click "Run Script" button (or press Alt+P)
2. Wait for "Setup Complete!" message
```

#### Step 6: Preview & Render
```
Preview:  Press Spacebar to play animation
Render:   Press Ctrl+F12 to render full animation
```

### Customization Quick Reference

#### Change Animation Speed
```python
ANIMATION_FRAMES = 250  # Default (8.3 seconds at 30fps)
ANIMATION_FRAMES = 150  # Faster (5 seconds)
ANIMATION_FRAMES = 450  # Slower (15 seconds)
```

#### Adjust Camera Distance
```python
CAMERA_DISTANCE = 10.0  # Default
CAMERA_DISTANCE = 15.0  # Further away (shows more of image)
CAMERA_DISTANCE = 7.0   # Closer (more zoomed in)
```

#### Change Camera Field of View
```python
CAMERA_FOV = 50.0  # Default (natural look)
CAMERA_FOV = 35.0  # Telephoto (compressed, narrow)
CAMERA_FOV = 70.0  # Wide angle (expansive)
```

#### Toggle Depth of Field
```python
ENABLE_DOF = True   # Cinematic blur effect (default)
ENABLE_DOF = False  # Everything in focus
```

### Troubleshooting

#### "Image not found" error
- Check that IMAGE_PATH is correct
- Use forward slashes (/) even on Windows
- Or use raw string: `r"C:\Users\Name\Pictures\image.jpg"`

#### Script runs but nothing appears
- Make sure you updated IMAGE_PATH
- Check the Blender console for error messages
- Verify the image file exists and is readable

#### Animation is too fast/slow
- Adjust ANIMATION_FRAMES
- Remember: frames ÷ 30 = seconds (at 30fps)

#### Camera doesn't move
- Check the timeline at the bottom
- Drag the green playhead to see camera position change
- Ensure animation was set up (check for "Setup Complete!" message)

### Tips for Best Results

✨ **Image Selection**
- Vertical/portrait images work great
- High resolution images (1920px+ height) recommended
- Images with interesting details from top to bottom

🎨 **Artistic Control**
- For dramatic effect: Use ENABLE_DOF = True
- For documentary style: Use ENABLE_DOF = False
- For epic reveal: Increase ANIMATION_FRAMES to 400+

📹 **Rendering**
- Preview with EEVEE (faster, default)
- Switch to Cycles in script for photorealistic quality
- Render single frame first to test (F12)

### Output

After rendering (Ctrl+F12):
- Video saved in Blender's output directory
- Default: `/tmp/` on Linux, `C:\tmp\` on Windows
- Change in: Render Properties → Output → Output Path

### Next Steps

1. **Experiment** with different configuration values
2. **Try** different images (landscapes, portraits, art)
3. **Adjust** lighting in the script if needed
4. **Export** your animation and share!

---

### Need Help?

- Check `TECHNICAL_OVERVIEW.md` for detailed information
- Review Blender documentation: https://docs.blender.org/
- Modify the `add_lighting()` function for custom lighting
- Edit `setup_render_settings()` for different output formats

Enjoy creating cinematic image animations! 🎥
