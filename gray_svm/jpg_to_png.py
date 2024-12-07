import os
from PIL import Image
from tkinter import Tk, filedialog


# Create new file
def select_output_folder():
    Tk().withdraw()
    folder_selected = filedialog.askdirectory(title="Select or Create Output Folder")
    if not folder_selected:
        print("No folder selected. Exiting.")
        exit()
    return folder_selected
#%%
input_folder = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/Calc_Test_Images'

output_folder = select_output_folder()

os.makedirs(output_folder, exist_ok=True)

# Image processing
processed_count = 0
for file_name in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, file_name)

    if os.path.isfile(input_file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        try:
            img = Image.open(input_file_path)
            
            # To .png
            png_file_name = os.path.splitext(file_name)[0] + ".png"
            png_file_path = os.path.join(output_folder, png_file_name)
            img.save(png_file_path, format="PNG")
            
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

print(f"Done: {processed_count} ，Save path：{output_folder}")
#%%
from PIL import Image
import os

image_folder = '//Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/samples/'

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    
    if os.path.isfile(image_path) and not image_name.startswith('.'):
        with Image.open(image_path) as img:
            print(f"{image_name}: {img.size}")  
#%%
from PIL import Image
import os

image_folder = '//Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/samples/'
output_folder = '//Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/samples/resized_samples/'
os.makedirs(output_folder, exist_ok=True)

target_size = (869, 1152)

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    
    if os.path.isfile(image_path) and not image_name.startswith('.'):
        with Image.open(image_path) as img:
           
            resized_img = img.resize(target_size)
            resized_img.save(os.path.join(output_folder, image_name))

print("Done")
