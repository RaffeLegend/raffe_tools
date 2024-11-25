import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

def load_files_from_folder(folder_path):
    file_contents = []
    file_names = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents.append(file.read())
                file_names.append(file_name)
    return file_contents, file_names

def cluster_files(file_contents, num_clusters=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(file_contents)
    
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
    plt.show()

if __name__ == "__main__":
    folder_path = 'Users/river/Downloads/frequency'
    file_contents, file_names = load_files_from_folder(folder_path)
    kmeans, X = cluster_files(file_contents)
    visualize_clusters(kmeans, X, file_names)