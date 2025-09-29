import datetime
import random
import time


def generate_row(date_low_b, date_up_b, val_low_b, val_up_b):
    start_ts = int(date_low_b.timestamp())
    end_ts = int(date_up_b.timestamp())

    rand_ts = random.randint(start_ts, end_ts)
    val_current = random.uniform(val_low_b, val_up_b)

    return val_current, datetime.datetime.fromtimestamp(rand_ts)


def main():
    start_date = datetime.datetime(2022, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
    filename = f"workouts_one_user_raw_{int(time.time())}.csv"
    with open(filename, "wt", 1) as source_file:
        for _ in range(50):
            value, date = generate_row(start_date, end_date, 0.0, 100.0)
            print(f"{date},{value:.2f}")
            source_file.write(f"{date},{value:.2f}\n")
    source_file.close()


main()
