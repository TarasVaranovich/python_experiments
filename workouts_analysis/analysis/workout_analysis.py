import pandas as pd

from workouts_analysis import WORKOUT_STATS_PATH


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_PATH)
    print(workouts_df)

main()