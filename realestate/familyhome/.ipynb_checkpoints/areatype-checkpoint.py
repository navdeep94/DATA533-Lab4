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
class AreaType(attributes.Characteristics):  
    amen1 = {"1": 'Hospital, Park, Shopping Center, School, and a Mall', "2": 'Hospital, Park, Shopping Center, and a School', "3 or more": 'Hospital, Park, Shopping Center, School, Mall, Library, Beach, and a Cafe'}
    amen2 = {"1": 'Normal view, park facing, or sea facing', "2": 'Normal View or Park facing', "3 or more": 'Normal view, park facing, sea facing, or sun facing'}
    amen3 = {"1": 'highly populated', "2": 'average population around', "3 or more": 'very less population'}
    
    view1 = {"low": 'Hospital, Park, Shopping Center, School, and a Mall', "medium": 'Hospital, Park, Shopping Center, and a School', "high": 'Hospital, Park, Shopping Center, School, Mall, Library, Beach, and a Cafe'}
    view2 = {"low": 'Normal view, park facing, or sea facing', "medium": 'Normal View or Park facing', "high": 'Normal view, park facing, sea facing, or sun facing'}
    view3 = {"low": 'average population around', "medium": 'highly populated', "high": 'very less population'}
    
    popu1 = {"1": 'Hospital, Park, Shopping Center, School, and a Mall', "2": 'Hospital, Park, Shopping Center, and a School', "3": 'Hospital, Park, Shopping Center, School, Mall, Library, Beach, and a Cafe'}
    popu2 = {"1": 'Normal View or Park facing', "2": 'Normal view, park facing, or sea facing', "3": 'Normal view, park facing, sea facing, or sun facing'}
    popu3 = {"1": 'highly populated', "2": 'average population around', "3": 'very less population'}    
        
    
    
    def __init__(self, fm, b, f):
        attributes.Characteristics.__init__(self, fm, b, f)
        
    
    def nearby_amenities(self):
        return AreaType.amen1[self.fm]
        
    def view(self):
        return AreaType.amen2[self.fm]
        
    def population(self):
        return AreaType.amen3[self.fm]
    
    def Characteristics_display(self):
        attributes.Quality.Characteristics_display(self)
        print("The amenities you will get based on your choices are {}.".format(AreaType.amen1[self.fm]))
        print("The different views options you will get based on your choices are {}.".format(AreaType.amen2[self.fm]))  
        print("The population around your house based on your choices is {}.".format(AreaType.amen3[self.fm]))  

obj = AreaType('1', 'low', '1')

obj.Characteristics_display()


