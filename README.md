# Meeting Scheduler
This is a skeleton project for a meeting scheduler with failing unit tests

## Task
Your task is to use this is a starting point to create a meeting scheduler

## Requirements
* This needs to be a command line app that can be used to find a meeting window
* The user should be prompted for the desired window and the duration
  * Example:
    ```commandline
    Please enter time window to search in:
    2021-11-19-09:00:00 to 2021-11-19-18:00:00
    Please enter the desired meeting duration (in seconds):
    1800
    The following slot is available...
    ```
* People's availability is in the calendar.csv file (This contains the busy time slots, not the available ones)
* The console app should print the earliest slot when everyone is available (within the search window)
* If a slot isn't available, this should be conveyed to the user

## Technical Considerations
* This is a skeleton project with pre-created classes but feel free to change the structure if you think this is appropriate.
* The first important thing is the algorithm you choose to implement the window search. (Don't use an out of the box library)
* Secondly, its important to add some appropriate unit tests so that you try out several possibilities (Feel free to try out different data in the calendar.csv file)
* Please refrain from using a left to right interval scanning algo (ie. search precision should be infinitesimally small)