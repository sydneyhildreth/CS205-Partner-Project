
class Trail:
    def __init__(self, name, location, elevation, rank):
        self.name = name
        self.location = location
        self.elevation = elevation
        self.rank = rank

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getElevation(self):
        return self.elevation

    def get_rank(self):
        return self.rank

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_elevation(self, elevation):
        self.elevation = elevation

    def set_rank(self, rank):
        self.rank = rank
