from realestate.apartment import Feature

class Error(Exception):
    pass

class NoException(Error):
    pass

class CustomErrorException(Error):
    pass

class Condition(Feature.Features):
    maintenance = {
        '0-3': 'Not Required', 
        '3-5': 'Required'
    }
    
    discount = {
        '0-3': '0-5%',
        '3-5': '5-10%'
    }
    
    furnishingStatus = {
        '0-3': 'Fully Furnished',
        '3-5': 'Semi Furnished'
    }
        
    def __init__(self, country):
        Feature.Features.__init__(self, country)
        
    def apartment_maintenance(self):
        return Condition.maintenance[self.apartmentInfo]
    
    def apartment_discount(self):
        return Condition.discount[self.apartmentInfo]
    
    def apartment_furnishing_status(self):
        return Condition.furnishingStatus[self.apartmentInfo]
        
    def apartment_display(self):
        Feature.Features.apartment_display(self)
        print("Maintenance Status for {} property is : {}".format(self.apartmentInfo, self.apartment_maintenance()))
        print("Discounts Available for {} property are : {}".format(self.apartmentInfo, self.apartment_discount()))
        print("Furnishing Status for {} property are : {}".format(self.apartmentInfo, self.apartment_furnishing_status()))
        
try:
    c = Condition("0-3")
    if c.apartment_maintenance() == "Not Required":
        raise NoException
    else:
        raise CustomErrorException
        
except NoException:
    print("No Exception is there in the code")

except CustomErrorException:
    print("Custom Exception in the code")

except ZeroDivisionError:
    print("Zero Division Error")

except IndexError:
    print("Index Error")
    
except NameError:
    print("Name Error")
    
except IndentationError:
    print("Indentation Error")
    
else:
    print("Some other unknown error")
    
finally:
    print("Code is finally executed")