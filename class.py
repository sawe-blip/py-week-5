# --- Superhero Classes (Encapsulation + Inheritance) ---

class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.__strength = strength  # Private attribute

    def show_power(self):
        print(f"{self.name} uses the power: {self.power}")

    def get_strength(self):
        return self.__strength

class FlyingHero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h")


# --- Vehicle Classes (Polymorphism) ---

class Vehicle:
    def move(self):
        print("This vehicle moves")

class Car(Vehicle):
    def move(self):
        print("The car is driving")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing")


# --- Create and Use Objects ---

print("=== Superhero Section ===")
hero1 = Superhero("Shadow", "Invisibility", 90)
hero2 = FlyingHero("SkyWing", "Wind Blast", 85, 300)

hero1.show_power()
print(f"{hero1.name}'s strength is: {hero1.get_strength()}")

hero2.show_power()
hero2.fly()

print("\n=== Vehicle Polymorphism Section ===")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()


