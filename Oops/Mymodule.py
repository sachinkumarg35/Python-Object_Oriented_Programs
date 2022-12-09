"""
Car Class
"""

class Cab:
    
    #Initialise for first iteration.
    numberofcabs = 0
    
    def __init__(self, driver, kms, pay):
        self.driver = driver
        self.running = kms
        self.bill = pay
        Cab.numberofcabs = Cab.numberofcabs + 1
        
    #Returns average price per km
    def rateperkm(self):
        return self.bill/self.running
    
    #Return number of cabs running
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs
    
    if __name__ == "__main__":
        
        #Cab class
        firstcab = Cab("Ramesh", 80, 1200)
        
        #Driver attribute in cab class
        print(firstcab.driver)
        
        #class method
        print(Cab.noofcabs())