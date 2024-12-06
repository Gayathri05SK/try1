import math
import numpy as np

class calculator:
    def __init__(self,filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
                if line.strip().startswith("WaferDiameter"):
                    diameter = line[14:]
                if line.strip().startswith("NumberOfPoints"):
                    n = line[15:]
                if line.strip().startswith("Angle"):
                    deg = line[6:]
        self.diameter = int(diameter)
        self.n = int(n)
        self.deg = int(deg)
        print(int(diameter) , int(n) , int(deg))
        self.calculator()


    def distance_between(self):
        start_point = np.array([0,0])
        end_point = np.array([self.diameter/2 , 0])
        step_vector = (end_point - start_point) / (self.n - 1)
        return step_vector


     

    def find_coordinated(self , distance , deg):
        x = (distance)*math.cos(math.radians(deg))
        y = (distance)*math.sin(math.radians(deg))
        return (x , y)


    def calculator(self):
        dis = self.distance_between()
        distancs = dis
        print(dis)
        with open("C:/Users/ADMIN/Downloads/KLA workshop/KLA workshop/Workshop2024/Milestone1/ans/4.txt" , 'w') as w:
            for i in range(int(self.n)):
                x, y = self.find_coordinated(dis , self.deg)
                print((x[0],y[0]))
                print((-x[0],-y[0]))
                w.write(f'({str(x[0])},{str(y[0])})\n')
                w.write(f'({str(-x[0])},{str(-y[0])})\n')
                dis = dis + distancs

testcase = calculator("C:/Users/ADMIN/Downloads/KLA workshop/KLA workshop/Workshop2024/Milestone1/Input/Testcase4.txt")