"""
VEHICLE INVENTORY MANAGER
"""

"""
--ADDITIONS TO IMPLEMENT--
DISCLAIMER: Company/genre is used because I may place the Ford inventory in a broader category for the user to view from (e.g. United States, Japan, Austrailia, etc.)

* Utilize one function to hold all ford vehicle classes and objects created so far **1
* Brainstorm some tasteful vehicle companies and genres to add **2
* Create a function for each new company/genre **3
* Decipher what should be added to create a realistic inventory for the company or companies that are added to the program **4
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
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power )
        print('-' * 100)

# Coupe inventory
fordDark = styleCoupe('Ford Mustang Dark Horse', 2024, '62,515', '5.0L Coyote V8', '6-Speed Manual/10A', 450)
fordPrbe = styleCoupe('Ford Probe GT', 1996, '15,999', '2.5L NA V6', '5-Speed Manual', 164) 
fordCap = styleCoupe('Ford Capri MKIII', 1983, '18,900', '2.9L V6', '4-Speed Manual', 177)
fordS350 = styleCoupe('Ford Mustang Shelby GT350', 2020, '60,440', '5.2L VooDoo V8', '6-Speed Manual', 810)
fordMach1 = styleCoupe('Ford Mustang Mach-1', 2021, '57,945', '5.0L V8 TT', '6-Speed Manual', 460)

# Prompt user and print all in-stock coupe vehicles if request is confirmed
def viewCoupe_inv():
    coupeCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if coupeCat == 'yes':
        print('=' * 100)
        print('\n')
        print('Coupe - IN STOCK')
        print('\n')
        print('=' * 100)
        print("| MODEL | YEAR | MSRP | ENGINE | GEARBOX | POWER (WHP) |")
        print('=' * 100)
        fordMach1.CPE()
        fordCap.CPE()
        fordMach1.CPE()
        fordDark.SPT()
        fordS350.CPE()
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
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power)
        print('-' * 100)

# Sport inventory
fordMshlby = styleSport('Ford Mustang Shelby GT500', 2019, '66,994', '5.2L Predator V8 Supercharged', '7-Speed Dual Clutch', 770)
fordMgt = styleSport('Ford Mustang GT', 2024, '42,805', '5.0K Coyote V8', '6-Speed Manual/10A', 400)
fordPrbe = styleSport('Ford Probe GT', 1996, '15,999', '2.5L NA V6', '5-Speed Manual', 153)
fordDark = styleSport('Ford Mustang Dark Horse', 2024, '62,515', '5.0L Coyote V8', '6-Speed Manual/10A', 450)
fordGt = styleSport('Ford GT', 2022, '500,000', '3.5L EcoBoost V6 Twin-Turbo', '7-Speed Dual Clutch', 550)
fordFrs = styleSport('Ford Focus RS', 2018, '34,990', '2.3L I4 Turbo', '6-Speed Manual', 350)

# Prompt user and print all in-stock sport vehicles if request is confirmed
def viewSport_inv():
    sportCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if sportCat == 'yes':
        print('=' * 100)
        print('\n')
        print("Sport - IN STOCK")
        print('\n')
        print('=' * 100)
        print("| MODEL | YEAR | MSRP | ENGINE | GEARBOX | POWER (WHP) |")
        print('=' * 100)
        fordMshlby.SPT()
        fordFrs.SPT()
        fordPrbe.SPT()
        fordGt.SPT()
        fordMgt.SPT()
        fordDark.SPT()
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
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power)
        print('-' * 100)

# SUV inventory
fordKuga = styleSUV('Ford Kuga', 2024, '32,000', '1.5L EcoBoost', '6-Speed Manual', 150)
fordExpd = styleSUV('Ford Expedition', 2025, '62,400', '3.5L EcoBoost V6', '10-Speed Automatic', 372)
fordMache =  styleSUV('Ford Mustang MACH-E', 2023, '25,985', '98.8 Kw Electric', 'Single-Speed/Reduction Drive', 465)
fordBron = styleSUV('Ford Bronco Raptor', 2026, '79,995', '3.0L EcoBoost V6', '10-Speed Automatic', 418)

# Prompt user and print all in-stock SUV vehicles if request is confirmed
def viewSuv_inv():
    suvCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if suvCat == 'yes':
        print('=' * 100)
        print('\n')
        print("SUV - IN STOCK")
        print('\n')
        print('=' * 100)
        print("| MODEL | YEAR | MSRP | ENGINE | GEARBOX | POWER (WHP) |")
        print('=' * 100)
        fordKuga.SUV()
        fordExpd.SUV()
        fordMache.SUV()
        fordBron.SUV()
    else:
        exit

# Holds spec data for truck class vehicles
class styleTruck():
    def __init__(self, name, year, msrp, engine,  gearbox, power):
        self.name = name
        self.year = year
        self.msrp = msrp
        self.engine = engine
        self.gearbox = gearbox
        self.power = power

    # Print a formatted spec row for truck inventory
    def TRK(self): 
        print('|', self.name, '|', self.year, '|', currency.get_money_with_currency_format(self.msrp), '|', self.engine, '|', self.gearbox, '|', self.power)
        print('-' * 100)

# Truck inventory
fordRapt = styleTruck('Ford F-150 Raptor SVT', 2010, '41,995', '6.2L V8', '6-Speed Automatic', 411)
fordRang = styleTruck('Ford Ranger Double Cab', 2019, '30,300', '2.3L EcoBoost', '10-Speed Automatic', 270)
fordSupd = styleTruck('Ford Super Duty Lariat', 2021, '62,735', '7.3L Power Stroke V8 Turbo', '10-Speed Automatic', 475)
fordLite = styleTruck('Ford F-150 Lighting', 2024, '62,995', 'Dual Electric Motors', 'Single-Speed Automatic', 452)
fordRtrem = styleTruck('Ford Ranger Tremor', 2024, '42,265', '2.3L EcoBoost Turbo', '10-Speed Automatic', 240)

# Prompt user and print all in-stock trucks if request is confirmed
def viewTruck_inv():
    truckCat = input("Would you like to see our inventory (Yes/No): ").lower().strip()
    if truckCat == 'yes':
        print('=' * 100)
        print('\n')
        print("Trucks - IN STOCK")
        print('\n')
        print('=' * 100)
        print("| MODEL | YEAR | MSRP | ENGINE | GEARBOX | POWER (WHP) |")
        print('=' * 100)
        fordRapt.TRK()
        fordRang.TRK()
        fordSupd.TRK()
        fordRtrem.TRK()
        fordLite.TRK()
    else:
        exit

# Shows vehicle class menu and displays chosen category details and/or inventory
def readFord():
    print('=' * 80)
    print("-- VEHICLE CLASS TYPES --")
    print('=' * 80)
    print("| Coupe | Sport | SUV | Truck | Off-Road | Track |")
    print('=' * 80)

    # Provides option to view vehicle class details (name + classID) 
    view_class = input("Show vehicle class info: ").lower().strip()
    if view_class == 'coupe':
        print('=' * 80)
        print('| Class Name | Class ID')
        coupe.CLS()
        print('=' * 80)
        viewCoupe_inv()
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
        print('| Class Name | Class ID')
        truck.CLS()
        print('=' * 80)
        viewTruck_inv()
    elif view_class == 'offroad' or view_class == 'off-road':
        print('| Class Name | Class ID')
        offroad.CLS()
    elif view_class == 'track':
        print('| Class Name | Class ID')
        track.CLS()

readFord()