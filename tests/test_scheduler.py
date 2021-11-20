import datetime as dtm
import scheduling.time_window as twd
import scheduling.person as psn
import scheduling.scheduler as sch

def test_try_schedule_a_meeting_in_this_millenium():

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
    assert meeting_window is not None

def test_try_schedule_impossible_meeting():

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

def test_try_schedule_60_min_meeting():

    # Arrange
    desired_window = twd.TimeWindow(
        dtm.datetime(2021, 11, 19, 8, 0, 0),
        dtm.datetime(2021, 11, 19, 18, 0, 0),
    )

    people = [
        psn.Person([
            twd.TimeWindow(
                dtm.datetime(2021, 11, 19, 9, 30, 0),
                dtm.datetime(2021, 11, 19, 10, 0, 0)),
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
    assert meeting_window is not None

def test_try_schedule_30_min_meeting():

    # Arrange
    desired_window = twd.TimeWindow(
        dtm.datetime(2021, 11, 19, 8, 0, 0),
        dtm.datetime(2021, 11, 19, 18, 0, 0),
    )

    people = [
        psn.Person([
            twd.TimeWindow(
                dtm.datetime(2021, 11, 19, 9, 30, 0),
                dtm.datetime(2021, 11, 19, 10, 0, 0)),
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
    meeting_window = sch.Scheduler.schedule(desired_window, people, 1800)

    # Assert
    assert meeting_window is not None
