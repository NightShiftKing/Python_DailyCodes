class Frog():
    def __init__(self, name, color, size):
    
        self.name = name
        self.color = color
        self.size = size
        self.hunger_level = 0
        self.energy_level = 10


    def ribbit(self):
        print("Greninja")
        self.hunger_level +1

    def jump(self):
        print("BIGGGG Jump")
        self.energy_level -2
        self.hunger_level +1

    def eat(self, fly_count):
        self.energy_level = self.energy_level + fly_count
        self.hunger_level = self.hunger_level - fly_count/2
        print("YUM YUM! you ate ", fly_count," flies!")

    def sleep(self):
        self.energy_level = 10
        print("Zzz... the frog is sleeping")

    def status(self):
        print("Name is:",self.name)
        print("Color is:", self.color)
        print("Size is:",self.size)
        print("Hunger level is:",self.hunger_level)
        print("Energy level is:",self.energy_level)

Greninja = Frog("Greninja", "Blue", "Large")

Greninja.status() 