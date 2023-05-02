#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "brand", color = "color", size = 0, material = "material", condition = "condition"):
        self.brand = brand
        self.color = color
        self.size = size
        self.material = material
        self.condition = condition
    
    def get_brand(self):
        print('Retrieving brand')
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    brand = property(get_brand, set_brand)

    def get_color(self):
        print('Retrieving color')
        return self._color

    def set_color(self, color):
        self._color = color

    color = property(get_color, set_color)

    def get_size(self):
        print('Retrieving size')
        return self._size

    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def get_material(self):
        print('Retrieving material')
        return self._material

    def set_material(self, material):
        self._material = material

    material = property(get_material, set_material)

    def get_condition(self):
        print('Retrieving condition')
        return self._condition

    def set_condition(self, condition):
        self._condition = condition

    condition = property(get_condition, set_condition)

    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')