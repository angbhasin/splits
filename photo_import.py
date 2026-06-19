"""
Extract swim times from a photo using Claude vision API.
Returns a list of dicts: {swimmer_name, event, course, time_seconds, time_str}
"""
import base64
import json
import os
import anthropic
from events import EVENTS, parse_time, validate_time, format_time
from swimcloud_import import EVENT_ALIASES, COURSE_ALIASES

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

EVENTS_LIST = "\n".join(f"- {e}" for e in EVENTS)

PROMPT = f"""You are analyzing a photo of a swim meet results sheet or hand-written times list.

Extract every swimmer name and their swim times from the image. For each time found, identify:
1. The swimmer's name
2. The swimming event (stroke and distance)
3. The course: SCY (short course yards) or LCM (long course meters)
4. The time in MM:SS.mm or SS.mm format

Valid events are ONLY:
{EVENTS_LIST}

Return a JSON array. Each element must be an object with these exact keys:
- "swimmer_name": string
- "event": string (must match one of the valid events above exactly)
- "course": string (either "SCY" or "LCM")
- "time": string (e.g. "54.32" or "1:54.32")

If the course is unclear from context, use "SCY" as the default.
If you cannot determine the event, skip that entry.
Return ONLY the JSON array, nothing else. Example:
[{{"swimmer_name": "John Smith", "event": "100 Freestyle", "course": "SCY", "time": "47.23"}}]
"""


def extract_times_from_image(image_bytes: bytes, media_type: str) -> tuple[list[dict], list[str]]:
    """Call Claude vision to extract swim times from an image."""
    b64 = base64.standard_b64encode(image_bytes).decode("utf-8")

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": b64,
                    },
                },
                {"type": "text", "text": PROMPT},
            ],
        }],
    )

    raw = response.content[0].text.strip()

    # Strip markdown code fences if Claude wrapped the JSON
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        entries = json.loads(raw)
    except json.JSONDecodeError:
        return [], [f"Could not parse Claude's response: {raw[:200]}"]

    results = []
    errors = []

    for entry in entries:
        swimmer_name = entry.get("swimmer_name", "").strip()
        event_raw = entry.get("event", "").strip()
        course_raw = entry.get("course", "").strip().upper()
        time_str = entry.get("time", "").strip()

        if not swimmer_name or not event_raw or not time_str:
            continue

        # Normalize event
        if event_raw in EVENTS:
            event = event_raw
        else:
            event = EVENT_ALIASES.get(event_raw.lower())
        if not event:
            errors.append(f"Unknown event '{event_raw}' for {swimmer_name} — skipped")
            continue

        # Normalize course
        course = course_raw if course_raw in ("SCY", "LCM") else COURSE_ALIASES.get(course_raw.lower())
        if not course:
            course = "SCY"

        time_sec = parse_time(time_str)
        if time_sec is None:
            errors.append(f"Invalid time '{time_str}' for {swimmer_name} {event} — skipped")
            continue

        err = validate_time(event, course, time_sec)
        if err:
            errors.append(f"{swimmer_name} {course} {event} {time_str}: {err}")
            continue

        results.append({
            "swimmer_name": swimmer_name,
            "event": event,
            "course": course,
            "time_seconds": time_sec,
            "time_str": format_time(time_sec),
        })

    if not results and not errors:
        errors.append("No swim times could be found in the image.")

    return results, errors
