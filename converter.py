from PIL import Image
import os
import sys # Import sys to access command-line arguments

def convert_png_to_jpg(input_folder, output_folder):
    """
    Converts all PNG files in the input_folder to JPG files in the output_folder.
    """
    print(f"Starting conversion in folder: {input_folder}")
    
    # 1. Create the output folder if it doesn't exist (e.g., in the same directory as the script)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    # 2. Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            try:
                # ... (rest of the conversion logic remains the same) ...
                input_filepath = os.path.join(input_folder, filename)
                base_name = os.path.splitext(filename)[0]
                output_filename = base_name + '.jpg'
                output_filepath = os.path.join(output_folder, output_filename)

                img = Image.open(input_filepath)

                if img.mode == 'RGBA':
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3])
                    img = background

                img.save(output_filepath, 'JPEG', quality=95)
                
                print(f"✅ Converted: {filename} -> {output_filename}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
        
        else:
            # print(f"⏭️ Skipping non-PNG file: {filename}")
            pass


if __name__ == "__main__":
    # --- Check for arguments from the Batch file ---
    
    # sys.argv[1] will be the folder path passed by the batch script
    if len(sys.argv) > 1:
        # Use the folder selected by the batch file as the input
        selected_input_dir = sys.argv[1]
        
        # Set the output folder to a predictable name (e.g., 'jpg_output')
        # You can change this to a specific path if needed
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'jpg_output') 

        convert_png_to_jpg(selected_input_dir, output_dir)
        
    else:
        # Fallback if the script is run directly without arguments
        print("Please run this script via the 'RunConverter.bat' file.")
        print("Conversion aborted.")