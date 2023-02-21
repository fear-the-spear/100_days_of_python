class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # Add name of class you want to inherit from
    def __init__(self):
        super().__init__()  # allow inheritance from 'super' (Animal) class

    def breathe(self):
        super.breathe()  # inherits everything from Animal's 'breathe' method
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)  # 2
