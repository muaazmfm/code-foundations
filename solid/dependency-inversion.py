from abc import ABC, abstractmethod

# Bad
class Bulb:
    def __init__(self):
        self.status = False

class Switch:
    def __init__(self, bulb:Bulb):
        self.bulb = bulb

    def toggle(self):
        self.bulb.status = not self.bulb.status

# Good
class Switchable(ABC):
    @abstractmethod
    def toggle(self):
        pass

class Bulb2(Switchable):
    def __init__(self):
        self.status = False

    def toggle(self):
        self.status = not self.status

if __name__ == "__main__":
    switch = Switch(Bulb())
    print(switch.bulb.status)
    switch.toggle()
    print(switch.bulb.status)
    switch.toggle()
    print(switch.bulb.status)

    bulb = Bulb2()
    print(bulb.status)
    bulb.toggle()
    print(bulb.status)


