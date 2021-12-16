# ---
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
# ---

from realestate.familyhome import attributes
class Highlights(attributes.Characteristics):  
    garage1 = {"1": 'No Garage available', "2": 'Garage with one car capacity', "3 or more": 'Garage with two cars capacity'}
    garage2 = {"1": 'No Swimming Pool', "2": 'No Swimming Pool or Indoor Swimming Pool', "3 or more": 'No Swimming Pool, Indoor Swimming Pool or Outdoor Swimming Pool'}
    garage3 = {"1": 'Partially Furnished', "2": 'Partially Furnished or Fully Furnished', "3 or more": 'Fully Furnished or Luxuriously Furnished'}
    
    pool1 = {"low": 'Garage with one car capacity', "medium": 'No Garage available', "high": 'Garage with two cars capacity'}
    pool2 = {"low": 'No Swimming Pool', "medium": 'No Swimming Pool or Indoor Swimming Pool', "high": 'No Swimming Pool, Indoor Swimming Pool or Outdoor Swimming Pool'}
    pool3 = {"low": 'Partially Furnished', "medium": 'Partially Furnished or Fully Furnished', "high": 'Fully Furnished or Luxuriously Furnished'}
    
    furn1 = {"1": 'No Garage available', "2": 'Garage with one car capacity', "3": 'Garage with two cars capacity'}
    furn2 = {"1": 'No Swimming Pool', "2": 'No Swimming Pool or Indoor Swimming Pool', "3": 'No Swimming Pool, Indoor Swimming Pool or Outdoor Swimming Pool'}
    furn3 = {"1": 'Partially Furnished', "2": 'Partially Furnished or Fully Furnished', "3": 'Fully Furnished or Luxuriously Furnished'}    
            
    def __init__(self, fm, b, f):
        attributes.Characteristics.__init__(self, fm, b, f)
        
    def garage_capacity(self):
        return Highlights.garage1[self.fm]
        
    def swimming_pool_type(self):
        return Highlights.garage2[self.fm]
        
    def furnish_type(self):
        return Highlights.garage3[self.fm]
    
    
    def Characteristics_display(self):
        attributes.Quality.Characteristics_display(self)
        print("The garage options you will get based on your choices are {}.".format(Highlights.garage1[self.fm]))
        print("The Swimming pool options you will get based on your choices are {}.".format(Highlights.garage2[self.fm]))  
        print("The furnishing condition of your house based on your choices is {}.".format(Highlights.garage3[self.fm]))  

obj = Highlights('1', 'low', '1')

obj.Characteristics_display()


