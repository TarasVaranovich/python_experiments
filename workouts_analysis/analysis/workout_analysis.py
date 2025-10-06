import pandas as pd
from matplotlib import pyplot as plt

from workouts_analysis import WORKOUT_STATS_SORTED


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    workouts_df.plot.kde()
    plt.savefig("workouts_kde.jpg")

main()