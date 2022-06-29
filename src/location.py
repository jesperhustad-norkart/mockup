from dataclasses import dataclass

@dataclass
class Location:
    uuid: str
    lat: float
    lon: float