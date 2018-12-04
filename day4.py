"""Day 4: Repose Record

https://adventofcode.com/2018/day/4
"""

import re
from collections import namedtuple
from typing import Dict, List

from questions import day4 as question

LogEntry = namedtuple("LogEntry", "year month day hour minute message")
pattern = r"\[(\d+?)-(\d+?)-(\d+?) (\d+?):(\d+?)\] (.+)"
parsed_logs = []

for line in question.strip().splitlines():
    match = re.match(pattern, line)
    assert match is not None
    attrs = (int(m) if m.isdigit() else m for m in match.groups())
    parsed_logs.append(LogEntry(*attrs))

parsed_logs.sort(key=lambda e: (e.year, e.month, e.day, e.hour, e.minute))

sleep_times: Dict[int, List[int]] = {}
last_guard_id = None
last_asleep = None  # in minutes

for log in parsed_logs:
    if "begins shift" in log.message:
        match = re.search(r"\d+", log.message)
        assert match is not None
        last_guard_id = int(match.group(0))
        if last_guard_id not in sleep_times:
            sleep_times[last_guard_id] = []

    elif log.message == "falls asleep":
        last_asleep = log.minute

    elif log.message == "wakes up":
        assert last_guard_id is not None and last_asleep is not None
        sleep_times[last_guard_id].extend(
            list(range(last_asleep, log.minute)))


def part1() -> int:
    """Find the guard that has the most minutes asleep.
    What minute does that guard spend asleep the most?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    longest_sleeper = max(sleep_times, key=lambda g: len(sleep_times[g]))
    sleepiest_minute = max(
        sleep_times[longest_sleeper], key=sleep_times[longest_sleeper].count)

    return longest_sleeper * sleepiest_minute


def part2() -> int:
    """Of all guards, which guard is most frequently asleep on the same minute?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    sleepiest_minute = None
    sleeping_guard = None
    sleep_frequency = 0

    for guard, times in sleep_times.items():
        if len(times) == 0:
            continue
        _sleepiest_minute = max(
            sleep_times[guard], key=sleep_times[guard].count)
        _sleep_frequency = sleep_times[guard].count(_sleepiest_minute)

        if _sleep_frequency > sleep_frequency:
            sleepiest_minute = _sleepiest_minute
            sleeping_guard = guard
            sleep_frequency = _sleep_frequency

    assert sleeping_guard is not None and sleepiest_minute is not None
    return sleeping_guard * sleepiest_minute


print("Day 4, part 1 answer:", part1())
print("Day 4, part 2 answer:", part2())
