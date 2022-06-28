from dataclasses import dataclass

@dataclass
class Point:
    id: str
    value: float
    seriesName: str
    komtekLocationReferenceId: str
    resolution: str
    unit: str
    timestamp: str

    def toRow(self):
        return [
            self.id, 
            self.value, 
            self.seriesName, 
            self.komtekLocationReferenceId, 
            self.resolution, 
            self.unit, 
            self.timestamp
        ]

    def getDefault():
        return Point(
            id="",
            seriesName="77db43ae-fb4d-4481-bc18-fff1d5aaf87b",
            resolution="P7D",
            value=None, komtekLocationReferenceId=None, unit=None, timestamp=None
            )