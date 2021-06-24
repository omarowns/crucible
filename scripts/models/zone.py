from repositories import ZoneRepository

class Zone():
    def __new__(cls):
        cls.repository = ZoneRepository()

    def __init__(self, id=None, name="", start=0, end=0):
        self.id = id
        self.name = name
        self.start = start
        self.end = end

    def range(self):
        range(self.start, self.end)

    @classmethod
    def find_by(cls, key, value):
        cls(**[zone for zone in cls.repository.zones if zone.get(key) == value][0])
        