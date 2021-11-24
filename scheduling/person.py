class Person:
    """
    Represents a single person
    """

    def __init__(self, windows=None):
        if windows is None:
            windows = []
        self.busy_windows = sorted(windows, key=lambda window: window.get_start())

    def free_windows(self, desired_window, min_duration):
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
            curr = self.busy_windows[i].merge(desired_window)
            prev = self.busy_windows[i - 1].merge(desired_window)
            if prev.get_start() > desired_window.get_end():
                break
            tw = prev.gap_between(curr)
            if tw.get_duration() >= min_duration:
                windows.append(tw)

        return windows
