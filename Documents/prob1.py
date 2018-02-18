class line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        pass

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1)/(x2-x1))


class Cylender(object):
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return(self.height*(3.24)*self.radius**2)
    def surface_area(self):
        top = (3.14)*(self.radius)**2
        return(2*top+2*3.14*self.radius*self.height)
       
 
coordinate1 = (3,2)
coordinate2 = (8,10)

li = line(coordinate1,coordinate2)
print(li.coor1)
print(li.coor2)
print(li.distance())
print(li.slope())

ci = Cylender(10,20)
print(ci.volume())
print(ci.surface_area())

