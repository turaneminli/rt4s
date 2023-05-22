from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

model_name = "VGG-Face"

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
    fig = plt.figure(figsize=(10, 5))
    gs = GridSpec(1, 2, width_ratios=[1, 1])

    # Show image on the left
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.imshow(plt.imread("reference4.jpg"))
    ax1.axis('off')

    # Plot embeddings on the right
    ax2 = fig.add_subplot(gs[0, 1])
    cax = ax2.imshow(embedding, cmap=plt.cm.ocean, aspect='auto')
    ax2.axis('off')

    # Set colorbar
    cbar = fig.colorbar(cax)
    cbar.set_label('Dimension Value')

    # Show the plot
    plt.show()
