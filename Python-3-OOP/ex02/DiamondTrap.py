from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing the King, inheriting from Baratheon and Lannister."""
    def __init__(self, first_name, is_alive=True):
        """ """
        super().__init__(first_name, is_alive)
    
    def die(self):
        """ """
        self.is_alive = False

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value


    def get_eyes(self):
        return self._eyes

    def get_hairs(self):
        return self._hairs
    
    def set_hairs(self, value):
        self._hairs = value
    
    def set_eyes(self, color):
        self._eyes = color
    
