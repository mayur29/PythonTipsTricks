class Cook(object):
    def Preparedish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()
        self.boiler = Boiler()
        self.boiler.workingBoiler()
        self.friers = friers()
        self.friers.vegieFries()


class Cutter(object):
    def cutVegetables():
        print('All vegetables are cut')

class Boiler(object):
    def workingBoiler():
        print('Boiler is working')


class friers(object):
    def vegieFries():
        print('All vegetables are frying')



if __name__ == 'main':
    cook = Cook()
    cook.Preparedish()