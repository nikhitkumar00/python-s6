class poly:
    def sum(self, a = None, b = None):
        if a!=None and b!=None:
            print("Rectangle : ",a*b)
        elif(a!= None):
            print("Square : ",a**2)
        else:
            print("NONEEE")

A = poly()
A.sum()
A.sum(2)
A.sum(2,3)