class Wine(object):
    def __init__(self,verity,root,year):
        self.verity = verity
        self.root = root
        self.year = year

    def display_wine(self):
        print("verity is " + self.verity)
        print("root is " + self.root)
        print("age is " + str(self.year))

    def check_type(self):
       if self.verity == 'Zin':
           print("it is Zin")
       else:
           if self.verity == "Cab":
               print("it is Cab")
           else:
               print("it is Barbera")

w1 = Wine('Zin','R100',1999)
w1.display_wine()
w1.check_type()

   
           
