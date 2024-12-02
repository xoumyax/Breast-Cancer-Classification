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
input_folder = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/gray_svm/Calc_Training_Images'

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
            #img.save(png_file_path, format="PNG")
            
            # grayscale
            gray_img = img.convert('L')
            
            # save
            gray_png_file_path = os.path.join(output_folder, f"gray_{png_file_name}")
            gray_img.save(gray_png_file_path, format="PNG")
            
            processed_count += 1
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

print(f"Done: {processed_count} ，Save path：{output_folder}")

#%% Histogram Equalization
import cv2
import numpy as np

input_folder = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/gray_svm/gray'

output_folder = select_output_folder()

os.makedirs(output_folder, exist_ok=True)

processed_equalized_count = 0
for file_name in os.listdir(input_folder):
    gray_file_path = os.path.join(input_folder, file_name)
    try:
        gray_img = Image.open(gray_file_path)
        gray_np = np.array(gray_img)
        
        equalized_img = cv2.equalizeHist(gray_np)
        
        equalized_file_name = os.path.basename(gray_file_path).replace("gray_", "equalized_")
        equalized_file_path = os.path.join(output_folder, equalized_file_name)
        Image.fromarray(equalized_img).save(equalized_file_path, format="PNG")
        
        processed_equalized_count += 1
    except Exception as e:
        print(f"Error processing file {gray_file_path}: {e}")

print(f"Histogram Equalization Done: {processed_equalized_count} ")