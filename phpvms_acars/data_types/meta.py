class Meta:
    def __init__(self, meta):
        self.current_page = meta['current_page']
        self.from_item = meta['from']
        self.last_page = meta['last_page']
        self.path = meta['path']
        self.per_page = meta['per_page']
        self.to_item = meta['to']
        self.total = meta['total']
        self.prev_page = meta['prev_page']
        self.next_page = meta['next_page']
