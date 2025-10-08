import pandas as pd
from pandas import CategoricalDtype

from workouts_analysis import WORKOUT_STATS_DAY_OF_WEEK


def main():
    days_of_week_cats= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_of_week_type = CategoricalDtype(categories=days_of_week_cats, ordered=True)
    workouts_df = pd.read_csv(WORKOUT_STATS_DAY_OF_WEEK)
    mean_for_day = workouts_df.groupby("day_of_week")["value"].mean().reset_index(name="avg")
    mean_for_day["day_of_week"] = mean_for_day["day_of_week"].astype(days_of_week_type)
    mean_for_day.sort_values("day_of_week", ascending=True, inplace=True)
    print(mean_for_day)


main()