class Bid:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.flight_id = data['flight_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
