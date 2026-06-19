# All standard competitive swimming events for SCY and LCM
# World records used as lower bound (fastest possible) — times faster than WR are rejected.
# WR times are stored in seconds. Values taken from FINA world records (as of 2024).

EVENTS = [
    "50 Freestyle", "100 Freestyle", "200 Freestyle", "400 Freestyle",
    "800 Freestyle", "1500 Freestyle",
    "50 Backstroke", "100 Backstroke", "200 Backstroke",
    "50 Breaststroke", "100 Breaststroke", "200 Breaststroke",
    "50 Butterfly", "100 Butterfly", "200 Butterfly",
    "100 IM", "200 IM", "400 IM",
]

# World records (seconds). If a submitted time is faster, it's rejected.
# SCY records (short course yards)
SCY_WORLD_RECORDS = {
    "50 Freestyle": 18.35,
    "100 Freestyle": 39.90,
    "200 Freestyle": 89.63,
    "400 Freestyle": 197.05,
    "800 Freestyle": 411.80,
    "1500 Freestyle": 820.03,
    "50 Backstroke": 21.49,
    "100 Backstroke": 43.35,
    "200 Backstroke": 98.06,
    "50 Breaststroke": 24.53,
    "100 Breaststroke": 52.39,
    "200 Breaststroke": 117.40,
    "50 Butterfly": 19.97,
    "100 Butterfly": 43.00,
    "200 Butterfly": 98.48,
    "100 IM": 43.04,
    "200 IM": 98.83,
    "400 IM": 215.42,
}

# LCM records (long course meters / Olympic)
LCM_WORLD_RECORDS = {
    "50 Freestyle": 20.91,
    "100 Freestyle": 46.80,
    "200 Freestyle": 102.00,
    "400 Freestyle": 220.07,
    "800 Freestyle": 449.45,
    "1500 Freestyle": 871.02,
    "50 Backstroke": 24.00,
    "100 Backstroke": 51.85,
    "200 Backstroke": 111.92,
    "50 Breaststroke": 25.95,
    "100 Breaststroke": 57.13,
    "200 Breaststroke": 125.48,
    "50 Butterfly": 22.27,
    "100 Butterfly": 49.45,
    "200 Butterfly": 110.73,
    "100 IM": 54.56,
    "200 IM": 114.00,
    "400 IM": 244.52,
}

# Slowest "reasonable" time per event — reject anything slower than this
# (roughly 3× a typical beginner's time)
MAX_TIMES = {
    "50 Freestyle": 600,
    "100 Freestyle": 1200,
    "200 Freestyle": 2400,
    "400 Freestyle": 4800,
    "800 Freestyle": 9600,
    "1500 Freestyle": 18000,
    "50 Backstroke": 600,
    "100 Backstroke": 1200,
    "200 Backstroke": 2400,
    "50 Breaststroke": 600,
    "100 Breaststroke": 1200,
    "200 Breaststroke": 2400,
    "50 Butterfly": 600,
    "100 Butterfly": 1200,
    "200 Butterfly": 2400,
    "100 IM": 1200,
    "200 IM": 2400,
    "400 IM": 4800,
}

COURSES = ["SCY", "LCM"]

# Relay events: base name → legs in order
RELAY_BASES = [
    "200 Freestyle Relay",
    "400 Freestyle Relay",
    "800 Freestyle Relay",
    "200 Medley Relay",
    "400 Medley Relay",
]

# Leg labels: index → display name (0=leadoff, 3=anchor)
RELAY_LEG_LABELS = ["Leadoff", "Leg 2", "Leg 3", "Anchor"]

# Medley relay legs have stroke labels
MEDLEY_LEG_LABELS = ["Leadoff (Back)", "Leg 2 (Breast)", "Leg 3 (Fly)", "Anchor (Free)"]

def relay_leg_labels(base: str) -> list[str]:
    return MEDLEY_LEG_LABELS if "Medley" in base else RELAY_LEG_LABELS

def relay_event_name(base: str, leg_label: str) -> str:
    return f"{base} - {leg_label}"

# All relay event names flattened (e.g. "400 Freestyle Relay - Leadoff")
RELAY_EVENTS = [
    relay_event_name(base, leg)
    for base in RELAY_BASES
    for leg in relay_leg_labels(base)
]

ALL_EVENTS = EVENTS + RELAY_EVENTS

# World records for relay legs — use corresponding individual stroke WR as lower bound
# Freestyle relay legs
_SCY_RELAY_WR = {
    "200 Freestyle Relay": 18.35,   # 50 free WR
    "400 Freestyle Relay": 39.90,   # 100 free WR
    "800 Freestyle Relay": 89.63,   # 200 free WR
    "200 Medley Relay": 21.49,      # 50 back WR (leadoff/back leg; use min across all strokes)
    "400 Medley Relay": 43.00,      # 100 fly WR (lowest individual 100 WR)
}
_LCM_RELAY_WR = {
    "200 Freestyle Relay": 20.91,
    "400 Freestyle Relay": 46.80,
    "800 Freestyle Relay": 102.00,
    "200 Medley Relay": 22.27,
    "400 Medley Relay": 46.80,
}
_RELAY_MAX = {
    "200 Freestyle Relay": 600,
    "400 Freestyle Relay": 1200,
    "800 Freestyle Relay": 2400,
    "200 Medley Relay": 600,
    "400 Medley Relay": 1200,
}

SCY_WORLD_RECORDS.update({e: _SCY_RELAY_WR[b] for b in RELAY_BASES for e in [relay_event_name(b, l) for l in relay_leg_labels(b)]})
LCM_WORLD_RECORDS.update({e: _LCM_RELAY_WR[b] for b in RELAY_BASES for e in [relay_event_name(b, l) for l in relay_leg_labels(b)]})
MAX_TIMES.update({e: _RELAY_MAX[b] for b in RELAY_BASES for e in [relay_event_name(b, l) for l in relay_leg_labels(b)]})


def validate_time(event: str, course: str, time_seconds: float) -> str | None:
    """Return error string if time is invalid, else None."""
    if event not in ALL_EVENTS:
        return f"Unknown event: {event}"
    if course not in COURSES:
        return f"Invalid course: {course}"
    if time_seconds <= 0:
        return "Time must be positive"

    wr = SCY_WORLD_RECORDS[event] if course == "SCY" else LCM_WORLD_RECORDS[event]
    if time_seconds < wr * 0.98:  # allow 2% margin for rounding
        return f"Time is faster than the world record ({format_time(wr)}). Please enter a valid time."

    max_t = MAX_TIMES[event]
    if time_seconds > max_t:
        return f"Time exceeds maximum allowed ({format_time(max_t)}). Please enter a valid time."

    return None


def format_time(seconds: float) -> str:
    """Convert seconds to MM:SS.mm or SS.mm string."""
    mins = int(seconds // 60)
    secs = seconds % 60
    if mins > 0:
        return f"{mins}:{secs:05.2f}"
    return f"{secs:.2f}"


def parse_time(time_str: str) -> float | None:
    """Parse MM:SS.mm or SS.mm into seconds. Returns None on failure."""
    time_str = time_str.strip()
    try:
        if ":" in time_str:
            parts = time_str.split(":", 1)
            minutes = int(parts[0])
            secs = float(parts[1])
        else:
            minutes = 0
            secs = float(time_str)
        if secs >= 60 or secs < 0 or minutes < 0:
            return None
        return minutes * 60 + secs
    except (ValueError, IndexError):
        return None
