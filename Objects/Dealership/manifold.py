from currencies import Currency

currency = Currency('USD')

# Ford Inventory
class vehicle_class():
    def __init__(self, className, classID):
        self.className = className
        self.classID = classID


    def CLS(self):
        print('|', self.className, '|', self.classID, '|')

# VEHICLE IDs
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
track = vehicle_class("Track", 79)

class styleSUV():
    def __init__(self, name, year, msrp, engine, gearbox, power, className=suv):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power
        self.className = className

    def SUV(self):
        print("| Model | Year | MSRP | Engine | Gearbox | Power (WHP) |")
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power, )
        print('-' * 80)

fordKuga = styleSUV('Ford Kuga', 2024, '32,000', '1.5L EcoBoost', '6-Speed Manual', '150', suv)
fordExpd = styleSUV('Ford Expedition', 2025, '62,400', '3.5L EcoBoost V6', '10-Speed Automatic Transmission', '406', suv)
fordMache =  styleSUV('Ford Mustang MACH-E', 2023, '25,985', '98.8 Kw Electric', 'Single-Speed/Reduction Drive', 465, suv)

def viewSuv_inv():
    suvCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if suvCat == 'yes':
        print('=' * 80)
        print("SUV - IN STOCK")
        print('=' * 80)
        fordKuga.SUV()
        fordExpd.SUV()
        fordMache.SUV()
    else:
        exit

print("-- VEHICLE CLASS TYPES --")
print('=' * 80)
print("| Coupe | Sport | SUV | Truck | Off-Road | Track |")
print('=' * 80)
view_class = input("Show vehicle class info: ").lower().strip()
if view_class == 'coupe':
    coupe.CLS()
elif view_class == 'sport':
    sport.CLS()
elif view_class == 'suv':
    print('=' * 80)
    print("| Class Name | Class ID")
    suv.CLS()
    print('=' * 80)
    viewSuv_inv()
elif view_class == 'truck':
    truck.CLS()
elif view_class == 'offroad' or view_class == 'off-road':
    offroad.CLS()
elif view_class == 'track':
    track.CLS()