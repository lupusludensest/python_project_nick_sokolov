# -*- coding: utf-8 -*-
import winsound
freq, duration  = 380, 2000   # Hz/milliseconds

class Car:
    def __init__(self, make, model, year, color, doors, ext_type, drive, gas_hybr_elect, horse_power, price, max_passangers):
        self.car_make, self.car_model, self.car_year, self.car_color, self.car_doors, self.car_ext_type, self.car_drive, self.car_gas_hybr_elect, self.car_horse_power, self.car_price, self.max_passangers, self.car_passangers, self.car_pssngrs_as_prsns \
        = make, model, year, color, doors, ext_type, drive, gas_hybr_elect, horse_power, price, max_passangers, 0, []
        print(f'Car: {make}, {model}, year:{year}, {color}, doors:{doors}, {ext_type}, {drive}, {gas_hybr_elect}, horse power:{horse_power}, price: ${price}, max passangers: {max_passangers}\n')

    def ordered(self):
        print(f'{self.car_make}/{self.car_model}/year: {self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}: is ordered\n')

    def in_stock(self):
        print(f'{self.car_make}/{self.car_model}/year: {self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}: in stock\n')

    def sold(self):
        print(f'{self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}: is sold\n')

    def discount_price(self, discount = int(input('Enter the % discount: \n'))):
        print(f'Price of "{self.car_make}/{self.car_model}/year:{self.car_year}" discounted %{discount} is: ${self.car_price/100*(100-discount)} VS base price: ${self.car_price}/max.pass.:{self.max_passangers}\n')

    def check_passangers(self):
        print(f'There are "{int(self.car_passangers)}" passangers are in the {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers} ')

    def check_pssngrs_as_prsns(self):
        print(f'There are "{int(len(self.car_pssngrs_as_prsns))}" passangers are in the {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers} ')

    def add_pssngrs_as_prsns(self, psngr_nm):
        if len(self.car_pssngrs_as_prsns) + 1  < self.max_passangers:
            mssg = f'{psngr_nm} got the car {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers} '
            self.car_pssngrs_as_prsns.append(psngr_nm)
        elif len(self.car_pssngrs_as_prsns) + 1  == self.max_passangers:
            mssg = f'{psngr_nm} got the car, but no more space! {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers} '
            self.car_pssngrs_as_prsns.append(psngr_nm)
        elif len(self.car_pssngrs_as_prsns) + 1  > self.max_passangers:
            winsound.Beep(freq, duration)
            mssg = f'No more space! in {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers} '
        return print(mssg)

    def passangers_get_in(self, psngrs_qntty = int(input('Enter quantity of the passangers: \n'))):
        if psngrs_qntty <= self.max_passangers:
            print_out = (f'{psngrs_qntty} passangers are in the {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}')
            self.car_passangers += psngrs_qntty
        elif psngrs_qntty == self.max_passangers:
            print_out = (f'Max passangers! {psngrs_qntty} passanger/s is/are in the {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}')
            self.car_passangers += self.max_passangers
        elif psngrs_qntty > self.max_passangers:
            winsound.Beep(freq, duration)
            print_out = (f'No more passangers! {psngrs_qntty - self.max_passangers} passengers are excessive to the  {self.car_make}/{self.car_model}/year:{self.car_year}/{self.car_color}/doors:{self.car_doors}/exterior type:{self.car_ext_type}/{self.car_drive}/{self.car_gas_hybr_elect}/horse power:{self.car_horse_power}/${self.car_price}/max.pass.:{self.max_passangers}')
            self.car_passangers += self.max_passangers
        return print(print_out)

car1 = Car('Toyota', 'CHR', 2018, 'Grey Mettallic', 5, 'SUV', 'FWD', 'Gas', 164, 23242, 5)
car1.in_stock()
car1.sold()

car2 = Car('Tesla', 'Model Y', 2021, 'Navy Blue', 5, 'SUV', 'AWD', 'Electro', 222, 50444, 5)
car2.in_stock()
car2.sold()
car2.discount_price()

car3 = Car('Tesla', 'Model X', 2021, 'Yellow', 5, 'SUV', 'AWD', 'Electro', 360, 89990, 6)
car3.ordered()
# car3.passangers_get_in()
# car3.check_passangers()
car3.add_pssngrs_as_prsns('Foo')
car3.add_pssngrs_as_prsns('Booo')
car3.add_pssngrs_as_prsns('Roooo')
car3.add_pssngrs_as_prsns('Woo')
car3.add_pssngrs_as_prsns('Mooo')
car3.add_pssngrs_as_prsns('Toooo')
car3.add_pssngrs_as_prsns('Qoooo0')
car3.check_pssngrs_as_prsns()




