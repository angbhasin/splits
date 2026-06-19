"""
Curated list of notable real-world swim performances.
Update this file when new world records or major meet results come in.
Times are stored in seconds; time_str is the display format.
"""

FEATURED_SWIMS = [
    # ── LCM (Long Course Meters) ──────────────────────────────────────────────
    {"swimmer_name": "Pan Zhanle",        "event": "100 Freestyle",    "course": "LCM", "time_seconds": 46.40,  "time_str": "46.40",    "meet": "Paris Olympics",       "year": 2024},
    {"swimmer_name": "Leon Marchand",     "event": "400 IM",           "course": "LCM", "time_seconds": 242.50, "time_str": "4:02.50",  "meet": "Paris Olympics",       "year": 2024},
    {"swimmer_name": "Leon Marchand",     "event": "200 Breaststroke", "course": "LCM", "time_seconds": 125.85, "time_str": "2:05.85",  "meet": "Paris Olympics",       "year": 2024},
    {"swimmer_name": "Leon Marchand",     "event": "200 Butterfly",    "course": "LCM", "time_seconds": 112.56, "time_str": "1:52.56",  "meet": "Paris Olympics",       "year": 2024},
    {"swimmer_name": "Leon Marchand",     "event": "200 IM",           "course": "LCM", "time_seconds": 114.59, "time_str": "1:54.59",  "meet": "Paris Olympics",       "year": 2024},
    {"swimmer_name": "Kristóf Milák",     "event": "200 Butterfly",    "course": "LCM", "time_seconds": 110.34, "time_str": "1:50.34",  "meet": "World Championships",  "year": 2022},
    {"swimmer_name": "David Popovici",    "event": "100 Freestyle",    "course": "LCM", "time_seconds": 46.86,  "time_str": "46.86",    "meet": "World Championships",  "year": 2022},
    {"swimmer_name": "Thomas Ceccon",     "event": "100 Backstroke",   "course": "LCM", "time_seconds": 51.60,  "time_str": "51.60",    "meet": "World Championships",  "year": 2022},
    {"swimmer_name": "Caeleb Dressel",    "event": "100 Butterfly",    "course": "LCM", "time_seconds": 49.45,  "time_str": "49.45",    "meet": "Tokyo Olympics",       "year": 2021},
    {"swimmer_name": "Caeleb Dressel",    "event": "50 Freestyle",     "course": "LCM", "time_seconds": 21.07,  "time_str": "21.07",    "meet": "Tokyo Olympics",       "year": 2021},
    {"swimmer_name": "Kaylee McKeown",    "event": "100 Backstroke",   "course": "LCM", "time_seconds": 57.33,  "time_str": "57.33",    "meet": "Tokyo Olympics",       "year": 2021},
    {"swimmer_name": "Kaylee McKeown",    "event": "200 Backstroke",   "course": "LCM", "time_seconds": 123.14, "time_str": "2:03.14",  "meet": "Tokyo Olympics",       "year": 2021},
    {"swimmer_name": "Adam Peaty",        "event": "100 Breaststroke", "course": "LCM", "time_seconds": 57.13,  "time_str": "57.13",    "meet": "World Championships",  "year": 2019},
    {"swimmer_name": "Katie Ledecky",     "event": "1500 Freestyle",   "course": "LCM", "time_seconds": 920.48, "time_str": "15:20.48", "meet": "Pro Swim Series",      "year": 2018},
    {"swimmer_name": "Sarah Sjöström",    "event": "50 Freestyle",     "course": "LCM", "time_seconds": 23.61,  "time_str": "23.61",    "meet": "World Championships",  "year": 2017},
    {"swimmer_name": "Lilly King",        "event": "100 Breaststroke", "course": "LCM", "time_seconds": 64.13,  "time_str": "1:04.13",  "meet": "World Championships",  "year": 2017},
    {"swimmer_name": "Katie Ledecky",     "event": "800 Freestyle",    "course": "LCM", "time_seconds": 484.79, "time_str": "8:04.79",  "meet": "Rio Olympics",         "year": 2016},
    {"swimmer_name": "Katie Ledecky",     "event": "400 Freestyle",    "course": "LCM", "time_seconds": 236.46, "time_str": "3:56.46",  "meet": "Rio Olympics",         "year": 2016},
    {"swimmer_name": "Katinka Hosszu",    "event": "400 IM",           "course": "LCM", "time_seconds": 266.36, "time_str": "4:26.36",  "meet": "Rio Olympics",         "year": 2016},
    {"swimmer_name": "Florent Manaudou",  "event": "50 Freestyle",     "course": "LCM", "time_seconds": 20.91,  "time_str": "20.91",    "meet": "World Championships",  "year": 2014},

    # ── SCY (Short Course Yards) ──────────────────────────────────────────────
    {"swimmer_name": "Caeleb Dressel",    "event": "50 Freestyle",     "course": "SCY", "time_seconds": 18.35,  "time_str": "18.35",    "meet": "NCAA Championships",   "year": 2018},
    {"swimmer_name": "Caeleb Dressel",    "event": "100 Freestyle",    "course": "SCY", "time_seconds": 39.90,  "time_str": "39.90",    "meet": "NCAA Championships",   "year": 2018},
    {"swimmer_name": "Caeleb Dressel",    "event": "100 Butterfly",    "course": "SCY", "time_seconds": 43.00,  "time_str": "43.00",    "meet": "NCAA Championships",   "year": 2018},
    {"swimmer_name": "Ryan Murphy",       "event": "100 Backstroke",   "course": "SCY", "time_seconds": 43.35,  "time_str": "43.35",    "meet": "NCAA Championships",   "year": 2016},
    {"swimmer_name": "Ryan Murphy",       "event": "200 Backstroke",   "course": "SCY", "time_seconds": 98.06,  "time_str": "1:38.06",  "meet": "NCAA Championships",   "year": 2016},
    {"swimmer_name": "Adam Peaty",        "event": "100 Breaststroke", "course": "SCY", "time_seconds": 52.39,  "time_str": "52.39",    "meet": "World Cup",            "year": 2019},
    {"swimmer_name": "Lilly King",        "event": "100 Breaststroke", "course": "SCY", "time_seconds": 55.73,  "time_str": "55.73",    "meet": "NCAA Championships",   "year": 2017},
    {"swimmer_name": "Kathleen Baker",    "event": "100 Backstroke",   "course": "SCY", "time_seconds": 49.15,  "time_str": "49.15",    "meet": "NCAA Championships",   "year": 2018},
    {"swimmer_name": "Katie Ledecky",     "event": "400 Freestyle",    "course": "SCY", "time_seconds": 212.34, "time_str": "3:32.34",  "meet": "Pro Swim Series",      "year": 2017},
    {"swimmer_name": "Ryan Lochte",       "event": "200 IM",           "course": "SCY", "time_seconds": 98.83,  "time_str": "1:38.83",  "meet": "NCAA Championships",   "year": 2010},
]
