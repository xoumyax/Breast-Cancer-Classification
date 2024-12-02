import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load feature dataset
input_csv = "/Users/mac/Desktop/TAMU/2024 FALL/ECEN 649 Pattern Reg/Project/gray_svm/test/glcm_11_features.csv"
data = pd.read_csv(input_csv)

# Ensure the dataset includes a 'label' column for classification
if 'label' not in data.columns:
    raise ValueError("The dataset is missing a 'label' column for classification!")

# Separate features and labels
X = data.drop(columns=['file_name', 'label'])  # Drop the filename and label columns
y = data['label']  # Labels: 0 for benign, 1 for malignant

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Calculate Gamma for the RBF kernel
# Gamma = 1 / number of features
num_features = X_train.shape[1]  # Number of features in the dataset
gamma = 1 / num_features

# Train SVM with RBF kernel
svm_model = SVC(C=1, kernel='rbf', gamma=gamma, tol=0.001, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# Predict on the test set
y_pred = svm_model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Classification Accuracy: {accuracy * 100:.2f}%\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))
