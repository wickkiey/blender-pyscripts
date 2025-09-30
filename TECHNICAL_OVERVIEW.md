# Image Camera Roll Animation - Technical Overview

## Scene Setup

```
┌─────────────────────────────────────────────────────────────┐
│                      3D SPACE LAYOUT                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Sun Light (5, -5, 10)          Fill Light (-5, -5, 5)      │
│      ☀                               💡                      │
│                                                               │
│                                                               │
│  Frame 1: Camera at TOP of image                             │
│      📷 ←────── CAMERA_DISTANCE ──────→ ┌─────────────┐     │
│  (0, -10, +5)                            │             │     │
│                                          │    IMAGE    │     │
│                                          │    PLANE    │     │
│                                          │   (0,0,0)   │     │
│           ↓ Camera animates ↓            │             │     │
│           ↓    downward     ↓            └─────────────┘     │
│           ↓                 ↓                                 │
│                                                               │
│  Frame 250: Camera at BOTTOM of image                        │
│  (0, -10, -5)                                                │
│      📷                                                       │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Animation Timeline

```
Frame:    1                                                250
          ├────────────────────────────────────────────────┤
Camera Z: +5.0 (top)                                    -5.0 (bottom)
          
          Smooth Bezier interpolation for cinematic feel
          ↓
          [Ease In] ──→ [Linear motion] ──→ [Ease Out]
```

## Camera Settings

- **Distance from Image**: 10.0 units (Y-axis: -10)
- **Field of View**: 50 degrees
- **Depth of Field**: Enabled (f/2.8 for shallow focus)
- **Focus Distance**: 10.0 units (locked on image plane)
- **Interpolation**: Bezier curve (auto handles for smooth easing)

## Image Plane Properties

- **Position**: Origin (0, 0, 0)
- **Orientation**: Facing camera (along Y-axis)
- **Scaling**: Automatic based on image aspect ratio
  - Base height: 10 units
  - Width: height × (image_width / image_height)
- **Material**: Principled BSDF with image texture

## Lighting Setup

1. **Sun Light**
   - Position: (5, -5, 10)
   - Energy: 1.0
   - Type: Directional (sun)
   - Purpose: Main illumination

2. **Fill Light**
   - Position: (-5, -5, 5)
   - Energy: 0.5
   - Type: Area light (5.0 size)
   - Purpose: Soften shadows, add dimension

## Render Configuration

- **Resolution**: 1920×1080 (Full HD)
- **Frame Rate**: 30 fps
- **Render Engine**: EEVEE (fast preview) / Can switch to Cycles
- **Motion Blur**: Enabled for realistic movement
- **Total Duration**: 8.3 seconds (250 frames ÷ 30 fps)

## Workflow

1. **Initialize**: Clear default scene objects
2. **Load Image**: Import image file and get dimensions
3. **Create Plane**: Generate mesh with correct aspect ratio
4. **Setup Material**: Create shader nodes with image texture
5. **Position Camera**: Place at top of image, facing center
6. **Keyframe Start**: Set camera position at frame 1
7. **Keyframe End**: Set camera position at frame 250
8. **Apply Smoothing**: Set Bezier interpolation for smooth motion
9. **Add Lighting**: Create sun and fill lights
10. **Configure Render**: Set resolution, fps, and quality settings

## Cinematic Effects

- **Depth of Field**: Creates focus fall-off (bokeh effect)
- **Motion Blur**: Adds realism to movement
- **Smooth Interpolation**: Natural acceleration/deceleration
- **Proper Lighting**: Three-point lighting approach (implied)

## Customization Points

All configurable via constants at the top of the script:
- IMAGE_PATH: Your source image
- ANIMATION_FRAMES: Duration control
- CAMERA_DISTANCE: Affects field of view coverage
- CAMERA_FOV: Wide vs telephoto look
- ENABLE_DOF: Toggle depth of field effect
