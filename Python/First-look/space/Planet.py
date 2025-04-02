class Planet:
    shape = 'runde'

    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = int(radius)
        self.gravity = int(gravity)
        self.system = system

    def orbit(self):
        return f'og sirkler i {self.system}'

    def info(self):
        return f'{self.name} er en planet med radius {self.radius} og gravitasjon på {self.gravity}'

    @classmethod
    def commons(cls):
        return f'Alle planeter er {cls.shape} pga gravitasjonen'

    @staticmethod
    def spin(speed = '10000 kilometer i timen'):
        return f'Planeten spinner {speed}'