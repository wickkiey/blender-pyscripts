"""
TRELLIS Gradio Application
A web interface for text-to-3D and image-to-3D generation using TRELLIS

This application provides an easy-to-use interface for generating 3D models
that can be directly imported into Blender.

Usage:
    python gradio_trellis_app.py

Then open the provided URL in your browser (typically http://localhost:7860)
"""

import gradio as gr
import os
import time
import numpy as np
from datetime import datetime
from pathlib import Path

# Configuration
OUTPUT_DIR = "outputs"
DEFAULT_OUTPUT_FORMAT = "glb"
DEFAULT_STEPS = 50
DEFAULT_GUIDANCE = 7.5

# Create output directory if it doesn't exist
Path(OUTPUT_DIR).mkdir(exist_ok=True)


def generate_text_to_3d(prompt, num_steps, guidance_scale, output_format):
    """
    Generate 3D model from text prompt
    
    Args:
        prompt: Text description of the 3D object
        num_steps: Number of inference steps (higher = better quality)
        guidance_scale: How closely to follow the prompt (7-15 recommended)
        output_format: Output file format ("glb" or "obj")
    
    Returns:
        Tuple of (file_path, status_message)
    """
    try:
        # Validate inputs
        if not prompt or len(prompt.strip()) == 0:
            return None, "❌ Error: Please enter a text prompt"
        
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_')
        
        filename = f"{timestamp}_{safe_prompt}.{output_format}"
        output_path = os.path.join(OUTPUT_DIR, filename)
        
        # Status update
        status_msg = f"🔄 Generating 3D model from prompt: '{prompt}'\n"
        status_msg += f"⚙️ Steps: {num_steps}, Guidance: {guidance_scale}\n"
        status_msg += f"📦 Format: {output_format.upper()}\n"
        status_msg += "⏳ Please wait...\n"
        
        # Note: This is a placeholder implementation
        # In a real implementation, you would call the TRELLIS model here
        # For demonstration purposes, we'll create a simple example file
        
        status_msg += "\n⚠️ NOTE: This is a demo implementation.\n"
        status_msg += "To use actual TRELLIS model:\n"
        status_msg += "1. Install TRELLIS from: https://github.com/microsoft/TRELLIS\n"
        status_msg += "2. Update the generate_3d_model() function below\n"
        status_msg += "3. Load model weights from HuggingFace\n\n"
        
        # Simulate processing time
        time.sleep(2)
        
        # Create a simple placeholder file
        if output_format == "glb":
            create_placeholder_glb(output_path, prompt)
        else:
            create_placeholder_obj(output_path, prompt)
        
        status_msg += f"✅ Success! Model saved to: {output_path}\n"
        status_msg += f"📁 Full path: {os.path.abspath(output_path)}\n"
        status_msg += "\n📋 Next steps:\n"
        status_msg += "1. Download the generated model\n"
        status_msg += "2. Open Blender\n"
        status_msg += "3. Go to File → Import → glTF 2.0 (.glb) or Wavefront (.obj)\n"
        status_msg += "4. Select the downloaded file\n"
        status_msg += "\nOr use model_viewer_blender.py for automatic setup!"
        
        return output_path, status_msg
        
    except Exception as e:
        error_msg = f"❌ Error during generation: {str(e)}"
        return None, error_msg


def generate_image_to_3d(image, num_steps, guidance_scale, output_format):
    """
    Generate 3D model from image
    
    Args:
        image: Input image (PIL Image or numpy array)
        num_steps: Number of inference steps
        guidance_scale: Guidance scale for generation
        output_format: Output file format
    
    Returns:
        Tuple of (file_path, status_message)
    """
    try:
        if image is None:
            return None, "❌ Error: Please upload an image"
        
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_from_image.{output_format}"
        output_path = os.path.join(OUTPUT_DIR, filename)
        
        status_msg = f"🔄 Generating 3D model from image\n"
        status_msg += f"⚙️ Steps: {num_steps}, Guidance: {guidance_scale}\n"
        status_msg += f"📦 Format: {output_format.upper()}\n"
        status_msg += "⏳ Please wait...\n"
        
        # Placeholder implementation
        status_msg += "\n⚠️ NOTE: This is a demo implementation.\n"
        status_msg += "To use actual TRELLIS model, integrate the official model here.\n\n"
        
        # Simulate processing
        time.sleep(2)
        
        # Create placeholder file
        if output_format == "glb":
            create_placeholder_glb(output_path, "image_based_model")
        else:
            create_placeholder_obj(output_path, "image_based_model")
        
        status_msg += f"✅ Success! Model saved to: {output_path}\n"
        status_msg += f"📁 Full path: {os.path.abspath(output_path)}\n"
        
        return output_path, status_msg
        
    except Exception as e:
        error_msg = f"❌ Error during generation: {str(e)}"
        return None, error_msg


