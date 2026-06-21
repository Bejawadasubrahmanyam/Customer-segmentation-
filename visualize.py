import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(df):
    plt.figure()
    sns.scatterplot(
        x=df['Annual Income'],
        y=df['Spending Score'],
        hue=df['Cluster'],
        palette='Set1'
    )
    plt.title("Customer Segmentation")
    plt.savefig("outputs/cluster_plot.png")
    plt.show()
