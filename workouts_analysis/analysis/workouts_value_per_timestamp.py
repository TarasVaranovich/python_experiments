import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from workouts_analysis import WORKOUT_STATS_SORTED, WORKOUTS_DIR


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    workouts_df["timestamp"] = pd.to_datetime(workouts_df["timestamp"])
    sns.scatterplot(data=workouts_df, x='timestamp', y='value')
    plt.savefig(WORKOUTS_DIR + "value_per_timestamp.jpg")


main()
