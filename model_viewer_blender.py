"""
Blender Python Script: 3D Model Viewer with Turntable Animation
This script loads a 3D model (GLB/OBJ) and creates a turntable animation
with proper lighting and camera setup - similar to image_camera_roll.py

Usage:
1. Open Blender
2. Open the Scripting workspace
3. Load this script in the text editor
4. Update the MODEL_PATH variable to point to your 3D model file
5. Run the script (Alt+P or click Run Script button)
"""

import bpy
import math
import os

# Configuration
MODEL_PATH = "/path/to/your/model.glb"  # Update this path to your 3D model
ANIMATION_FRAMES = 250  # Total frames for turntable animation (360 degree rotation)
CAMERA_DISTANCE = 10.0  # Distance of camera from model
CAMERA_HEIGHT = 5.0  # Height of camera above model center
CAMERA_FOV = 50.0  # Camera field of view in degrees
ENABLE_DOF = True  # Enable depth of field for cinematic focus
ROTATE_MODEL = False  # If True, rotates model; if False, rotates camera
LIGHTING_STYLE = "studio"  # "studio", "outdoor", or "dramatic"


def clear_scene():
    """Clear all objects from the scene"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def import_model(model_path):
    """
    Import a 3D model (GLB or OBJ format)
    Returns: imported object(s)
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    file_ext = os.path.splitext(model_path)[1].lower()
    
    # Import based on file type
    if file_ext in ['.glb', '.gltf']:
        # Import GLB/GLTF
        bpy.ops.import_scene.gltf(filepath=model_path)
    elif file_ext == '.obj':
        # Import OBJ
        bpy.ops.import_scene.obj(filepath=model_path)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}. Use .glb, .gltf, or .obj")
    
    # Get imported objects
    imported_objects = bpy.context.selected_objects
    
    if not imported_objects:
        raise RuntimeError("No objects were imported from the model file")
    
    # Create a parent empty for all imported objects
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
    parent_empty = bpy.context.active_object
    parent_empty.name = "ModelParent"
    
    # Parent all imported objects to the empty
    for obj in imported_objects:
        obj.parent = parent_empty
    
    # Center the model at origin
    center_model(parent_empty, imported_objects)
    
    return parent_empty, imported_objects


def center_model(parent_empty, objects):
    """Center the model at the world origin"""
    if not objects:
        return
    
    # Calculate bounding box of all objects
    min_coords = [float('inf'), float('inf'), float('inf')]
    max_coords = [float('-inf'), float('-inf'), float('-inf')]
    
    for obj in objects:
        if obj.type == 'MESH':
            for vertex in obj.data.vertices:
                world_coord = obj.matrix_world @ vertex.co
                for i in range(3):
                    min_coords[i] = min(min_coords[i], world_coord[i])
                    max_coords[i] = max(max_coords[i], world_coord[i])
    
    # Calculate center
    center = [(min_coords[i] + max_coords[i]) / 2 for i in range(3)]
    
    # Move parent empty to center the model
    parent_empty.location = (-center[0], -center[1], -center[2])
    
    # Calculate model size for camera positioning
    size = [(max_coords[i] - min_coords[i]) for i in range(3)]
    max_dimension = max(size)
    
    return center, max_dimension


def create_turntable_camera(model_parent, model_size=5.0):
    """
    Create camera with turntable animation
    """
    # Adjust camera distance based on model size
    distance = max(CAMERA_DISTANCE, model_size * 1.5)
    
    # Create camera
    bpy.ops.object.camera_add(location=(distance, 0, CAMERA_HEIGHT))
    camera = bpy.context.active_object
    camera.name = "TurntableCamera"
    
    # Set camera properties
    camera.data.lens_unit = 'FOV'
    camera.data.angle = math.radians(CAMERA_FOV)
    
    # Point camera at model center
    direction = model_parent.location - camera.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    
    # Enable depth of field
    if ENABLE_DOF:
        camera.data.dof.use_dof = True
        camera.data.dof.focus_distance = distance
        camera.data.dof.aperture_fstop = 2.8
    
    # Set as active camera
    bpy.context.scene.camera = camera
    
    # Set animation frame range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = ANIMATION_FRAMES
    
    if ROTATE_MODEL:
        # Rotate the model instead of camera
        create_model_rotation_animation(model_parent)
    else:
        # Rotate camera around model
        create_camera_rotation_animation(camera, model_parent, distance)
    
    return camera


