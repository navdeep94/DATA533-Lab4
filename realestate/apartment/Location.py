from realestate.apartment import Feature

class Location(Feature.Features):
    cities = {
        'USA': ['Chicago','Seattle','New York','Boston'], 
        'CANADA': ['Vancouver','Kelowna','Montreal','Toronto'], 
        'UK': ['London','Birmighan','Leeds','Southampton']
    }
    locality = {
        'USA': ['Charles Street','Brown Road','Morgan Highway','Alpine Park'],
        'CANADA': ['English Bay','Glenmore','Concordia Street','Robson Park'],
        'UK': ['Smith Rd','James Arthur Mall','Michelle Street','Captain James Edward Road']
    }
    
    direction = {
        'USA': ['North','South','East','West','North East'],
        'CANADA': ['South West','North','West','South East'],
        'UK': ['North West','South','South West','East']
    }
        
    def __init__(self, country):
        Feature.Features.__init__(self, country)
        
    def apartment_cities(self):
        return Location.cities[self.apartmentInfo]
    
    def apartment_locality(self):
        return Location.locality[self.apartmentInfo]
    
    def apartment_facing_direction(self):
        return Location.direction[self.apartmentInfo]
        
    def apartment_display(self):
        Feature.Features.apartment_display(self)
        print("Cities Available for {} property are : {}".format(self.apartmentInfo, self.apartment_cities()))
        print("Localities Available for {} property are : {}".format(self.apartmentInfo, self.apartment_locality()))
        print("Directions Available for {} property are : {}".format(self.apartmentInfo, self.apartment_facing_direction()))