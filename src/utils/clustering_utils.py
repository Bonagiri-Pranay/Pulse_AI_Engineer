from sklearn.cluster import AgglomerativeClustering

def cluster_embeddings(embs, threshold=0.25):
    model = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=threshold,
        metric="cosine",
        linkage="average"
    )
    return model.fit_predict(embs)
