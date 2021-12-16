class Features:
    price = {
        '1BHK': '150000 - 200000 CAD', 
        '2BHK': '250000 - 300000 CAD', 
        '3BHK': '350000 - 400000 CAD',
        'USA': '250000 - 400000 USD',
        'CANADA': '200000 - 350000 CAD',
        'UK': '300000 - 500000 POUNDS',
        '0-3': '250000 - 300000 CAD',
        '3-5': '150000 - 250000 CAD'
        }
    area = {
        '1BHK': '500 - 800 sqft', 
        '2BHK': '800 - 1100 sqft', 
        '3BHK': '1100 - 1500 sqft',
        'USA': '500 - 1500 sqft',
        'CANADA': '800 - 1500 sqft',
        'UK': '650 - 1400 sqft',
        '0-3': '800 - 1200 sqft',
        '3-5': '600 - 800 sqft'
        }
    
    def __init__(self, apartmentInfo):
        self.apartmentInfo = apartmentInfo
    
    def apartment_price(self):
        return Features.price[self.apartmentInfo]
    
    def apartment_area(self):
        return Features.area[self.apartmentInfo]
    
    def apartment_display(self):
        print("Price Range for {} Apartment is : {}".format(self.apartmentInfo, self.apartment_price()))
        print("Area Range for {} Apartment is : {}".format(self.apartmentInfo, self.apartment_area()))

class ApartmentType(Features):
    floors = {'1BHK': [2, 3, 7, 11, 13], '2BHK': [1, 4, 5, 8, 10], '3BHK': [6, 9, 12, 14, 15]}
    
    def __init__(self, apartmentType):
        Features.__init__(self, apartmentType)
        
    def apartment_floors(self):
        return ApartmentType.floors[self.apartmentInfo]
    
    def apartment_display(self):
        Features.apartment_display(self)
        print("Floors Available for {} are : {}".format(self.apartmentInfo, self.apartment_floors()))