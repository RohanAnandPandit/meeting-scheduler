class Scheduler:
    '''
    The scheduler class that can be used to find a free slot given people's availability within a desired time window
    '''

    def schedule(desired_window, people, duration):
        '''
        Try and schedule a meeting between the given people for the given duration within the desired window
        :param desired_window: The time window in which we want to find a free slot
        :param people: A list of Person objects
        :param duration: Duration in seconds
        :return: A TimeWindow object representing the earliest slot when everyone is free (None if its no possible)
        '''

        return None