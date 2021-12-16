# --
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# --

# +
class Error(Exception):
    pass
class NoException(Error):
    pass
class CustomErrorException(Error):
    pass

class Characteristics:  
    family_members1 = {"1": '500000-600000', "2": '600000-700000', "3 or more": '700000-800000'}
    family_members2 = {"1": '1400 sq. ft', "2": '1600 sq. ft', "3 or more": '1800 sq. ft'}
    budget_1 = {"low": '500000-600000', "medium": '600000-700000', "high": '700000-800000'}
    budget_2 = {"low": '1400 sq. ft', "medium": '1600 sq. ft', "high": '1800 sq. ft'}
    floors_1 = {"1": '500000-600000', "2": '600000-700000', "3": '700000-800000'}
    floors_2 = {"1": '1400 sq. ft', "2": '1600 sq. ft', "3": '1800 sq. ft'}
    
        
    def __init__(self, fm, b, f):
        self.fm = fm
        self.b = b
        self.f = f
       
    def house_price(self):
        return Characteristics.family_members1[self.fm]
        
        
    def house_area(self):
        return Characteristics.family_members2[self.fm]
        
        
    def Characteristics_display(self):
        print("The price range you will get based on your choices is {}.".format(Characteristics.family_members1[self.fm]))
        print("The house area you will get based on your choices is {}.".format(Characteristics.family_members2[self.fm]))  
        
        
class Quality(Characteristics):  
    family_members3 = {"1": 'Average Quality', "2": 'Good Quality', "3 or more": 'Excellent Quality'}
    def __init__(self, fm, b, f):
        Characteristics.__init__(self, fm, b, f)
        
          
    def build_quality(self):
        return Quality.family_members3[self.fm]
        
        
    def Characteristics_display(self):
        Characteristics.Characteristics_display(self)
        print("The house quality you will get based on your choices is {}.".format(Quality.family_members3[self.fm]))
         
        
# -
obj = Quality('1', 'low', '1')



obj.Characteristics_display()


try:
    c = Characteristics('1', 'low', '1')
    if c.house_price() == "500000-600000":
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