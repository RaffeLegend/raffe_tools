import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from PIL import Image

import matplotlib.pyplot as plt


def load_images_from_folder(folder_path):
    file_contents = []
    file_names = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                with Image.open(file_path) as img:
                    file_contents.append(np.array(img))
                    file_names.append(file_name)
    return file_contents, file_names

def cluster_files(file_contents, num_clusters=5):

    flattened_images = [img.flatten() for img in file_contents]
    X = np.array(flattened_images)
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    return kmeans, X

def visualize_clusters(kmeans, X, file_names):
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X.toarray())
    
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(principal_components[:, 0], principal_components[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.legend(handles=scatter.legend_elements()[0], labels=set(kmeans.labels_))
    
    for i, file_name in enumerate(file_names):
        plt.annotate(file_name, (principal_components[i, 0], principal_components[i, 1]))
    
    plt.title('File Clustering Visualization')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.savefig('clustering_visualization.png')

if __name__ == "__main__":
    folder_path = '/mnt/data2/users/hilight/yiwei/dataset/frequency'
    file_contents, file_names = load_images_from_folder(folder_path)
    kmeans, X = cluster_files(file_contents)
    visualize_clusters(kmeans, X, file_names)