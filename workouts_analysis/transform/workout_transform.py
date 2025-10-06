import time

import pandas as pd

from workouts_analysis import WORKOUT_STATS_PATH


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_PATH, header=None, names=["timestamp", "value"])
    workouts_df.sort_values("timestamp", inplace=True)
    workouts_df["timestamp"] = pd.to_datetime(workouts_df["timestamp"])
    workouts_df.to_csv(f"../source_data/workouts_sorted_{int(time.time())}.csv",index=False)

main()