from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pickle
import os


def train_kmeans(data, n_cluster = 3, randome_state = 42):
    k_model =  KMeans(n_clusters=n_cluster, random_state= randome_state )
    k_model.fit(data)

    labels = k_model.labels_
    scores =  silhouette_score(data, labels)
    print(f'silhoutte score of clusters is : {scores:.4f}')
    return k_model


'''
save model in pickle
'''
def save_model(model, path):
    with open(path, mode= 'wb') as f:
        pickle.dump(path, f)
    print(f'model save as {path}')


if __name__ == "__main__":
    import pandas as pd
    data =  pd.read_csv('D:\ml_clusters\src\data\preprocess_data.py')
    model = train_kmeans(data)

    save_model(model, 'D:\ml_clusters\src\outputs\k_means.pkl')

