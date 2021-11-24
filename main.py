import pandas as pd
import datetime
import scheduling.time_window as tw
from scheduling.person import Person
from scheduling.scheduler import Scheduler


def convert_to_datetime(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d-%H:%M:%S')


def get_time_window(s):
    [start_str, end_str] = s.replace(' ', '').split('to')
    start = convert_to_datetime(start_str)
    end = convert_to_datetime(end_str)
    return tw.TimeWindow(start, end)


def load_people():
    df = pd.read_csv('calendar.csv')
    df.head()
    windows = {}
    for index, (person, start, end) in df.iterrows():
        if person not in windows:
            windows[person] = []

        windows[person].append(tw.TimeWindow(convert_to_datetime(start), convert_to_datetime(end)))

    people = []
    for person in windows:
        people.append(Person(windows[person]))

    return people


if __name__ == "__main__":
    people = load_people()

    while True:
        desired_window = get_time_window(input('Please enter time window to search in:\n'))
        duration = int(input('Please enter the desired meeting min_duration (in seconds):\n'))
        meeting_window = Scheduler.schedule(desired_window, people, duration)

        if meeting_window:
            print('The following slot is available...')
            print(meeting_window)
        else:
            print('There is no slot available')