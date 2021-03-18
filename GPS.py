try:
    from plyer import gps
    from kivy.utils import platform
    from kivy_garden.mapview import MapMarker

    class location:
        def __init__(self, map):
            self.mapview = map
            self.state = 0
            self.lat = 0
            self.lon = 0
            self.my_marker = 0

        def set_state_geolocation(self):
            if self.state == 0:
                self.state = True
            else:
                self.state = False
            return self.state

        def set_lat_lon(self, lat, lon):
            self.lat = lat
            self.lon = lon

        def get_lat_lon(self):
            return [self.lat, self.lon]

except Exception as e:
    print(e)