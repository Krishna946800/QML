import pennylane as qml
from pennylane import numpy as np
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import cv2
import random
import os
import pickle
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import random
from PIL import Image


dataset = "cat_v1"
categories = ["Bengal", "Domestic_Shorthair", "Maine_Coon", "Ragdoll", "Siamese"]
num_images = 500

image_size = (256, 256)  

def nearest_power_of_2(n):
    return 2 ** int(np.ceil(np.log2(n)))

for category in categories:
    folder_path = os.path.join(dataset, category)
    images = os.listdir(folder_path)[:num_images] 

quantum_encoded_images = []

for category in categories:
    folder_path = os.path.join(dataset, category)
    image_paths = [os.path.join(folder_path, img) for img in images]
    images = os.listdir(folder_path)[:num_images] 

    for img_file in tqdm(images, desc=f"Encoding {category} images"):
        try:
            
            img_path = os.path.join(folder_path, img_file)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, image_size)  
            image = image.flatten() / 256.0 

            target_size = nearest_power_of_2(len(image)) 
            num_qubits = int(np.log2(target_size))  


            dev = qml.device("default.qubit", wires=num_qubits)

            @qml.qnode(dev)
            def quantum_image_encoding(image):
                qml.AmplitudeEmbedding(features=image, wires=range(num_qubits), normalize=True, pad_with=0.0)
                return qml.state()

            padded_image = np.pad(image, (0, target_size - len(image)), 'constant')

            quantum_state = quantum_image_encoding(padded_image)
            quantum_encoded_images.append((category, img_file, quantum_state))
        
        except Exception as e:
            print(f"Error processing {img_file}: {e}")

with open("quantum_encoded_pet_images.pkl", "wb") as f:
    pickle.dump(quantum_encoded_images, f)

print("Encoding Sucessfull!")

with open("quantum_encoded_pet_images.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    
random_entries = random.sample(loaded_data, 10)

for i, (category, filename, quantum_state) in enumerate(random_entries):
    print(f"\n Entry {i+1}")
    print(f"Category : {category}")
    print(f"Filename : {filename}")
    print(f" Quantum State (Size: {len(quantum_state)}):")
    print(quantum_state[:10])