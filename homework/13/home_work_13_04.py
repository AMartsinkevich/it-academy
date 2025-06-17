class Sphere:

    def __init__(self, radius=1, x_coord=0, y_coord=0, z_coord=0):
        self._radius = radius
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._z_coord = z_coord
        self._pi = 3.1415926535897932384626433832795

    def get_volume(self):
        return round(4 / 3 * self._pi * self._radius ** 3, 2)

    def get_square(self):
        return round(4 * self._pi * self._radius ** 2, 2)

    def get_radius(self):
        return self._radius

    def get_center(self):
        return self._x_coord, self._y_coord, self._z_coord

    def set_radius(self, radius):
        self._radius = radius

    def set_center(self, x_coord, y_coord, z_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._z_coord = z_coord

    def is_point_inside(self, x_coord, y_coord, z_coord):
        distance = ((x_coord - self._x_coord) ** 2 + (y_coord - self._y_coord) ** 2 + (z_coord - self._z_coord) ** 2) ** (1/2)
        return distance < self._radius


if __name__ == '__main__':

    sphere = Sphere()
    print(sphere.get_center())
    print(sphere.get_radius())
    sphere.set_center(1, 2, 3)
    sphere.set_radius(5)
    print(sphere.get_center())
    print(sphere.get_radius())
    print(sphere.get_volume())
    print(sphere.get_square())
    print(sphere.is_point_inside(1, 1, 1))
    print(sphere.is_point_inside(1, 10, 1))