def create_camera_rotation_animation(camera, model_parent, distance):
    """Animate camera rotating around the model"""
    
    # Create an empty to act as the rotation center
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=model_parent.location)
    rotation_center = bpy.context.active_object
    rotation_center.name = "CameraRotationCenter"
    
    # Parent camera to the rotation center
    camera.parent = rotation_center
    
    # Set keyframes for rotation
    bpy.context.scene.frame_set(1)
    rotation_center.rotation_euler = (0, 0, 0)
    rotation_center.keyframe_insert(data_path="rotation_euler", index=2)
    
    bpy.context.scene.frame_set(ANIMATION_FRAMES)
    rotation_center.rotation_euler = (0, 0, math.radians(360))
    rotation_center.keyframe_insert(data_path="rotation_euler", index=2)
    
    # Set interpolation to linear for smooth rotation
    if rotation_center.animation_data and rotation_center.animation_data.action:
        for fcurve in rotation_center.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'


def create_model_rotation_animation(model_parent):
    """Animate model rotating in place"""
    
    # Set keyframes for model rotation
    bpy.context.scene.frame_set(1)
    model_parent.rotation_euler = (0, 0, 0)
    model_parent.keyframe_insert(data_path="rotation_euler", index=2)
    
    bpy.context.scene.frame_set(ANIMATION_FRAMES)
    model_parent.rotation_euler = (0, 0, math.radians(360))
    model_parent.keyframe_insert(data_path="rotation_euler", index=2)
    
    # Set interpolation to linear
    if model_parent.animation_data and model_parent.animation_data.action:
        for fcurve in model_parent.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'


def add_studio_lighting():
    """Add studio-style three-point lighting"""
    
    # Key Light (main light)
    bpy.ops.object.light_add(type='AREA', location=(5, -5, 8))
    key_light = bpy.context.active_object
    key_light.name = "KeyLight"
    key_light.data.energy = 500
    key_light.data.size = 5.0
    key_light.rotation_euler = (math.radians(45), 0, math.radians(45))
    
    # Fill Light (softer, opposite side)
    bpy.ops.object.light_add(type='AREA', location=(-5, -3, 5))
    fill_light = bpy.context.active_object
    fill_light.name = "FillLight"
    fill_light.data.energy = 200
    fill_light.data.size = 5.0
    fill_light.rotation_euler = (math.radians(45), 0, math.radians(-45))
    
    # Rim/Back Light (separation from background)
    bpy.ops.object.light_add(type='SPOT', location=(0, 5, 6))
    rim_light = bpy.context.active_object
    rim_light.name = "RimLight"
    rim_light.data.energy = 300
    rim_light.rotation_euler = (math.radians(120), 0, 0)
    
    return key_light, fill_light, rim_light


def add_outdoor_lighting():
    """Add outdoor-style lighting with sun"""
    
    # Sun light (main illumination)
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
    sun = bpy.context.active_object
    sun.name = "SunLight"
    sun.data.energy = 3.0
    sun.rotation_euler = (math.radians(45), 0, math.radians(45))
    
    # Sky/ambient light
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 10))
    sky_light = bpy.context.active_object
    sky_light.name = "SkyLight"
    sky_light.data.energy = 100
    sky_light.data.size = 10.0
    sky_light.data.color = (0.6, 0.7, 1.0)  # Slightly blue for sky
    
    return sun, sky_light


