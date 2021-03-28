from plyer import gps


class location:  # Определение геолокации
    def __init__(self, map):
        self.mapview = map
        self.state = False
        self.lat = 0
        self.lon = 0
        self.my_marker = 0

    def set_state_geolocation(self):
        if self.state:  # Если True то получаем местоположение
            self.state = True
        else:
            self.state = False
        return self.state

    def set_lat_lon(self, lat, lon):  # запоминаем местоположение
        self.lat = lat
        self.lon = lon

    def get_lat_lon(self):  # Отдаем местоположение
        return [self.lat, self.lon]