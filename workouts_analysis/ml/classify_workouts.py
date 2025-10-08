import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from workouts_analysis import WORKOUT_STATS_SORTED, WORKOUTS_DIR


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    print(workouts_df)
    sns.scatterplot(data=workouts_df, x='timestamp', y='value')
    plt.savefig(WORKOUTS_DIR + "value_per_timestamp.jpg")
    #https://www.datacamp.com/tutorial/k-means-clustering-python


main()
