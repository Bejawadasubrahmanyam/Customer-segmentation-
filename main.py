from src.preprocess import load_and_clean
from src.clustering import perform_clustering
from src.visualize import plot_clusters

def main():
    df, scaled_data = load_and_clean("data/customers.csv")
    df = perform_clustering(df, scaled_data)
    plot_clusters(df)

if __name__ == "__main__":
    main()
