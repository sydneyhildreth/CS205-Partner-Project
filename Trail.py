
class Trail:
    def __init__(self, name, location, elevation, rank):
        self._name = name
        self._location = location
        self._elevation = elevation
        self._rank = rank

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_elevation(self):
        return self._elevation

    def get_rank(self):
        return self._rank

    def set_name(self, name):
        self._name = name

    def set_location(self, location):
        self._location = location

    def set_elevation(self, elevation):
        self._elevation = elevation

    def set_rank(self, rank):
        self._rank = rank
