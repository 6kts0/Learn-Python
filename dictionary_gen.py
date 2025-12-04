"""
Generating a dictionairy with a loop
"""

import pandas as pd

DICT_MAIN = {}

# Initialize keys
categories = ["Sedan", "Suv", "Sport", "Super", "Hatchback"]

# Initialize value elements
sedan_type = ['Cadillac CT5-V', 'Lucid Air Sapphire', 'Kia K5 LXS', 'Honda Civic', 'Hyundai Elantra', 'Genesis G80', 'BMW 7-series', 'Subaru WRX', 'Lexus ES', 'Tesla Model 3', 'Acura Integra', 'Toyota Camry', 'Toyota Crown', 'Audi S3', 'BMW 3-series']

suv_type = ['Jeep Grand Cherokee', 'Honda CR-V', 'Audi RS Q8', 'Porsche Macan GTS', 'Kia Telluride', 'Chevrolet Trax', 'Ferrari Purosangue', 'Buick Envista', 'Kia Niro ', 'Volvo XC60', 'Mazda CX-90', 'Honda Passport', 'Kia Sportage', 'Ford Mustang Mach-E', 'Cadillac Escalade']

sport_type = ['BMW M2', 'Honda Civic Type-R', 'Mustang GT350', 'Chevrolet Corevette ZR1', 'Audi RS3', 'Porshe 911', 'Mercedes AMG GT', 'Aston Martin Vantage', 'Nissan GTR', 'Mitsubishi Lancer Evo', 'Lotus Emira', 'Cadillac CTS-V', 'Audi E-Tron', 'Lexus LFA', 'Toyota GR Supra']

super_type = ['Ferrari 812 Superfast', 'Lamborghini Revuelto', 'Aston Martin Valkyrae', 'Maclaren 720S', 'Koenigsegg CC850', 'Bugatti Chiron', 'Ferrari F8', 'Lamborghini Murcielago', 'Corevette C8', 'Ferrari SF90', 'Mercedes-AMG ONE', 'Lotus Evija', 'Ferrari 488 Pista', 'Rimac Nevera', 'Ford GT'] 

hatch_type = ['Honda Civic', 'Mazda 3', 'Volkswagen Golf', 'MINI Cooper', 'Toyota Prius', 'Kia Soul', 'Chevrolet Bolt', 'Toyota GR Corolla', 'BMW 4-Series', 'Audi RS7', 'BMW i4', 'Mazda CX-30', 'Volvo EX30', 'Subaru Impreza', 'Hyundai Ioniq 5']

all_cars = [sedan_type, suv_type, sport_type, super_type, hatch_type]


# For each key name the corresponding list will be added as its value
for i in range(len(categories)):
    DICT_MAIN[categories[i]] = all_cars[i]

# Order dictionary into a dataframe to print tabular data
DICT_MAIN_df = pd.DataFrame(DICT_MAIN) 

print(DICT_MAIN_df)






