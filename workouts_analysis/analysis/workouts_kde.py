import pandas as pd
from matplotlib import pyplot as plt

from workouts_analysis import WORKOUT_STATS_SORTED, WORKOUTS_DIR


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    workouts_df.plot.kde()
    plt.savefig(WORKOUTS_DIR + "workouts_kde.jpg")


main()
