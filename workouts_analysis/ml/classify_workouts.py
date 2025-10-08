import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

from workouts_analysis import WORKOUT_STATS_SORTED


# https://www.datacamp.com/tutorial/k-means-clustering-python
def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    workouts_df["timestamp"] = pd.to_datetime(workouts_df["timestamp"])
    workouts_df["timestamp"] = workouts_df["timestamp"].astype('int64')

    X_train, X_test, y_train, y_test = train_test_split(workouts_df[['timestamp']],
                                                        workouts_df[['value']], test_size=0.33,
                                                        random_state=0)
    X_train_norm = preprocessing.normalize(X_train)
    X_test_norm = preprocessing.normalize(X_test)
    # TODO: What means fitting model?
    kmeans = KMeans(n_clusters=3, random_state=0, n_init='auto')
    kmeans.fit(X_train_norm)
    # TODO: here is an issue
    sns.scatterplot(data=X_train, x='timestamp', y='value', hue=kmeans.labels_)
    sns.boxplot(x=kmeans.labels_, y=y_train['stats_classification'])

    silhouette_score(X_train_norm, kmeans.labels_, metric='euclidean')


main()
