# Ford Inventory
class vehicle_class():
    def __init__(self, name, classID):
        self.name = name
        self.classID = classID

    def CLS(self):
        print("Vehicle Class:", self.name, self.classID)

"""
Vehicle class IDs
"""
# coupe: 11
# sport: 13
# suv: 17
# truck: 19
# off-road: 29
# track: 79
coupe = vehicle_class("Coupe", 11)
sport = vehicle_class("Sport", 13)
suv = vehicle_class("SUV", 17)
truck = vehicle_class("Truck", 19)
offroad = vehicle_class("Off-Road", 29)
track = vehicle_class("track", 79)

print("Classes: | Coupe -- Sport -- SUV -- Truck -- Off-Road -- Track |")
view_class = input("(ADMIN) View vehicle class IDs: ").lower().strip()
if view_class == 'coupe':
    coupe.CLS()
elif view_class == 'sport':
    sport.CLS()
elif view_class == 'suv':
    suv.CLS()
elif view_class == 'truck':
    truck.CLS()
elif view_class == 'offroad' or view_class == 'off-road':
    offroad.CLS()
elif view_class == 'track':
    track.CLS()

class styleSUV():
    def __init__(self, name, year, msrp, engine, gearbox, power, vin):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power
        self.vin = vin

    def SUV(self):
        print("Vehicle summary:", self.name, self.year, self.msrp, self.engine, self.gearbox, self.power, self.vin)

fordKuga = styleSUV("Ford Kuga", 2024, 32000, "1.5L EcoBoost", "6-Speed Manual", "150HP", 15787)

fordKuga.SUV()











