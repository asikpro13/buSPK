from android.permissions import Permission, request_permissions
from plyer import gps
from kivy.utils import platform


class location:
    def __init__(self, map):
        self.mapview = map
        request_permissions([Permission.ACCESS_COARSE_LOCATION,
                             Permission.ACCESS_FINE_LOCATION], callback)
        gps.configure(on_location=self.location,
                      on_status=self.on_auth_status)

    def callback(self, permission, results):
        if all([res for res in results]):
            print(';sada')
        else:
            print('ВСЕ ПЛОХО')

    def on_auth_status(self, general, status):
        print(general, status)

    def start(self):
        gps.start(1000, 0)

    def location(self):
        if platform == 'android':
            lat = kwargs['lat']
            lon = kwargs['lon']
            self.my_geolocation_marker = MapMarker(lat=float(lat), lon=float(lon), source="location_me.png")
            self.mapview.add_marker(my_geolocation_marker)
            print(lat, lon)

    def stop(self):
        self.mapview.remove_marker(self.my_geolocation_marker)
        gps.stop()
