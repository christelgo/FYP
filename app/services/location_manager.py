import re 
from app.models.outlet import Outlet

POSTAL_RE = re.compile(r"^\d{6}$")

SECTOR_to_ZONE =[
    ((11,13), "West"),
    ((26,27), "West"),
    ((60,64), "West"),
    ((65,68), "West"),
    ((69,71), "West"),
    ((72,73), "West"),
    ((75,76), "West"),
    ((77,78), "West"),

    ((1,6), "Central"),
    ((7,8), "Central"),
    ((9,10), "Central"),
    ((14,16), "Central"),
    ((17,19), "Central"),
    ((20,21), "Central"),
    ((22,23), "Central"),
    ((24,25), "Central"),
    ((28,30), "Central"),
    ((31,33), "Central"),
    ((34,37), "Central"),
    ((38,41), "Central"),
    ((42,45), "Central"),
    ((53,53), "Central"),
    ((55,55), "Central"),
    ((56,57), "Central"),
    ((58,59), "Central"),
    ((79,80), "Central"),

    ((54,54), "East"),
    ((46,48), "East"),
    ((49,52), "East"),
    ((82,82), "East")
]

def zone_from_postal(postal_code: str) -> str | None:

    if not postal_code:
        return None
    
    postal_code = postal_code.strip()

    if not POSTAL_RE.match(postal_code):
        return None
    
    sector = int(postal_code[:2])

    for (lo,hi), zone in SECTOR_to_ZONE:
        if lo<= sector <= hi:
            return zone
    return None

