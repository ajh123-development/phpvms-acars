from typing import List
from .link import Link
from .meta import Meta
from .pirep_item import PirepItem

class PirepData:
    def __init__(self, data):
        self.data: List[PirepItem] = [PirepItem(item) for item in data['data']]
        self.links = Link(data['links'])
        self.meta = Meta(data['meta'])