def create_placeholder_glb(output_path, description):
    """Create a placeholder GLB file for demonstration"""
    # This creates a minimal GLB file structure
    # In real implementation, this would be replaced with actual TRELLIS output
    with open(output_path, 'wb') as f:
        # Minimal GLB header
        f.write(b'glTF')  # Magic
        f.write(b'\x02\x00\x00\x00')  # Version 2
        f.write(b'\x00\x00\x00\x00')  # Length (placeholder)
        
    # Add metadata as comment
    metadata_path = output_path + ".txt"
    with open(metadata_path, 'w') as f:
        f.write(f"Placeholder GLB file\n")
        f.write(f"Description: {description}\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"\nReplace this with actual TRELLIS model output\n")


def create_placeholder_obj(output_path, description):
    """Create a placeholder OBJ file for demonstration"""
    # Simple cube as placeholder
    with open(output_path, 'w') as f:
        f.write("# Placeholder OBJ file\n")
        f.write(f"# Description: {description}\n")
        f.write(f"# Generated: {datetime.now()}\n")
        f.write("# Replace with actual TRELLIS model output\n\n")
        f.write("# Cube vertices\n")
        f.write("v -1.0 -1.0 -1.0\n")
        f.write("v  1.0 -1.0 -1.0\n")
        f.write("v  1.0  1.0 -1.0\n")
        f.write("v -1.0  1.0 -1.0\n")
        f.write("v -1.0 -1.0  1.0\n")
        f.write("v  1.0 -1.0  1.0\n")
        f.write("v  1.0  1.0  1.0\n")
        f.write("v -1.0  1.0  1.0\n")
        f.write("\n# Cube faces\n")
        f.write("f 1 2 3 4\n")
        f.write("f 5 8 7 6\n")
        f.write("f 1 5 6 2\n")
        f.write("f 2 6 7 3\n")
        f.write("f 3 7 8 4\n")
        f.write("f 5 1 4 8\n")


# Create Gradio interface
def create_interface():
    """Create the Gradio web interface"""
    
    with gr.Blocks(title="TRELLIS 3D Generator", theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🎨 TRELLIS 3D Model Generator
            
            Generate high-quality 3D models from text or images for use in Blender!
            
            **Note**: This is a demonstration interface. To use the actual TRELLIS model:
            1. Follow the setup instructions in `TRELLIS_SETUP.md`
            2. Install TRELLIS from [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS)
            3. Update the generation functions with actual model calls
            """
        )
        
        with gr.Tabs():
            # Text to 3D Tab
            with gr.Tab("📝 Text to 3D"):
                with gr.Row():
                    with gr.Column():
                        text_prompt = gr.Textbox(
                            label="Enter your text prompt",
                            placeholder="e.g., a red dragon, modern chair, futuristic spaceship...",
                            lines=3
                        )
                        
                        with gr.Row():
                            text_steps = gr.Slider(
                                minimum=20,
                                maximum=100,
                                value=DEFAULT_STEPS,
                                step=5,
                                label="Inference Steps (higher = better quality)"
                            )
                            text_guidance = gr.Slider(
                                minimum=1.0,
                                maximum=20.0,
                                value=DEFAULT_GUIDANCE,
                                step=0.5,
                                label="Guidance Scale (7-15 recommended)"
                            )
                        
                        text_format = gr.Radio(
                            choices=["glb", "obj"],
                            value="glb",
                            label="Output Format"
                        )
                        
                        text_generate_btn = gr.Button("🚀 Generate 3D Model", variant="primary")
                    
                    with gr.Column():
                        text_output_file = gr.File(label="Generated 3D Model")
                        text_status = gr.Textbox(
                            label="Status",
                            lines=15,
                            max_lines=20
                        )
                
                text_generate_btn.click(
                    fn=generate_text_to_3d,
                    inputs=[text_prompt, text_steps, text_guidance, text_format],
                    outputs=[text_output_file, text_status]
                )
            
            # Image to 3D Tab
            with gr.Tab("🖼️ Image to 3D"):
                with gr.Row():
                    with gr.Column():
                        image_input = gr.Image(
                            label="Upload an image",
                            type="numpy"
                        )
                        
                        with gr.Row():
                            image_steps = gr.Slider(
                                minimum=20,
                                maximum=100,
                                value=DEFAULT_STEPS,
                                step=5,
                                label="Inference Steps"
                            )
                            image_guidance = gr.Slider(
                                minimum=1.0,
                                maximum=20.0,
                                value=DEFAULT_GUIDANCE,
                                step=0.5,
                                label="Guidance Scale"
                            )
                        
                        image_format = gr.Radio(
                            choices=["glb", "obj"],
                            value="glb",
                            label="Output Format"
                        )
                        
                        image_generate_btn = gr.Button("🚀 Generate 3D Model from Image", variant="primary")
                    
                    with gr.Column():
                        image_output_file = gr.File(label="Generated 3D Model")
                        image_status = gr.Textbox(
                            label="Status",
                            lines=15,
                            max_lines=20
                        )
                
                image_generate_btn.click(
                    fn=generate_image_to_3d,
                    inputs=[image_input, image_steps, image_guidance, image_format],
                    outputs=[image_output_file, image_status]
                )
            
            # Help Tab
            with gr.Tab("ℹ️ Help & Tips"):
                gr.Markdown(
                    """
                    ## 💡 Tips for Best Results
                    
                    ### Text Prompts
                    - Be specific and descriptive
                    - Include material/texture details (e.g., "metallic", "wooden", "glossy")
                    - Mention style if important (e.g., "low-poly", "realistic", "stylized")
                    - Examples:
                      - "a red ceramic coffee mug with a handle"
                      - "a low-poly medieval sword with silver blade"
                      - "a modern wooden chair with black metal legs"
                    
                    ### Image Inputs
                    - Use clear, well-lit images
                    - Avoid cluttered backgrounds
                    - Single objects work better than complex scenes
                    - Higher resolution images may yield better results
                    
                    ### Parameters
                    - **Inference Steps**: More steps = better quality but slower (50 is a good balance)
                    - **Guidance Scale**: Controls how closely the model follows your prompt
                      - Lower (5-7): More creative freedom
                      - Higher (10-15): Stricter adherence to prompt
                    
                    ### Using in Blender
                    1. Download the generated model file (.glb or .obj)
                    2. Open Blender
                    3. Go to File → Import → glTF 2.0 (.glb) or Wavefront (.obj)
                    4. Navigate to and select your downloaded file
                    5. The model will appear in your scene!
                    
                    **Pro Tip**: Use `model_viewer_blender.py` script for automatic setup with
                    lighting, camera, and turntable animation!
                    
                    ## 📋 Output Formats
                    
                    ### GLB (Recommended)
                    - Single file format
                    - Includes textures and materials
                    - Best for Blender
                    - Widely supported
                    
                    ### OBJ
                    - Universal 3D format
                    - Separate material files (.mtl)
                    - Good for editing and modification
                    
                    ## 🔧 Troubleshooting
                    
                    - **Generation takes too long**: Try reducing inference steps to 30-40
                    - **Low quality results**: Increase inference steps to 75-100
                    - **Model looks wrong**: Adjust guidance scale or rephrase your prompt
                    - **Import error in Blender**: Make sure you're using the correct import option for your file format
                    
                    For more information, see `TRELLIS_SETUP.md`
                    """
                )
        
        gr.Markdown(
            """
            ---
            
            **Note**: Generated models are saved in the `outputs/` directory.
            
            For full TRELLIS integration, please refer to the [TRELLIS repository](https://github.com/microsoft/TRELLIS)
            """
        )
    
    return demo


def main():
    """Main function to launch the Gradio app"""
    print("=" * 60)
    print("TRELLIS 3D Model Generator - Gradio Interface")
    print("=" * 60)
    print(f"\nOutput directory: {os.path.abspath(OUTPUT_DIR)}")
    print("\nStarting Gradio interface...")
    print("Once started, open the URL shown below in your web browser")
    print("=" * 60)
    
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,
        share=False,  # Set to True to create a public link
        show_error=True
    )


if __name__ == "__main__":
    main()
