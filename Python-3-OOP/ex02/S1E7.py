from S1E9 import Character


class Baratheon(Character):
    """A class representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor of the Baratheon Class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    
    def die(self):
        """ """
        self.is_alive = False
        # return self.is_alive

    def __str__(self):
        """ """
        return f"the {self.family_name} family member named {self.first_name} with {self.eyes} eyes and {self.hairs} hair."

    def __repr__(self):
        return f"<Baratheon: {self.first_name}, Alive: {self.is_alive}>"
    

    


class Lannister(Character):
    """A class representing the Lannister family"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of the Lannister Class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    
    def die(self):
        """ """
        self.is_alive = False
        # return self.is_alive
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ """
        return cls(first_name, is_alive)
    
    def __str__(self):
        """ """
        return f"the {self.family_name} family member named {self.first_name} with {self.eyes} eyes and {self.hairs} hair."

    def __repr__(self):
        return f"<Lannister: {self.first_name}, Alive: {self.is_alive}>"
