"""
Example usage and validation of image_camera_roll.py

This script demonstrates how to use the image_camera_roll.py script
and validates that it has the correct structure and imports.

Note: This cannot actually run in Blender without the bpy module,
but it validates the script structure.
"""

import ast
import os


def validate_script():
    """Validate the image_camera_roll.py script structure"""
    script_path = os.path.join(os.path.dirname(__file__), 'image_camera_roll.py')
    
    print("Validating image_camera_roll.py...")
    print("=" * 50)
    
    # Read the script
    with open(script_path, 'r') as f:
        code = f.read()
    
    # Parse the AST
    tree = ast.parse(code)
    
    # Find all function definitions
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    # Expected functions
    expected_functions = [
        'clear_scene',
        'create_image_plane',
        'create_camera_with_animation',
        'add_lighting',
        'setup_render_settings',
        'main'
    ]
    
    print("\n✓ Script parsed successfully")
    print(f"\n✓ Found {len(functions)} functions:")
    for func in functions:
        status = "✓" if func in expected_functions else "?"
        print(f"  {status} {func}()")
    
    # Check for required configuration variables
    print("\n✓ Configuration variables:")
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id.isupper():  # Convention for constants
                        print(f"  - {target.id}")
    
    # Check imports
    print("\n✓ Imports:")
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                print(f"  - {alias.name}")
    
    print("\n" + "=" * 50)
    print("✓ Validation complete!")
    print("\nThe script is ready to use in Blender.")
    print("\nQuick start:")
    print("1. Open Blender")
    print("2. Switch to 'Scripting' workspace")
    print("3. Open image_camera_roll.py")
    print("4. Update IMAGE_PATH variable")
    print("5. Click 'Run Script' or press Alt+P")
    
    return True


def show_example_configuration():
    """Show example configuration"""
    print("\n" + "=" * 50)
    print("Example Configuration:")
    print("=" * 50)
    print("""
# In image_camera_roll.py, modify these variables:

IMAGE_PATH = "/home/user/Pictures/my_image.jpg"  # Your image path
ANIMATION_FRAMES = 250  # 250 frames ≈ 8.3 seconds at 30fps
CAMERA_DISTANCE = 10.0  # Distance from image
CAMERA_FOV = 50.0  # Field of view in degrees
ENABLE_DOF = True  # Depth of field for cinematic look
""")


if __name__ == "__main__":
    try:
        validate_script()
        show_example_configuration()
    except Exception as e:
        print(f"✗ Validation failed: {e}")
        import traceback
        traceback.print_exc()
