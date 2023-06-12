from .airline import Airline
from .airport import Airport
from .distance import Distance
from .fuel import Fuel

class PirepItem:
    def __init__(self, item):
        self.id = item['id']
        self.user_id = item['user_id']
        self.airline_id = item['airline_id']
        self.aircraft_id = item['aircraft_id']
        self.event_id = item['event_id']
        self.flight_id = item['flight_id']
        self.flight_number = item['flight_number']
        self.route_code = item['route_code']
        self.route_leg = item['route_leg']
        self.flight_type = item['flight_type']
        self.dpt_airport_id = item['dpt_airport_id']
        self.arr_airport_id = item['arr_airport_id']
        self.alt_airport_id = item['alt_airport_id']
        self.level = item['level']
        self.distance = Distance(item['distance'])
        self.planned_distance = Distance(item['planned_distance'])
        self.flight_time = item['flight_time']
        self.planned_flight_time = item['planned_flight_time']
        self.zfw = item['zfw']
        self.block_fuel = Fuel(item['block_fuel'])
        self.fuel_used = Fuel(item['fuel_used'])
        self.landing_rate = item['landing_rate']
        self.score = item['score']
        self.route = item['route']
        self.notes = item['notes']
        self.source = item['source']
        self.source_name = item['source_name']
        self.state = item['state']
        self.status = item['status']
        self.submitted_at = item['submitted_at']
        self.block_off_time = item['block_off_time']
        self.block_on_time = item['block_on_time']
        self.created_at = item['created_at']
        self.updated_at = item['updated_at']
        self.ident = item['ident']
        self.phase = item['phase']
        self.status_text = item['status_text']
        self.airline = Airline(item['airline'])
        self.dpt_airport = Airport(item['dpt_airport'])
        self.arr_airport = Airport(item['arr_airport'])
        self.fields = item['fields']
