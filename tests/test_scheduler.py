import datetime as dtm
import unittest
import scheduling.time_window as twd
import scheduling.person as psn
import scheduling.scheduler as sch


class TestScheduler(unittest.TestCase):
    def test_try_schedule_a_meeting_in_this_millenium(self):
        # Arrange
        desired_window = twd.TimeWindow(
            dtm.datetime(14, 11, 19, 8, 0, 0),
            dtm.datetime(2050, 9, 12, 18, 0, 0),
        )

        people = [
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(14, 11, 19, 8, 0, 0),
                    dtm.datetime(2021, 11, 19, 10, 15, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 10, 15, 0),
                    dtm.datetime(2021, 11, 19, 10, 45, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 12, 0, 0),
                    dtm.datetime(2021, 11, 19, 12, 30, 0))
            ]),
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 9, 30, 0),
                    dtm.datetime(2021, 11, 19, 10, 0, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 17, 0, 0),
                    dtm.datetime(2021, 11, 19, 17, 30, 0))
            ])
        ]

        # Act
        meeting_window = sch.Scheduler.schedule(desired_window, people, 3600)

        # Assert
        start = '2021-11-19 10:45:00'
        end = '2021-11-19 11:45:00'
        assert str(meeting_window) == f'{start}==>{end}'

    def test_try_schedule_impossible_meeting(self):
        # Arrange
        desired_window = twd.TimeWindow(
            dtm.datetime(2021, 11, 19, 8, 0, 0),
            dtm.datetime(2021, 11, 19, 18, 0, 0),
        )

        people = [
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 7, 0, 0),
                    dtm.datetime(2021, 11, 19, 22, 0, 0))
            ]),
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 6, 0, 0),
                    dtm.datetime(2021, 11, 19, 22, 0, 0))
            ])
        ]

        # Act
        meeting_window = sch.Scheduler.schedule(desired_window, people, 1800)

        # Assert
        assert meeting_window is None

    def test_try_schedule_60_min_meeting(self):
        # Arrange
        desired_window = twd.TimeWindow(
            dtm.datetime(2021, 11, 19, 8, 0, 0),
            dtm.datetime(2021, 11, 19, 18, 0, 0),
        )

        people = [
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 7, 30, 0),
                    dtm.datetime(2021, 11, 19, 10, 0, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 10, 15, 0),
                    dtm.datetime(2021, 11, 19, 12, 30, 0))
            ]),
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 7, 30, 0),
                    dtm.datetime(2021, 11, 19, 10, 0, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 17, 0, 0),
                    dtm.datetime(2021, 11, 19, 17, 30, 0))
            ])
        ]

        # Act
        meeting_window = sch.Scheduler.schedule(desired_window, people, 3600)
        start = '2021-11-19 12:30:00'
        end = '2021-11-19 13:30:00'

        assert str(meeting_window) == f'{start}==>{end}'

    def test_try_schedule_30_min_meeting(self):
        # Arrange
        desired_window = twd.TimeWindow(
            dtm.datetime(2021, 11, 19, 10, 0, 0),
            dtm.datetime(2021, 11, 19, 18, 0, 0),
        )

        people = [
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 9, 30, 0),
                    dtm.datetime(2021, 11, 19, 10, 0, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 10, 15, 0),
                    dtm.datetime(2021, 11, 19, 11, 45, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 12, 0, 0),
                    dtm.datetime(2021, 11, 19, 12, 30, 0))
            ]),
            psn.Person([
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 12, 30, 0),
                    dtm.datetime(2021, 11, 19, 17, 0, 0)),
                twd.TimeWindow(
                    dtm.datetime(2021, 11, 19, 17, 0, 0),
                    dtm.datetime(2021, 11, 19, 17, 30, 0))
            ])
        ]

        # Act
        meeting_window = sch.Scheduler.schedule(desired_window, people, 1800)

        start = '2021-11-19 17:30:00'
        end = '2021-11-19 18:00:00'
        # Assert
        assert str(meeting_window) == f'{start}==>{end}'
