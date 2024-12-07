""" 
Problem: 
As the paper mention that they use the "Calc-Training Full Mammogram Images (DICOM) dataset" which consist 1546 data,
but the result of my code is 1227 data.
"""
import pandas as pd
import os
import shutil

# image path
base_image_path = "/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/"

# import datasets 
target_folder = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/Calc_Test_Images'
os.makedirs(target_folder, exist_ok=True)

# import csv
csv_file_path = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/CBIS-DDSM/csv/dicom_info.csv'
dicom_data = pd.read_csv(csv_file_path)

"""
# PatientID which start with Calc-Training"
calc_training_images = dicom_data[dicom_data['PatientID'].str.startswith('Calc-Training', na=False) & 
                                 (dicom_data['SeriesDescription'] == 'full mammogram images')]

# PatientID which start with Calc-Training"
calc_training_images = dicom_data[dicom_data['PatientID'].str.startswith('Calc-Test', na=False) & 
                                 (dicom_data['SeriesDescription'].notna()) &
                                 (dicom_data['SeriesDescription'] != '')]
"""
calc_training_images = dicom_data[dicom_data['PatientID'].str.startswith('Calc-Test', na=False)]
#%%%
stored_count = 0

# Copy images to new file
for _, row in calc_training_images.iterrows():
    image_path = os.path.join(base_image_path,row['image_path'])
    patient_id = row['PatientID']
    
    if os.path.exists(image_path):
        extension = os.path.splitext(image_path)[1]
        # name the files
        new_file_name = f"{patient_id}{extension}"
        new_file_path = os.path.join(target_folder, new_file_name)
        
        # file name exist
        version = 2
        while os.path.exists(new_file_path):
            new_file_name = f"{patient_id}_v{version}{extension}"
            new_file_path = os.path.join(target_folder, new_file_name)
            version += 1
        
        # copy and rename
        shutil.copy(image_path, new_file_path)
        stored_count += 1
    else:
        print(f"Can not find the file: {image_path}")

print(f"Done. Successfully stored {stored_count} images in the folder: {target_folder}")
