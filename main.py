from datetime import datetime, date, timedelta
import random
import csv


def choose_rover(choose_from: dict) -> str:
    return min(choose_from, key=choose_from.get)


def shuffle_dict(to_shuffle: dict) -> dict:
    b = list(to_shuffle.items())
    random.shuffle(b)
    return dict(b)


def increment_count(rover: dict[str, int], key: str) -> dict:
    rover[key] += 1
    return rover


def get_next_meeting(from_date: date):
    meeting = 0
    if from_date.weekday() == 6 or from_date.weekday() < 2:
        meeting = 2
    else:
        meeting = 6

    ahead = meeting - from_date.weekday()
    if ahead <= 0:
        ahead += 7

    return from_date + timedelta(ahead)


def pair_rovers(r: dict[str, int], count: int, meeting_date: date) -> list[list]:
    pairs = []
    for _ in range(count):
        temp = []
        meeting_date = get_next_meeting(meeting_date)
        temp.append(meeting_date.strftime("%B %d, %Y"))
        for _ in range(2):
            r = shuffle_dict(r)
            rover = choose_rover(r)
            r = increment_count(r, rover)

            temp.append(rover)

        pairs.append(temp)
    print(r)
    return pairs


def write_to_csv(filename: str, r: list):
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Date", "", ""])
        csvwriter.writerows(r)


if __name__ == "__main__":
    roverr = input("Please enter the name of the rovers separated by a comma (,): ")
    sets = int(
        input(
            "How many set of schedules would you want? (A set is the number of meetings it would take to fit all the rovers in. Typically equal to the number of rovers): "
        )
    )
    day = int(input("From what day? "))
    month = int(input("What month? "))
    year = int(input("What year? "))
    from_date = date(year, month, day)
    rovers = roverr.title().split(",")
    rovers_dict = {k: 0 for k in rovers}
    pairs = pair_rovers(rovers_dict, len(rovers) * sets, from_date)
    write_to_csv("sample.csv", pairs)
