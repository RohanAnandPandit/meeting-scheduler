class TimeWindow:
    '''
    Represents a window of time with a start and end point
    '''

    def __init__(self, start, end):
        self.start = start
        self.end = end

    # The start datetime
    start = None

    # The end datetime
    end = None

    def __str__(self):
        return f'{self.start}==>{self.end}'

    def __repr__(self):
        return self.__str__()
