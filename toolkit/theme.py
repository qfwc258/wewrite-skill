# Theme

class Theme:
    def __init__(self, name='xiaochchen'):
        self.name = name
        self.config = {}
    
    def load(self):
        return self.config