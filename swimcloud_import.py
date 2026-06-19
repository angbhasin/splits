"""
Parse swimmer times from text pasted directly from a SwimCloud profile page.
Returns a list of dicts: {event, course, time_seconds, time_str}
"""
import re
from events import EVENTS, parse_time, validate_time, format_time

EVENT_ALIASES = {
    "50 free": "50 Freestyle", "50 freestyle": "50 Freestyle",
    "100 free": "100 Freestyle", "100 freestyle": "100 Freestyle",
    "200 free": "200 Freestyle", "200 freestyle": "200 Freestyle",
    "400 free": "400 Freestyle", "400 freestyle": "400 Freestyle",
    "800 free": "800 Freestyle", "800 freestyle": "800 Freestyle",
    "1000 free": None,  # not in our events
    "1500 free": "1500 Freestyle", "1500 freestyle": "1500 Freestyle",
    "1650 free": None,  # not in our events
    "50 back": "50 Backstroke", "50 backstroke": "50 Backstroke",
    "100 back": "100 Backstroke", "100 backstroke": "100 Backstroke",
    "200 back": "200 Backstroke", "200 backstroke": "200 Backstroke",
    "50 breast": "50 Breaststroke", "50 breaststroke": "50 Breaststroke",
    "100 breast": "100 Breaststroke", "100 breaststroke": "100 Breaststroke",
    "200 breast": "200 Breaststroke", "200 breaststroke": "200 Breaststroke",
    "50 fly": "50 Butterfly", "50 butterfly": "50 Butterfly",
    "100 fly": "100 Butterfly", "100 butterfly": "100 Butterfly",
    "200 fly": "200 Butterfly", "200 butterfly": "200 Butterfly",
    "100 im": "100 IM", "100 i.m.": "100 IM",
    "200 im": "200 IM", "200 i.m.": "200 IM",
    "400 im": "400 IM", "400 i.m.": "400 IM",
}

COURSE_ALIASES = {
    "scy": "SCY", "yards": "SCY", "y": "SCY", "sc yards": "SCY",
    "lcm": "LCM", "meters": "LCM", "m": "LCM", "lc meters": "LCM", "long course": "LCM",
}

TIME_RE = re.compile(r'\b(\d{1,2}:\d{2}\.\d{1,2}|\d{2,3}\.\d{1,2})\b')


def normalize_event(raw: str) -> str | None:
    return EVENT_ALIASES.get(raw.lower().strip())


def normalize_course(raw: str) -> str | None:
    return COURSE_ALIASES.get(raw.lower().strip())


def parse_pasted_text(text: str) -> tuple[list[dict], list[str]]:
    """
    Parse times from text pasted from a SwimCloud profile.
    SwimCloud tables look like (tab or space separated):
      Event       Course    Time    ...
      100 Free    SCY       47.32   ...

    We scan every line for a recognizable (event, course, time) combo.
    """
    results = []
    errors = []
    seen = set()

    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Find all time-like tokens in this line
        times_in_line = TIME_RE.findall(line)
        if not times_in_line:
            continue

        # Try to identify event and course from the line
        line_lower = line.lower()
        event = None
        for alias, canonical in EVENT_ALIASES.items():
            if alias in line_lower and canonical:
                event = canonical
                break
        if not event:
            continue

        course = None
        for alias, canonical in COURSE_ALIASES.items():
            if re.search(r'\b' + re.escape(alias) + r'\b', line_lower):
                course = canonical
                break

        if not course:
            # Try to infer from context — default skip with a warning
            errors.append(f"Skipped '{line[:60]}': could not determine course (SCY/LCM)")
            continue

        # Use the first valid time found in the line
        for time_str in times_in_line:
            time_sec = parse_time(time_str)
            if time_sec is None:
                continue
            err = validate_time(event, course, time_sec)
            if err:
                errors.append(f"Skipped {course} {event} {time_str}: {err}")
                continue
            key = (event, course)
            if key in seen:
                continue  # keep first (best) time only
            seen.add(key)
            results.append({"event": event, "course": course,
                            "time_seconds": time_sec, "time_str": format_time(time_sec)})
            break

    if not results and not errors:
        errors.append("No times found. Make sure you copied the full times table from SwimCloud.")

    return results, errors
