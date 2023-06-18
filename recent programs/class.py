class car:
    brand = ''
    model = ''
    capacity = '' #sm,md,l,xl
    color = ''
    powerSteering = True
    spareWheel = 0
    evoCertificate = False

    def setBrand(self,brandName):
        self.brand = brandName
        return self.brand

    def setModel(self,modelName):
        self.model = modelName
        return self.model
    
    def setCapacity(self,size):
        self.capacity = size
        return self.capacity
    
    def steering(self,power):
        self.powerSteering = power
        return self.powerSteering
    
    def paint(self,colour):
        self.color = colour
        return self.color
    
    def spareWheel(self,count):
        self.spareWheel = count
        return self.spareWheel
    
    def evoCertificate(self):
        if (self.capacity == 'l' or self.capacity == 'xl') and self.spareWheel > 1 and self.steering == True:
            self.evoCertificate = True
        return self.evoCertificate

mycar = car()
familyCar = car()

car.getBrand(mycar,'tesla')
car.getBrand(familyCar,'ford')

car.getModel(mycar,'tesla-y')
car.getModel(familyCar,'eco-sport')

car.getCapacity(mycar,'md')
car.getCapacity(familyCar,'l')

car.steering(mycar,True)
car.steering(familyCar,True)

car.paint(mycar,'grey')
car.paint(familyCar,'red')

car.spareWheel(mycar,1)
car.spareWheel(familyCar,2)

car.evoCertificate(mycar)
car.evoCertificate(familyCar)

