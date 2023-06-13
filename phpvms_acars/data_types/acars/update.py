from typing import Dict

class AcarsUpdate:
    def __init__(self, flight_time: int, distance: int, status: str, fields: Dict[str, str] = {}):
        self.flight_time = flight_time
        self.distance = distance
        self.status = status
        self.fields = fields
