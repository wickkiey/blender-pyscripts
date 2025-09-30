"""
Blender Python Script: Image Camera Roll Animation
This script inserts an image into 3D space and creates a camera animation
that rolls from top to bottom of the image for a cinematic view with focus effects.

Usage:
1. Open Blender
2. Open the Scripting workspace
3. Load this script in the text editor
4. Update the IMAGE_PATH variable to point to your image file
5. Run the script (Alt+P or click Run Script button)
"""

import bpy
import math
import os

# Configuration
IMAGE_PATH = "/path/to/your/image.jpg"  # Update this path to your image
ANIMATION_FRAMES = 250  # Total frames for the animation
CAMERA_DISTANCE = 10.0  # Distance of camera from image plane
CAMERA_FOV = 50.0  # Camera field of view in degrees
ENABLE_DOF = True  # Enable depth of field for cinematic focus


def clear_scene():
    """Clear default scene objects"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def create_image_plane(image_path):
    """
    Create a plane with the image as texture
    Returns: (plane object, image dimensions)
    """
    # Load the image
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = bpy.data.images.load(image_path)
    img_width = img.size[0]
    img_height = img.size[1]
    
    # Calculate aspect ratio
    aspect_ratio = img_width / img_height
    
    # Create plane with correct aspect ratio
    # Base height of 10 units
    plane_height = 10.0
    plane_width = plane_height * aspect_ratio
    
    bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0, 0))
    plane = bpy.context.active_object
    plane.name = "ImagePlane"
    plane.scale = (plane_width / 2, plane_height / 2, 1)
    
    # Create material with image texture
    mat = bpy.data.materials.new(name="ImageMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    nodes.clear()
    
    # Create shader nodes
    node_tex = nodes.new(type='ShaderNodeTexImage')
    node_tex.image = img
    node_tex.location = (0, 0)
    
    node_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    node_bsdf.location = (300, 0)
    
    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    node_output.location = (600, 0)
    
    # Link nodes
    links.new(node_tex.outputs['Color'], node_bsdf.inputs['Base Color'])
    links.new(node_bsdf.outputs['BSDF'], node_output.inputs['Surface'])
    
    # Assign material to plane
    if plane.data.materials:
        plane.data.materials[0] = mat
    else:
        plane.data.materials.append(mat)
    
    return plane, (plane_width, plane_height)


def create_camera_with_animation(plane, plane_dimensions):
    """
    Create camera and animate it to roll from top to bottom of the image
    """
    plane_width, plane_height = plane_dimensions
    
    # Create camera
    bpy.ops.object.camera_add(location=(0, -CAMERA_DISTANCE, 0))
    camera = bpy.context.active_object
    camera.name = "AnimatedCamera"
    
    # Set camera properties
    camera.data.lens_unit = 'FOV'
    camera.data.angle = math.radians(CAMERA_FOV)
    
    # Point camera at the plane center initially
    camera.rotation_euler = (math.radians(90), 0, 0)
    
    # Enable depth of field for cinematic effect
    if ENABLE_DOF:
        camera.data.dof.use_dof = True
        camera.data.dof.focus_distance = CAMERA_DISTANCE
        camera.data.dof.aperture_fstop = 2.8  # Shallow depth of field
    
    # Set as active camera
    bpy.context.scene.camera = camera
    
    # Calculate camera positions
    # Start at top of image, end at bottom
    top_z = plane_height / 2
    bottom_z = -plane_height / 2
    
    # Set animation frame range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = ANIMATION_FRAMES
    
    # Keyframe camera position at start (top of image)
    bpy.context.scene.frame_set(1)
    camera.location.z = top_z
    camera.keyframe_insert(data_path="location", index=2)
    
    # Keyframe camera position at end (bottom of image)
    bpy.context.scene.frame_set(ANIMATION_FRAMES)
    camera.location.z = bottom_z
    camera.keyframe_insert(data_path="location", index=2)
    
    # Set interpolation to smooth (ease in/out)
    if camera.animation_data and camera.animation_data.action:
        for fcurve in camera.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO'
                keyframe.handle_right_type = 'AUTO'
    
    # Update depth of field focus to follow camera
    if ENABLE_DOF:
        # The focus distance should remain constant as we're moving parallel to the plane
        camera.data.dof.focus_distance = CAMERA_DISTANCE
    
    return camera


def add_lighting():
    """Add basic lighting to the scene"""
    # Add sun light for even illumination
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
    sun = bpy.context.active_object
    sun.name = "SunLight"
    sun.data.energy = 1.0
    sun.rotation_euler = (math.radians(45), 0, math.radians(45))
    
    # Add fill light
    bpy.ops.object.light_add(type='AREA', location=(-5, -5, 5))
    fill = bpy.context.active_object
    fill.name = "FillLight"
    fill.data.energy = 0.5
    fill.data.size = 5.0
    
    return sun, fill


def setup_render_settings():
    """Configure render settings for better quality"""
    scene = bpy.context.scene
    
    # Set render resolution
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    
    # Set frame rate
    scene.render.fps = 30
    
    # Use Cycles for better rendering (optional, Eevee is faster for preview)
    scene.render.engine = 'BLENDER_EEVEE'
    
    # Enable motion blur for smoother animation
    scene.eevee.use_motion_blur = True
    scene.render.film_transparent = False


def main():
    """Main function to set up the scene"""
    print("Starting Image Camera Roll Animation setup...")
    
    # Check if image path is set
    if IMAGE_PATH == "/path/to/your/image.jpg":
        print("\nWARNING: Please update IMAGE_PATH variable with your actual image path!")
        print("The script will continue with a placeholder, but you need to set a real image path.")
        return
    
    # Clear the scene
    print("Clearing scene...")
    clear_scene()
    
    # Create image plane
    print(f"Loading image from: {IMAGE_PATH}")
    plane, dimensions = create_image_plane(IMAGE_PATH)
    print(f"Image plane created with dimensions: {dimensions[0]:.2f} x {dimensions[1]:.2f}")
    
    # Create animated camera
    print("Creating camera with animation...")
    camera = create_camera_with_animation(plane, dimensions)
    print(f"Camera animation set up: {ANIMATION_FRAMES} frames")
    
    # Add lighting
    print("Adding lighting...")
    add_lighting()
    
    # Setup render settings
    print("Configuring render settings...")
    setup_render_settings()
    
    # Set initial frame
    bpy.context.scene.frame_set(1)
    
    print("\n=== Setup Complete! ===")
    print(f"Animation runs from frame 1 to {ANIMATION_FRAMES}")
    print(f"Camera rolls from top to bottom of the image")
    print(f"Depth of Field: {'Enabled' if ENABLE_DOF else 'Disabled'}")
    print("\nPress Spacebar to preview the animation")
    print("Press Ctrl+F12 to render the animation")


if __name__ == "__main__":
    main()
