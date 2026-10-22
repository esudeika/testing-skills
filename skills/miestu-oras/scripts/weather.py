#!/usr/bin/env python3
"""Five largest Lithuanian cities' nearest forecast from official Meteo.lt API."""

import json
import math
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


CITIES = (
    ("Vilnius", "vilnius"),
    ("Kaunas", "kaunas"),
    ("Klaipėda", "klaipeda"),
    ("Šiauliai", "siauliai"),
    ("Panevėžys", "panevezys"),
)

CONDITIONS = {
    "clear": "Giedra",
    "partly-cloudy": "Mažai debesuota",
    "variable-cloudiness": "Nepastoviai debesuota",
    "cloudy-with-sunny-intervals": "Debesuota su pragiedruliais",
    "cloudy": "Debesuota",
    "rain-showers": "Trumpas lietus",
    "light-rain-at-times": "Protarpiais nedidelis lietus",
    "rain-at-times": "Protarpiais lietus",
    "light-rain": "Nedidelis lietus",
    "rain": "Lietus",
    "heavy-rain": "Smarkus lietus",
    "thunder": "Perkūnija",
    "isolated-thunderstorms": "Trumpas lietus su perkūnija",
    "thunderstorms": "Lietus su perkūnija",
    "heavy-rain-with-thunderstorms": "Smarkus lietus su perkūnija",
    "sleet-showers": "Trumpa šlapdriba",
    "sleet-at-times": "Protarpiais šlapdriba",
    "light-sleet": "Nedidelė šlapdriba",
    "sleet": "Šlapdriba",
    "freezing-rain": "Lijundra",
    "hail": "Kruša",
    "snow-showers": "Trumpas sniegas",
    "light-snow-at-times": "Protarpiais nedidelis sniegas",
    "snow-at-times": "Protarpiais sniegas",
    "light-snow": "Nedidelis sniegas",
    "snow": "Sniegas",
    "heavy-snow": "Smarkus sniegas",
    "snowstorm": "Pūga",
    "fog": "Rūkas",
    "squall": "Škvalas",
}


def parse_utc(value):
    """Parse Meteo.lt UTC timestamp with or without T/Z separators."""
    if not isinstance(value, str):
        raise ValueError("Trūksta prognozės laiko")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def nearest_forecast(data, now=None):
    """Return nearest not-in-the-past valid forecast record."""
    now = now or datetime.now(timezone.utc)
    candidates = []
    for item in data.get("forecastTimestamps", []):
        try:
            instant = parse_utc(item.get("forecastTimeUtc"))
            value = item.get("airTemperature")
            if instant >= now and isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value):
                candidates.append((instant, item))
        except (TypeError, ValueError, OverflowError):
            continue
    if not candidates:
        raise ValueError("Nėra galiojančios būsimos prognozės")
    return min(candidates, key=lambda pair: pair[0])


def get_forecast(place_code):
    url = f"https://api.meteo.lt/v1/places/{place_code}/forecasts/long-term"
    request = Request(url, headers={"User-Agent": "miestu-oras/1.0", "Accept": "application/json"})
    with urlopen(request, timeout=12) as response:
        return json.load(response)


def format_temperature(value):
    return f"{value:+.1f} °C".replace(".", ",")


def make_report(fetch=get_forecast, now=None):
    now = now or datetime.now(timezone.utc)
    rows = []
    failures = []
    for city, code in CITIES:
        try:
            timestamp, item = nearest_forecast(fetch(code), now)
            condition_code = item.get("conditionCode")
            condition = CONDITIONS.get(condition_code, "Sąlygos nenustatytos" if condition_code is None else f"Nežinomas kodas: {condition_code}")
            local_time = timestamp.astimezone(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M")
            rows.append(f"| {city} | {format_temperature(item['airTemperature'])} | {condition} | {local_time} |")
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            failures.append(f"{city}: {exc}")
            rows.append(f"| {city} | — | Duomenų gauti nepavyko | — |")

    result = [
        "## Penkių didžiausių Lietuvos miestų orų prognozė",
        "",
        "| Miestas | Oro temperatūra | Sąlygos | Prognozės laikas (Lietuvos) |",
        "|---|---:|---|---|",
        *rows,
        "",
        "Šaltinis: [Lietuvos hidrometeorologijos tarnyba (Meteo.lt)](https://api.meteo.lt/).",
        "Tai artimiausio galimo laiko **prognozė**, ne tiesioginis matavimas.",
    ]
    if failures:
        result.extend(["", "Nepavyko gauti dalies duomenų: " + "; ".join(failures)])
    return "\n".join(result), not failures


if __name__ == "__main__":
    report, all_successful = make_report()
    print(report)
    sys.exit(0 if all_successful else 1)
