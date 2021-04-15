# -*- coding: utf-8 -*-

class Car:
    def __init__(self, make, model, year, color, doors, ext_type, drive, gas_hybr_elect, horse_power, price):
        self.car_make, self.car_model, self.car_year, self.car_color, self.car_doors, self.car_ext_type, self.car_drive, self.car_gas_hybr_elect, self.car_horse_power, self.car_price  \
        = make, model, year, color, doors, ext_type, drive, gas_hybr_elect, horse_power, price
        print(f'Car: {make}, {model}, year:{year}, {color}, doors:{doors}, {ext_type}, {drive}, {gas_hybr_elect}, horse power:{horse_power}, price: ${price}\n')

    def ordered(self):
        print(f'{self.car_make}/{self.car_model}/year: {self.car_year}/{self.car_color}/doors: {self.car_doors}/exterior type: {self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power: {self.car_horse_power}/{self.car_price}: is ordered\n')

    def in_stock(self):
        print(f'{self.car_make}/{self.car_model}/year: {self.car_year}/{self.car_color}/doors: {self.car_doors}/exterior type: {self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power: {self.car_horse_power}/{self.car_price}: in stock\n')

    def sold(self):
        print(f'{self.car_make}/{self.car_model}/year: {self.car_year}/{self.car_color}/doors: {self.car_doors}/exterior type: {self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power: {self.car_horse_power}/{self.car_price}: is sold\n')

    def discount_price(self, discount = int(input('Enter the % discount: 10-30: \n'))):
        print(f'Price of "{self.car_make}/{self.car_model}/year: {self.car_year}" discounted %{discount} is: ${self.car_price/100*(100-discount)} VS base price: ${self.car_price}\n')

car1 = Car('Toyota', 'CHR', 2018, 'Grey Mettallic', 5, 'SUV', 'FWD', 'Gas', 164, 23242)
car1.in_stock()
car1.sold()

car2 = Car('Tesla', 'Model Y', 2021, 'Navy Blue', 5, 'SUV', 'AWD', 'Electro', 222, 50444)
car2.in_stock()
car2.sold()
car2.discount_price()

car3 = Car('Tesla', 'Model X', 2021, 'Yellow', 5, 'SUV', 'AWD', 'Electro', 360, 89990)
car3.ordered()




