#build the class
class Car:
    def __init__(self, make, model, rego, MaxRange):
        self.make = make
        self.model = model
        self.rego = rego
        self.MaxRange = MaxRange
        self.Range = MaxRange

    def GetDetails(self):
        return f"Make: {self.make}, Model: {self.model}, Rego: {self.rego}"

    def Travel(self, kms):
        self.Range -= kms

    def GetRange(self):
        return f"Current Range is {self.Range}kms"
    
class FuelType(Car):
    def __init__(self, make, model, rego, MaxRange, fuel):
        self.make = make
        self.model = model
        self.rego = rego
        self.MaxRange = MaxRange
        self.fuel = fuel    

c1 = Car("Holden", "Commodore", "ABC123", 600)
c1.GetDetails()
c1.Travel(200)
c1.GetRange()

#test
# print(c1.GetRange())
