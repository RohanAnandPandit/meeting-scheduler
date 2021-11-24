import datetime
from .time_window import TimeWindow


class Scheduler:
    """
    The scheduler class that can be used to find a free slot given people's availability within a desired time window
    """

    @staticmethod
    def schedule(desired_window, people, duration):
        """
        Try and schedule a meeting between the given people for the given min_duration within the desired window
        :param desired_window: The time window in which we want to find a free slot
        :param people: A list of Person objects
        :param duration: Duration in seconds
        :return: A TimeWindow object representing the earliest slot when everyone is free (None if its no possible)
        """
        merged_windows = people[0].free_windows(desired_window, duration)

        for person in people[1:]:
            new_windows = []

            for tw in person.free_windows(desired_window, duration):
                for mtw in merged_windows:
                    new_window = tw.merge(mtw)

                    if new_window.get_duration() >= duration:
                        new_windows.append(new_window)

            if not new_windows:
                return None

            merged_windows = new_windows

        start = min(map(lambda tw: tw.get_start(), merged_windows))

        return TimeWindow(start, start + datetime.timedelta(0, duration))
