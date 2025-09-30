"""
Example Workflow: TRELLIS 3D Generation Pipeline

This script demonstrates the complete workflow from text/image to 3D model viewing in Blender.
It shows how the different scripts work together.

Note: This is for demonstration purposes. Actual TRELLIS integration requires
following the setup in TRELLIS_SETUP.md
"""

import os
import sys


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def demonstrate_workflow():
    """Demonstrate the complete TRELLIS workflow"""
    
    print_section("TRELLIS 3D Generation Workflow Demo")
    
    print("This repository provides a complete pipeline for:")
    print("1. Generating 3D models from text/images using TRELLIS")
    print("2. Viewing and animating the models in Blender")
    print("3. Creating cinematic presentations")
    
    # Step 1: Installation
    print_section("Step 1: Installation")
    print("First, install TRELLIS dependencies:")
    print("\n  $ chmod +x install_trellis.sh")
    print("  $ ./install_trellis.sh")
    print("\nThis will:")
    print("  ✓ Create a virtual environment (venv_trellis)")
    print("  ✓ Install PyTorch")
    print("  ✓ Install Gradio and other dependencies")
    print("  ✓ Prepare for TRELLIS model usage")
    
    # Step 2: Generate 3D Model
    print_section("Step 2: Generate 3D Model")
    print("Start the Gradio web application:")
    print("\n  $ source venv_trellis/bin/activate")
    print("  $ python gradio_trellis_app.py")
    print("\nThen in your browser (http://localhost:7860):")
    print("  1. Enter a text prompt (e.g., 'a red dragon')")
    print("  2. OR upload an image")
    print("  3. Click 'Generate 3D Model'")
    print("  4. Download the generated .glb or .obj file")
    print("\nExample prompts:")
    print("  • 'a medieval sword with silver blade'")
    print("  • 'a modern coffee mug, ceramic, blue'")
    print("  • 'a futuristic spaceship'")
    
    # Step 3: View in Blender
    print_section("Step 3: View in Blender")
    print("Two options for viewing:")
    print("\nOption A - Manual Import:")
    print("  1. Open Blender")
    print("  2. File → Import → glTF 2.0 (.glb)")
    print("  3. Select your downloaded model")
    print("\nOption B - Automated Setup (Recommended):")
    print("  1. Open Blender")
    print("  2. Go to Scripting workspace")
    print("  3. Open 'model_viewer_blender.py'")
    print("  4. Update MODEL_PATH to your .glb file")
    print("  5. Run script (Alt+P)")
    print("\nThe script will automatically:")
    print("  ✓ Import and center the model")
    print("  ✓ Set up professional lighting")
    print("  ✓ Create turntable animation")
    print("  ✓ Configure camera and render settings")
    
    # Step 4: Customize
    print_section("Step 4: Customize (Optional)")
    print("In model_viewer_blender.py, you can adjust:")
    print("\n  LIGHTING_STYLE = 'studio'  # or 'outdoor', 'dramatic'")
    print("  CAMERA_DISTANCE = 10.0     # Adjust framing")
    print("  CAMERA_HEIGHT = 5.0        # Camera height")
    print("  ROTATE_MODEL = False       # True to rotate model instead of camera")
    print("  ENABLE_DOF = True          # Depth of field effect")
    
    # Step 5: Render
    print_section("Step 5: Render")
    print("In Blender:")
    print("  • Press SPACEBAR to preview animation")
    print("  • Press F12 to render a single frame")
    print("  • Press Ctrl+F12 to render full animation")
    print("\nOutput will be saved to Blender's output directory")
    print("(Default: /tmp/ on Linux, C:\\tmp\\ on Windows)")
    
    # Additional Scripts
    print_section("Bonus: Image Animation")
    print("For static images, use image_camera_roll.py:")
    print("\n  1. Open Blender")
    print("  2. Load image_camera_roll.py in Scripting workspace")
    print("  3. Update IMAGE_PATH to your image")
    print("  4. Run script (Alt+P)")
    print("\nThis creates a cinematic camera roll animation from top to bottom!")
    
    # Example Files
    print_section("Example Output Files")
    print("The workflow produces:")
    print("\n  outputs/")
    print("  ├── 20240930_143022_red_dragon.glb     # Generated 3D model")
    print("  ├── 20240930_143045_coffee_mug.glb     # Another model")
    print("  └── 20240930_143100_from_image.glb     # From image conversion")
    print("\nThese can all be loaded into Blender!")
    
    # Resources
    print_section("Resources & Documentation")
    print("📚 Documentation:")
    print("  • TRELLIS_SETUP.md - Complete setup guide")
    print("  • QUICKSTART.md - Quick start for image_camera_roll.py")
    print("  • README.md - Overview of all scripts")
    print("\n🔗 Links:")
    print("  • TRELLIS: https://github.com/microsoft/TRELLIS")
    print("  • Gradio: https://gradio.app")
    print("  • Blender: https://www.blender.org")
    
    # Tips
    print_section("Pro Tips")
    print("💡 Generation Tips:")
    print("  • Use descriptive prompts with materials and style")
    print("  • Higher inference steps = better quality (but slower)")
    print("  • GPU greatly speeds up generation (5-10x faster)")
    print("\n💡 Blender Tips:")
    print("  • GLB format is recommended (single file, includes textures)")
    print("  • Use 'studio' lighting for product visualization")
    print("  • Use 'dramatic' lighting for artistic renders")
    print("  • Adjust CAMERA_DISTANCE if model is too large/small")
    print("\n💡 Performance:")
    print("  • Text-to-3D: ~30s-2min on GPU, ~5-15min on CPU")
    print("  • Image-to-3D: Similar timing")
    print("  • Blender rendering: Depends on quality settings")
    
    # Summary
    print_section("Quick Reference")
    print("Complete workflow in commands:")
    print("\n  # 1. Install")
    print("  ./install_trellis.sh")
    print("\n  # 2. Generate model")
    print("  source venv_trellis/bin/activate")
    print("  python gradio_trellis_app.py")
    print("  # → Use web UI to generate and download model")
    print("\n  # 3. View in Blender")
    print("  # → Open Blender, load model_viewer_blender.py")
    print("  # → Update MODEL_PATH, run script")
    print("\n  # 4. Render")
    print("  # → Press Ctrl+F12 in Blender")
    
    print("\n" + "=" * 60)
    print("  Happy 3D Generation! 🎨🖼️➡️🎭")
    print("=" * 60 + "\n")


def check_installation():
    """Check if files are present"""
    print_section("Installation Check")
    
    required_files = [
        'install_trellis.sh',
        'gradio_trellis_app.py',
        'model_viewer_blender.py',
        'image_camera_roll.py',
        'TRELLIS_SETUP.md',
        'README.md'
    ]
    
    all_present = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_present = False
    
    if all_present:
        print("\n✓ All required files are present!")
    else:
        print("\n✗ Some files are missing. Please check the installation.")
        return False
    
    # Check if outputs directory exists
    if not os.path.exists('outputs'):
        print("\nCreating outputs directory...")
        os.makedirs('outputs')
        print("  ✓ outputs/ directory created")
    else:
        print("\n  ✓ outputs/ directory exists")
    
    return True


def main():
    """Main function"""
    if not check_installation():
        print("\nPlease ensure all files are present before continuing.")
        return 1
    
    demonstrate_workflow()
    
    print("\nFor detailed instructions, see:")
    print("  • TRELLIS_SETUP.md - Full setup and usage guide")
    print("  • README.md - Overview and quick start")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
