# blender-pyscripts
Blender Python integrations

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
