class Person:
    """
    Represents a single person
    """

    def __init__(self, windows=None):
        if windows is None:
            windows = []
        self.busy_windows = sorted(windows, key=lambda window: window.get_start())

    def free_windows(self, desired_window, min_duration):
        """
        List of person's free time slots in the desired window having required duration
        :param desired_window: The time window in which we want to find a free slot
        :param people: A list of Person objects
        :param duration: Duration in seconds
        :return: list of TimeWindow objects
        """
        windows = []
        if self.busy_windows:
            first = self.busy_windows[0]
            last = self.busy_windows[-1]
            if desired_window.starts_before(first):
                tw = desired_window.gap_before(first).merge(desired_window)
                if tw.get_duration() >= min_duration:
                    windows.append(tw)

            if last.ends_before(desired_window):
                tw = desired_window.gap_after(last).merge(desired_window)
                if tw.get_duration() >= min_duration:
                    windows.append(tw)

        for i in range(1, len(self.busy_windows)):
            curr = self.busy_windows[i]
            prev = self.busy_windows[i - 1]

            if prev.get_start() > desired_window.get_end():
                break

            tw = prev.gap_between(curr).merge(desired_window)
            if tw.get_duration() >= min_duration:
                windows.append(tw)

        return windows
