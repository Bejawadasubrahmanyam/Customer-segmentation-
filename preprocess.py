import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean(path):
    df = pd.read_csv(path)
    df = df.dropna()

    features = df[['Age', 'Annual Income', 'Spending Score']]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    return df, scaled_data
