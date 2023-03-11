# Practice Playground

# [challenge] take any number of args and return a sum of all args
def add(*args):
    num = 0
    for n in args:
        num += n
    print(num)


add(1, 2, 3, 4, 5)  # 15
add(3, 40, 38, 2837, 38, 902, 12)  # 3870

#


class Car:
    def __init__(self, **kwargs):
        # using `kwargs.get()`, we can set parameters to these attributes
        # as completely optional
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car = Car(make="Nissan")

print(my_car.model)  # None
print(my_car.make)  # Nissan


def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)


all_aboard(4, 7, 3, 0, x=10, y=64)
# 4 (7, 3, 0) {'x': 10, 'y': 64}
