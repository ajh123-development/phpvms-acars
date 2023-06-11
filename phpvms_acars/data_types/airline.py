class Airline:
    def __init__(self, data):
        self.id = data['id']
        self.icao = data['icao']
        self.iata = data['iata']
        self.name = data['name']
        self.country = data['country']
        self.logo = data['logo']
