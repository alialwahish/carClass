class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.tax=0.12

    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed 
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
        

bmw=Car(2000,"5mph","Full","15mpg")

        
bmw.display_all()