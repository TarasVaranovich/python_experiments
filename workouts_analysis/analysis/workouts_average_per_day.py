import pandas as pd

from workouts_analysis import WORKOUT_STATS_DAY_OF_WEEK


def main():
    workouts_df = pd.read_csv(WORKOUT_STATS_DAY_OF_WEEK)
    mean_for_day = workouts_df.groupby("day_of_week")["value"].mean().reset_index(name="avg")
    mean_for_day.sort_values("avg", ascending=False, inplace=True)
    print(mean_for_day)


main()
