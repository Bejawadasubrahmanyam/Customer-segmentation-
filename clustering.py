from sklearn.cluster import KMeans

def perform_clustering(df, scaled_data):
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_data)
    return df
