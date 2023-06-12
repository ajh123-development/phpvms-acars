from typing import List
from .fare import Fare
from .aircraft import Aircraft

class Subfleet:
    def __init__(self, data):
        self.id = data['id']
        self.airline_id = data['airline_id']
        self.hub_id = data['hub_id']
        self.type = data['type']
        self.simbrief_type = data['simbrief_type']
        self.name = data['name']
        self.cost_block_hour = data['cost_block_hour']
        self.cost_delay_minute = data['cost_delay_minute']
        self.fuel_type = data['fuel_type']
        self.ground_handling_multiplier = data['ground_handling_multiplier']
        self.cargo_capacity = data['cargo_capacity']
        self.fuel_capacity = data['fuel_capacity']
        self.gross_weight = data['gross_weight']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fares: List[Fare] = [Fare(fare) for fare in data['fares']]
        self.aircraft: List[Aircraft] = [Aircraft(aircraft) for aircraft in data['aircraft']]
