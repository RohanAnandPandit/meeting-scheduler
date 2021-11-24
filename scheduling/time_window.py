class TimeWindow:
    """
    Represents a window of time with a start and end point
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_duration(self):
        return (self.end - self.start).total_seconds()

    def starts_before(self, time_window):
        return self.start < time_window.get_start()

    def starts_after(self, time_window):
        return not self.starts_before(time_window)

    def ends_before(self, time_window):
        return self.end < time_window.get_end()

    def ends_after(self, time_window):
        return not self.ends_before(time_window)

    def gap_before(self, time_window):
        return TimeWindow(self.start, time_window.get_start())

    def gap_after(self, time_window):
        return TimeWindow(time_window.get_end(), self.end)

    def gap_between(self, time_window):
        return TimeWindow(self.end, time_window.get_start())

    def merge(self, time_window):
        """
        Find the overlapping time window
        :param time_window: TimeWindow object to merge with
        :return: TimeWindow object
        """
        start = max(self.start, time_window.get_start())
        end = min(self.end, time_window.get_end())
        return TimeWindow(start, end)

    def __str__(self):
        return f'{self.start}==>{self.end}'

    def __repr__(self):
        return self.__str__()
