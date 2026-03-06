"""
FORD INVENTORY MANAGER
"""
from currencies import Currency

currency = Currency('USD')

# Maps a vehicle type name to a numeric class ID
class vehicle_class():
    def __init__(self, className, classID):
        self.className = className
        self.classID = classID

    # Prints class name and ID
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

# Holds spec data for coupe class vehicles
class styleCoupe():
    def __init__(self, name, year, msrp, engine, gearbox, power):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power

    # Print a formatted spec row for coupe vehicle inventory
    def CPE(self):
        print("| Model | Year | MSRP | Engine | Gearbox | Power (WHP) |")
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power )
        print('-' * 80)

# Coupe inventory
fordMdh = styleCoupe('Ford Mustang Dark Horse', 2025, '63,080', '5.0L Naturally Aspirated V8', '6-Speed Manual', 500)
fordCap = styleCoupe('Ford Capri MKIII', 1983, '18,900', '2.9L V6', '4-Speed Manual', 177)
fordMach1 = styleCoupe('Ford Mustang Mach-1', 2021, '57,945', '5.0L V8 TT', '6-Speed Manual', 460)

# Prompt user and print all in-stock coupe vehicles if request is confirmed
def viewCoupe_inv():
    coupeCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if coupeCat == 'yes':
        print('=' * 80)
        print('\n')
        print('Coupe - IN STOCK')
        print('\n')
        print('=' * 80)
        fordMdh.CPE()
        fordCap.CPE()
        fordMach1.CPE()
    else:
        exit

# Holds spec data for sport class vehicles
class styleSport():
    def __init__(self, name, year, msrp, engine, gearbox, power):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power

    # Print a formatted spec row for sport vehicle inventory
    def SPT(self):
        print("| Model | Year | MSRP | Engine | Gearbox | Power (WHP) |")
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power)
        print('-' * 80)

# Sport inventory
fordMshlby = styleSport('Ford Mustang Shelby GT500', 2019, '66,994', '5.2L V8', '7-Speed Manual/Automatic', 770)
fordFrs = styleSport('Ford Focus RS', 2018, '34,990', '2.3L Inline-4', '6-Speed Manual', 350)
fordPrbe = styleSport('Ford Probe GT', 1996, '15,999', '2.5L Naturally Aspirated V6', '5-Speed Manual', 164)

# Prompt user and print all in-stock sport vehicles if request is confirmed
def viewSport_inv():
    sportCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if sportCat == 'yes':
        print('=' * 80)
        print('\n')
        print("Sport - IN STOCK")
        print('\n')
        print('=' * 80)
        fordMshlby.SPT()
        fordFrs.SPT()
        fordPrbe.SPT()
    else:
        exit

# Holds spec data for SUV class vehicles
class styleSUV():
    def __init__(self, name, year, msrp, engine, gearbox, power):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power

    # Print a formatted spec row for SUV vehicle inventory
    def SUV(self):
        print("| Model | Year | MSRP | Engine | Gearbox | Power (WHP) |")
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power)
        print('-' * 80)

# SUV inventory
fordKuga = styleSUV('Ford Kuga', 2024, '32,000', '1.5L EcoBoost', '6-Speed Manual', 150)
fordExpd = styleSUV('Ford Expedition', 2025, '62,400', '3.5L EcoBoost V6', '10-Speed Automatic', 406)
fordMache =  styleSUV('Ford Mustang MACH-E', 2023, '25,985', '98.8 Kw Electric', 'Single-Speed/Reduction Drive', 465)

# Prompt user and print all in-stock SUV vehicles if request is confirmed
def viewSuv_inv():
    suvCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if suvCat == 'yes':
        print('=' * 80)
        print('\n')
        print("SUV - IN STOCK")
        print('\n')
        print('=' * 80)
        fordKuga.SUV()
        fordExpd.SUV()
        fordMache.SUV()
    else:
        exit

# Shows vehicle class menu and displays chosen category details and/or inventory
def main():
    print("-- VEHICLE CLASS TYPES --")
    print('=' * 80)
    print("| Coupe | Sport | SUV | Truck | Off-Road | Track |")
    print('=' * 80)

    # Provides option to view vehicle class details (name + classID) 
    view_class = input("Show vehicle class info: ").lower().strip()
    if view_class == 'coupe':
        print('=' * 80)
        print('| Class Name | Class ID')
        coupe.CLS() # Returns specified class details
        print('=' * 80)
        viewCoupe_inv() # Returns specified vehicle class inventory (Coupe inventory etc.)
    elif view_class == 'sport':
        print('=' * 80)
        print('| Class Name | Class ID')
        sport.CLS()
        print('=' * 80)
        viewSport_inv()
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

main()