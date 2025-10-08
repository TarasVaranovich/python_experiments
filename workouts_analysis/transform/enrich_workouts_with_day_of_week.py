import time

import pandas as pd

from workouts_analysis import WORKOUT_STATS_SORTED, WORKOUTS_DIR


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_SORTED)
    workouts_df["day_of_week"] = pd.to_datetime(workouts_df["timestamp"]).dt.day_name()
    workouts_df.to_csv(WORKOUTS_DIR + f"workouts_day_of_week_{int(time.time())}.csv", index=False)

main()