def add_dramatic_lighting():
    """Add dramatic lighting with strong contrast"""
    
    # Strong key light from side
    bpy.ops.object.light_add(type='SPOT', location=(8, -3, 6))
    key_light = bpy.context.active_object
    key_light.name = "DramaticKey"
    key_light.data.energy = 800
    key_light.rotation_euler = (math.radians(60), 0, math.radians(30))
    
    # Weak fill from front
    bpy.ops.object.light_add(type='AREA', location=(0, -6, 3))
    fill_light = bpy.context.active_object
    fill_light.name = "DramaticFill"
    fill_light.data.energy = 50
    fill_light.data.size = 3.0
    
    return key_light, fill_light


def add_lighting():
    """Add lighting based on selected style"""
    if LIGHTING_STYLE == "studio":
        return add_studio_lighting()
    elif LIGHTING_STYLE == "outdoor":
        return add_outdoor_lighting()
    elif LIGHTING_STYLE == "dramatic":
        return add_dramatic_lighting()
    else:
        return add_studio_lighting()  # Default to studio


def setup_render_settings():
    """Configure render settings for quality output"""
    scene = bpy.context.scene
    
    # Set render resolution
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    
    # Set frame rate
    scene.render.fps = 30
    
    # Use Eevee for faster rendering (change to CYCLES for higher quality)
    scene.render.engine = 'BLENDER_EEVEE_NEXT'
    
    # Enable ambient occlusion for better depth
    if hasattr(scene.eevee, 'use_gtao'):
        scene.eevee.use_gtao = True
    
    # Enable bloom for nice highlights
    if hasattr(scene.eevee, 'use_bloom'):
        scene.eevee.use_bloom = True
    
    # Set background
    scene.render.film_transparent = False
    
    # World background color (neutral gray)
    if scene.world:
        scene.world.use_nodes = True
        bg_node = scene.world.node_tree.nodes.get('Background')
        if bg_node:
            bg_node.inputs[0].default_value = (0.05, 0.05, 0.05, 1.0)  # Dark gray


def main():
    """Main function to set up the scene"""
    print("Starting 3D Model Viewer with Turntable Animation setup...")
    
    # Check if model path is set
    if MODEL_PATH == "/path/to/your/model.glb":
        print("\n❌ WARNING: Please update MODEL_PATH variable with your actual model path!")
        print("The script cannot continue without a valid model path.")
        return
    
    # Clear the scene
    print("Clearing scene...")
    clear_scene()
    
    # Import the model
    print(f"Loading model from: {MODEL_PATH}")
    model_parent, imported_objects = import_model(MODEL_PATH)
    print(f"Model imported successfully: {len(imported_objects)} object(s)")
    
    # Get model size for camera positioning
    _, model_size = center_model(model_parent, imported_objects)
    print(f"Model size: {model_size:.2f} units")
    
    # Create turntable camera
    print("Creating turntable camera with animation...")
    camera = create_turntable_camera(model_parent, model_size)
    print(f"Camera animation set up: {ANIMATION_FRAMES} frames")
    
    # Add lighting
    print(f"Adding {LIGHTING_STYLE} lighting...")
    add_lighting()
    
    # Setup render settings
    print("Configuring render settings...")
    setup_render_settings()
    
    # Set initial frame
    bpy.context.scene.frame_set(1)
    
    print("\n=== Setup Complete! ===")
    print(f"Animation: {ANIMATION_FRAMES} frames (360° rotation)")
    print(f"Rotation: {'Model rotates' if ROTATE_MODEL else 'Camera rotates'}")
    print(f"Lighting: {LIGHTING_STYLE.capitalize()} style")
    print(f"Depth of Field: {'Enabled' if ENABLE_DOF else 'Disabled'}")
    print("\n📋 Controls:")
    print("  Spacebar - Preview animation")
    print("  Ctrl+F12 - Render animation")
    print("  F12 - Render single frame")
    print("\n💡 Tips:")
    print("  - Adjust CAMERA_DISTANCE and CAMERA_HEIGHT for better framing")
    print("  - Try different LIGHTING_STYLE: 'studio', 'outdoor', or 'dramatic'")
    print("  - Toggle ROTATE_MODEL to rotate model instead of camera")


if __name__ == "__main__":
    main()
