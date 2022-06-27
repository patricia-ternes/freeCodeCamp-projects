# Solution by Patricia Ternes <patricia.terdal@gmail.com>
# https://github.com/patricia-ternes/freeCodeCamp-projects/blob/main/ScientificComputingPython/TimeCalculator/time_calculator.py


def add_time(start, duration, day=False):
    days = 0

    # Transform inputs in lists
    start = (start.replace(":", " ")).split(" ")
    duration = duration.split(":")

    # Convert to 24h system
    if start[2] == "PM":
        start[0] = int(start[0]) + 12

    # Add the duration time to the start time
    hours = int(start[0]) + int(duration[0])
    minutes = int(start[1]) + int(duration[1])

    # Convert minutes to 60 minutes system
    hours += minutes // 60
    minutes = minutes % 60

    # Convert hours to 24 system
    days = hours // 24
    hours %= 24

    # Convert to AM/PM system
    meridiem = "AM"
    if hours == 0:
        hours = 12
    elif hours == 12:
        meridiem = "PM"
    elif hours > 12:
        meridiem = "PM"
        hours -= 12

    # Print Formatting
    ## Time in the 12-hour clock format (ending in AM or PM)
    new_time = " ".join([":".join([str(hours), str(minutes).rjust(2, "0")]), meridiem])

    ## The output should display the day of the week of the result.
    if day:
        weekday = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        N = weekday.index(day.capitalize())
        day = weekday[(N + days) % 7]
        new_time = ", ".join([new_time, day])

    ## If the result will be the next day, it should show (next day) after the time.
    if days == 1:
        new_time = " ".join([new_time, "(next day)"])
    ## If the result will be more than one day later, it should show (n days later) after the time
    elif days > 1:
        new_time = " ".join([new_time, "(%d days later)" % days])

    return new_time
