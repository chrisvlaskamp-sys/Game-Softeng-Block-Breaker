import pygame
class Action:

    def __init__(self, name, action_type, action_value = None): 
        self.name = name 
        self.action_type = action_type 
        self.action_value = action_value 
      
    

    def __repr__(self):
        if self.action_type == 'accelerate': 
            return f"name: {self.name} acceleration:{self.acceleration}"
        else:
            return f"name: {self.name} action type:{self.action_type}"

    def get_name(self):
        return self.name

    def get_acceleration(self):
        return self.action_value 
    
    def get_value(self):
        return self.action_value 
    
    