from kivy_garden.mapview import MapMarker
from toasts import toasts


class paths:
    def __init__(self):
        self.toasts = toasts()
        self.From_SP1_to_SP5_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.271631, lon=73.413228, source="point.png"),
            MapMarker(lat=61.271032, lon=73.417133, source="point.png"),
            MapMarker(lat=61.270598, lon=73.420051, source="point.png"),
            MapMarker(lat=61.270143, lon=73.423013, source="point.png"),
            MapMarker(lat=61.269709, lon=73.425545, source="point.png"),
            MapMarker(lat=61.268697, lon=73.424858, source="point.png"),
            MapMarker(lat=61.266837, lon=73.423356, source="point.png"),
            MapMarker(lat=61.264542, lon=73.422041, source="point.png"),
            MapMarker(lat=61.262124, lon=73.420582, source="point.png"),
            MapMarker(lat=61.260264, lon=73.419423, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)]
        # Маршрут от 1 до 5 сп

        self.From_SP1_to_SP4_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.259176, lon=73.418713, source="point.png"),
            MapMarker(lat=61.259471, lon=73.418879, source="point.png"),
            MapMarker(lat=61.260049, lon=73.419239, source="point.png"),
            MapMarker(lat=61.260587, lon=73.419550, source="point.png"),
            MapMarker(lat=61.261146, lon=73.419915, source="point.png"),
            MapMarker(lat=61.261884, lon=73.420344, source="point.png"),
            MapMarker(lat=61.262649, lon=73.420805, source="point.png"),
            MapMarker(lat=61.263264, lon=73.421202, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.264044, lon=73.421674, source="point.png"),
            MapMarker(lat=61.264374, lon=73.418736, source="point.png"),
            MapMarker(lat=61.264249, lon=73.419907, source="point.png"),
            MapMarker(lat=61.264712, lon=73.415550, source="point.png"),
            MapMarker(lat=61.264940, lon=73.413833, source="point.png"),
            MapMarker(lat=61.264642, lon=73.416533, source="point.png"),
            MapMarker(lat=61.265064, lon=73.412718, source="point.png"),
            MapMarker(lat=61.264611, lon=73.412482, source="point.png"),
            MapMarker(lat=61.264249, lon=73.412278, source="point.png"),
            MapMarker(lat=61.258884, lon=73.418540, source="point.png"),
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4)]
        # Маршрут от 1 до 4 сп

        self.From_SP1_to_SP3_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.249211, lon=73.374239, source="point.png"),
            MapMarker(lat=61.248991, lon=73.375709, source="point.png"),
            MapMarker(lat=61.248347, lon=73.381055, source="point.png"),
            MapMarker(lat=61.248583, lon=73.378246, source="point.png"),
            MapMarker(lat=61.248521, lon=73.382605, source="point.png"),
            MapMarker(lat=61.249052, lon=73.386604, source="point.png"),
            MapMarker(lat=61.248759, lon=73.384394, source="point.png"),
            MapMarker(lat=61.248759, lon=73.384394, source="point.png"),
            MapMarker(lat=61.249364, lon=73.388654, source="point.png"),
            MapMarker(lat=61.249602, lon=73.390220, source="point.png"),
            MapMarker(lat=61.249795, lon=73.391395, source="point.png"),
            MapMarker(lat=61.250426, lon=73.392146, source="point.png"),
            MapMarker(lat=61.250870, lon=73.392650, source="point.png"),
            MapMarker(lat=61.251421, lon=73.393262, source="point.png"),
            MapMarker(lat=61.251922, lon=73.393820, source="point.png"),
            MapMarker(lat=61.252369, lon=73.394324, source="point.png"),
            MapMarker(lat=61.252860, lon=73.394893, source="point.png"),
            MapMarker(lat=61.253305, lon=73.395397, source="point.png"),
            MapMarker(lat=61.253527, lon=73.396105, source="point.png"),
            MapMarker(lat=61.253591, lon=73.396915, source="point.png"),
            MapMarker(lat=61.254248, lon=73.397253, source="point.png"),
            MapMarker(lat=61.254728, lon=73.396802, source="point.png"),
            MapMarker(lat=61.255057, lon=73.396877, source="point.png"),
            MapMarker(lat=61.256204, lon=73.397462, source="point.png"),
            MapMarker(lat=61.255596, lon=73.397164, source="point.png"),
            MapMarker(lat=61.253926, lon=73.397340, source="point.png"),
            MapMarker(lat=61.256834, lon=73.397784, source="point.png"),
            MapMarker(lat=61.257594, lon=73.398159, source="point.png"),
            MapMarker(lat=61.258178, lon=73.398460, source="point.png"),
            MapMarker(lat=61.258178, lon=73.398460, source="point.png"),
            MapMarker(lat=61.259453, lon=73.399074, source="point.png"),
            MapMarker(lat=61.259351, lon=73.399975, source="point.png"),
            MapMarker(lat=61.259233, lon=73.400884, source="point.png"),
            MapMarker(lat=61.259124, lon=73.401946, source="point.png"),
            MapMarker(lat=61.258969, lon=73.403255, source="point.png"),
            MapMarker(lat=61.258809, lon=73.404467, source="point.png"),
            MapMarker(lat=61.258690, lon=73.405626, source="point.png"),
            MapMarker(lat=61.258509, lon=73.407300, source="point.png"),
            MapMarker(lat=61.258975, lon=73.398845, source="point.png"),
            MapMarker(lat=61.258375, lon=73.408437, source="point.png"),
            MapMarker(lat=61.258173, lon=73.410003, source="point.png"),
            MapMarker(lat=61.258028, lon=73.411297, source="point.png"),
            MapMarker(lat=61.257909, lon=73.412338, source="point.png"),
            MapMarker(lat=61.257770, lon=73.413475, source="point.png"),
            MapMarker(lat=61.257651, lon=73.414580, source="point.png"),
            MapMarker(lat=61.257547, lon=73.415556, source="point.png"),
            MapMarker(lat=61.257423, lon=73.416490, source="point.png"),
            MapMarker(lat=61.257305, lon=73.417562, source="point.png"),
            MapMarker(lat=61.257977, lon=73.417957, source="point.png"),
            MapMarker(lat=61.258592, lon=73.418354, source="point.png"),
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3)]
        # Маршрут от 1 до 3 сп

        self.From_SP1_to_SP2_points = [
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            MapMarker(lat=61.251057, lon=73.414062, source="point.png"),
            MapMarker(lat=61.251417, lon=73.416054, source="point.png"),
            MapMarker(lat=61.251650, lon=73.417315, source="point.png"),
            MapMarker(lat=61.251901, lon=73.418618, source="point.png"),
            MapMarker(lat=61.252660, lon=73.418020, source="point.png"),
            MapMarker(lat=61.253451, lon=73.417398, source="point.png"),
            MapMarker(lat=61.254236, lon=73.416797, source="point.png"),
            MapMarker(lat=61.254841, lon=73.416464, source="point.png"),
            MapMarker(lat=61.255441, lon=73.416502, source="point.png"),
            MapMarker(lat=61.256195, lon=73.416888, source="point.png"),
            MapMarker(lat=61.256882, lon=73.417307, source="point.png"),
            MapMarker(lat=61.257725, lon=73.417832, source="point.png"),
            MapMarker(lat=61.258463, lon=73.418272, source="point.png"),
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2)]
        # Маршрут от 1 до 2 сп

        self.From_SP2_to_SP5_points = [*self.From_SP1_to_SP2_points[1:], *self.From_SP1_to_SP5_points[1:]]
        # Маршрут от 2 до 5 сп

        self.From_SP2_to_SP4_points = [
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2),
            MapMarker(lat=61.251057, lon=73.414062, source="point.png"),
            MapMarker(lat=61.251417, lon=73.416054, source="point.png"),
            MapMarker(lat=61.251650, lon=73.417315, source="point.png"),
            MapMarker(lat=61.251901, lon=73.418618, source="point.png"),
            MapMarker(lat=61.252660, lon=73.418020, source="point.png"),
            MapMarker(lat=61.253451, lon=73.417398, source="point.png"),
            MapMarker(lat=61.254236, lon=73.416797, source="point.png"),
            MapMarker(lat=61.254841, lon=73.416464, source="point.png"),
            MapMarker(lat=61.255441, lon=73.416502, source="point.png"),
            MapMarker(lat=61.256195, lon=73.416888, source="point.png"),
            MapMarker(lat=61.256882, lon=73.417307, source="point.png"),
            MapMarker(lat=61.257498, lon=73.417694, source="point.png"),
            MapMarker(lat=61.257694, lon=73.415876, source="point.png"),
            MapMarker(lat=61.257953, lon=73.413966, source="point.png"),
            MapMarker(lat=61.258118, lon=73.412013, source="point.png"),
            MapMarker(lat=61.258376, lon=73.410425, source="point.png"),
            MapMarker(lat=61.258469, lon=73.409417, source="point.png"),
            MapMarker(lat=61.259022, lon=73.409685, source="point.png"),
            MapMarker(lat=61.259703, lon=73.409996, source="point.png"),
            MapMarker(lat=61.260432, lon=73.410361, source="point.png"),
            MapMarker(lat=61.261300, lon=73.410790, source="point.png"),
            MapMarker(lat=61.262225, lon=73.411252, source="point.png"),
            MapMarker(lat=61.263143, lon=73.411751, source="point.png"),
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4)]
        # Маршрут от 2 до 4 сп

        self.From_SP2_to_SP3_points = [
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3),
            *self.From_SP1_to_SP3_points[1:11],
            MapMarker(lat=61.249802, lon=73.391474, source="point.png"),
            MapMarker(lat=61.249342, lon=73.392086, source="point.png"),
            MapMarker(lat=61.248980, lon=73.392504, source="point.png"),
            MapMarker(lat=61.248582, lon=73.392965, source="point.png"),
            MapMarker(lat=61.248226, lon=73.393287, source="point.png"),
            MapMarker(lat=61.248257, lon=73.394317, source="point.png"),
            MapMarker(lat=61.249802, lon=73.391474, source="point.png"),
            MapMarker(lat=61.248200, lon=73.396130, source="point.png"),
            MapMarker(lat=61.248179, lon=73.397439, source="point.png"),
            MapMarker(lat=61.248242, lon=73.398321, source="point.png"),
            MapMarker(lat=61.248454, lon=73.399597, source="point.png"),
            MapMarker(lat=61.248718, lon=73.401035, source="point.png"),
            MapMarker(lat=61.248976, lon=73.402505, source="point.png"),
            MapMarker(lat=61.249236, lon=73.404205, source="point.png"),
            MapMarker(lat=61.249520, lon=73.405696, source="point.png"),
            MapMarker(lat=61.249805, lon=73.407263, source="point.png"),
            MapMarker(lat=61.250079, lon=73.408754, source="point.png"),
            MapMarker(lat=61.250234, lon=73.409583, source="point.png"),
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2)]
        # Маршрут от 2 до 3 сп

        self.From_SP3_to_SP4_points = [
            self.From_SP1_to_SP3_points[-1],
            *self.From_SP1_to_SP3_points[1:41],
            *self.From_SP2_to_SP4_points[:-9:-1]]
        # Маршрут от 3 до 4 сп

        self.From_SP3_to_SP5_points = [
            self.From_SP1_to_SP3_points[-1],
            *self.From_SP1_to_SP3_points[1:41],
            *self.From_SP2_to_SP4_points[-2:-9:-1],
            *self.From_SP1_to_SP5_points[1:9],
            MapMarker(lat=61.267886, lon=73.424159, source="point.png"),
            MapMarker(lat=61.265541, lon=73.422647, source="point.png"),
            MapMarker(lat=61.264026, lon=73.421655, source="point.png"),
            MapMarker(lat=61.264263, lon=73.419595, source="point.png"),
            MapMarker(lat=61.264532, lon=73.417363, source="point.png"),
            MapMarker(lat=61.264713, lon=73.415808, source="point.png"),
            MapMarker(lat=61.264909, lon=73.414102, source="point.png"),
            MapMarker(lat=61.265069, lon=73.412707, source="point.png"),
            MapMarker(lat=61.264496, lon=73.412407, source="point.png"),
            MapMarker(lat=61.263864, lon=73.412099, source="point.png"),
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)]
        # Маршрут от 3 до 5 сп

        self.From_SP4_to_SP5_points = [
            self.From_SP1_to_SP5_points[-1],
            *self.From_SP1_to_SP5_points[1:9],
            *self.From_SP1_to_SP4_points[13:20],
            self.From_SP1_to_SP4_points[-1]]
        # Маршрут от 4 до 5 сп

    def get_list_points(self, a, b):
        if (a == '1 СП' and b == '5 СП') or (a == '5 СП' and b == '1 СП'):
            return self.From_SP1_to_SP5_points
        elif (a == '1 СП' and b == '4 СП') or (a == '4 СП' and b == '1 СП'):
            return self.From_SP1_to_SP4_points
        elif (a == '1 СП' and b == '3 СП') or (a == '3 СП' and b == '1 СП'):
            return self.From_SP1_to_SP3_points
        elif (a == '1 СП' and b == '2 СП') or (a == '2 СП' and b == '1 СП'):
            return self.From_SP1_to_SP2_points
        elif (a == '2 СП' and b == '5 СП') or (a == '5 СП' and b == '2 СП'):
            return self.From_SP2_to_SP5_points
        elif (a == '2 СП' and b == '4 СП') or (a == '4 СП' and b == '2 СП'):
            return self.From_SP2_to_SP4_points
        elif (a == '2 СП' and b == '3 СП') or (a == '3 СП' and b == '2 СП'):
            return self.From_SP2_to_SP3_points
        elif (a == '3 СП' and b == '4 СП') or (a == '4 СП' and b == '3 СП'):
            return self.From_SP3_to_SP4_points
        elif (a == '3 СП' and b == '5 СП') or (a == '5 СП' and b == '3 СП'):
            return self.From_SP3_to_SP5_points
        elif (a == '4 СП' and b == '5 СП') or (a == '5 СП' and b == '4 СП'):
            return self.From_SP4_to_SP5_points

    def get_allSP_points(self):
        self.allSP_points = [
            # Маркер для СП1:
            MapMarker(lat=61.258720, lon=73.418079, source="station_marker.png", on_press=toasts.toast_for_SP1),
            # Маркер для СП2:
            MapMarker(lat=61.250593, lon=73.411524, source="station_marker.png", on_press=toasts.toast_for_SP2),
            # Маркер для СП3:
            MapMarker(lat=61.249223, lon=73.374205, source="station_marker.png", on_press=toasts.toast_for_SP3),
            # Маркер для СП4:
            MapMarker(lat=61.263820, lon=73.412419, source="station_marker.png", on_press=toasts.toast_for_SP4),
            # Маркер для СП5:
            MapMarker(lat=61.272384, lon=73.413556, source="station_marker.png", on_press=toasts.toast_for_SP5)]
        return self.allSP_points

    def get_all_points(self):
        return [self.From_SP1_to_SP5_points, self.From_SP1_to_SP4_points, self.From_SP1_to_SP3_points,
                      self.From_SP1_to_SP2_points, self.From_SP2_to_SP5_points, self.From_SP2_to_SP4_points,
                      self.From_SP2_to_SP3_points, self.allSP_points]