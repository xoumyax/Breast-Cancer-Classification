import os
import pandas as pd
import numpy as np
from skimage.feature import graycomatrix, graycoprops
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale
input_folder = '/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/gray_svm/HE_imag'
output_csv = "/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/gray_svm/test/glcm_features_135deg.csv"

# Define parameters for GLCM
distances = [1]  # D = 1
#angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Θ = 0°, 45°, 90°, 135°
angles = [3*np.pi/4]
all_features = []

# Function to normalize GLCM
def normalize_glcm(glcm):
    """Normalize the GLCM matrix."""
    glcm_sum = glcm.sum(axis=(0, 1), keepdims=True)  # Total sum of GLCM elements
    normalized_glcm = glcm / glcm_sum  # Normalize each element
    return normalized_glcm

def compute_glcm_features(glcm, normalized_glcm):
    G, _, _, num_angles = glcm.shape
    features = {}

    features['correlation'] = graycoprops(normalized_glcm, 'correlation').mean()
    features['homogeneity'] = graycoprops(normalized_glcm, 'homogeneity').mean()
    features['contrast'] = graycoprops(normalized_glcm, 'contrast').mean()
    features['ASM'] = graycoprops(normalized_glcm, 'ASM').mean()
    features['energy'] = graycoprops(normalized_glcm, 'energy').mean()
    features['dissimilarity'] = graycoprops(normalized_glcm, 'dissimilarity').mean()

    i_indices = np.arange(G)[:, None, None, None]  # (256, 1, 1, 1)
    j_indices = np.arange(G)[None, :, None, None]  # (1, 256, 1, 1)
    
    mean = normalized_glcm.mean(axis=(0, 1, 2))
    variance = np.sum(normalized_glcm * (i_indices - mean)**2, axis=(0, 1, 2))
    features['variance'] = variance.mean()

    features['maximum_probability'] = normalized_glcm.max(axis=(0, 1)).mean()
    features['sum_average'] = 0.5 * np.sum(
        normalized_glcm * (i_indices + j_indices),
        axis=(0, 1, 2)
    ).mean()

    return features

for file_name in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, file_name)

    if os.path.isfile(input_file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        try:
            image = imread(input_file_path)
            
            # Compute the GLCM
            glcm = graycomatrix(image, distances=distances, angles=angles, levels=256, symmetric=True, normed=True)

            # Normalize the GLCM
            normalized_glcm = normalize_glcm(glcm)

            # Extract GLCM features
            glcm_features = compute_glcm_features(glcm, normalized_glcm)
            features = {'file_name': file_name}
            features.update(glcm_features)

            all_features.append(features)
            print(f"Processed {file_name}")

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Save to csv
features_df = pd.DataFrame(all_features)
features_df.to_csv(output_csv, index=False)

print(f"GLCM Done! {output_csv}")
