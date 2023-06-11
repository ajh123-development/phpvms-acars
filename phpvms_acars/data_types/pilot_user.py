from .airline import Airline
from .bid import Bid
from .rank import Rank

class PilotUser:
    def __init__(self, data):
        self.id = data['data']['id']
        self.pilot_id = data['data']['pilot_id']
        self.ident = data['data']['ident']
        self.name = data['data']['name']
        self.name_private = data['data']['name_private']
        self.avatar = data['data']['avatar']
        self.rank_id = data['data']['rank_id']
        self.home_airport = data['data']['home_airport']
        self.curr_airport = data['data']['curr_airport']
        self.last_pirep_id = data['data']['last_pirep_id']
        self.flights = data['data']['flights']
        self.flight_time = data['data']['flight_time']
        self.transfer_time = data['data']['transfer_time']
        self.timezone = data['data']['timezone']
        self.state = data['data']['state']
        self.airline = Airline(data['data']['airline'])
        self.bids = [Bid(bid) for bid in data['data']['bids']]
        self.rank = Rank(data['data']['rank'])
