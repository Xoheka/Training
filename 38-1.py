# class Person:
#     def __init__(self, first_name: str, last_name: str):        # tworzy obiekty
#         self.last_name = last_name
#         self.first_name = first_name
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# me = Person('Bartosz', 'Kalenik')
# print(me)

# class Box:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Box({self.capacity})'
#
#     def __lt__(self, other):
#         return self.capacity < other.capacity
#
#
# boxes = [
#     Box(10),
#     Box(40),
#     Box(20)
# ]
#
# for box in sorted(boxes):
#     print(box)


class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)

    def __sub__(self, other):
        total = self.value - other.value
        return LengthUnit(total)

    def __eq__(self, other):
        return self.value == other.value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100  # /1000


def test_add_length_units():
    #given
    length = LengthUnit(10)
    length2 = LengthUnit(50)
    #when
    length3 = length + length2
    #then
    assert length3.value == 60


def test_sub_length_units():
    #given
    length = LengthUnit(10)
    length2 = LengthUnit(50)
    #when
    length3 = length2 - length
    #then
    assert length3.value == 40


def test_eq_length_units():
    #given
    length = LengthUnit(20)
    length2 = LengthUnit(20)
    #when
    length3 = length2 - length
    #then
    assert length == length2