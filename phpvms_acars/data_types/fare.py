class Fare:
    def __init__(self, data):
        self.id = data['id']
        self.code = data['code']
        self.name = data['name']
        self.capacity = data['capacity']
        self.cost = data['cost']
        self.count = data['count']
        self.price = data['price']
        self.type = data['type']
        self.notes = data['notes']
        self.active = data['active']
