import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np


model_name = "Facenet"

print(DeepFace.verify(img1_path="reference3.jpg",
      img2_path="reference4.jpg", model_name=model_name))
embedding = DeepFace.represent(
    img_path="reference4.jpg", model_name=model_name)[0]["embedding"]


# Check if the embedding list is empty or has fewer elements
if len(embedding) < 2:
    print("Error: Unable to generate embeddings.")
else:
    # Plot embeddings
    embedding = np.array(embedding)
    embedding = embedding.reshape((1, -1))

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 5))
    cax = ax.imshow(embedding, cmap='viridis', aspect='auto')

    # Set colorbar
    cbar = fig.colorbar(cax)
    cbar.set_label('Dimension Value')

    # Remove unnecessary plot elements
    ax.axis('off')

    # Show the plot
    plt.show()
