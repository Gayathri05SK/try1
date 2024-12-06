import math
class calculator:
    def __init__(self , filepath):
        with open(filepath , 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith("WaferDiameter"):
                    self.wafer_diameter = float(line.split(":")[1])
                if line.strip().startswith("DieSize"):
                    die_width , die_height = line[8:].split("x")
                    self.die_width , self.die_height = int(die_width) , int(die_height)
                if line.strip().startswith("DieShiftVector"):
                    die_vector_1, die_vector_2  = line[16:19].split(",")
                    self.die_vector = [int(die_vector_1) , int(die_vector_2)]
                if line.strip().startswith("ReferenceDie"):
                    center_1 , center_2 = line[14:19].split(",")
                    self.center = [int(center_1) , int(center_2)]
            print(self.wafer_diameter , self.die_width , self.die_height , self.die_vector , self.center)
        self.calc()
        

    def ref_die_vec(self):
        return [(self.center[0]+self.die_vector[0] - self.die_height/2)+1   , (self.center[1]+self.die_vector[1] - (self.die_width/2))+1 ]

    def hypotenuse(self , llc):
        hypo = math.sqrt(pow(llc[0] ,2) + pow(llc[1],2))
        if hypo < self.wafer_diameter/2:
            return True
        else:
            return False


    def calc(self):
         with open("F:\KLA workshop\Workshop2024\Milestone2\\ans\\1.txt" , 'w') as w:
            llc_origin = self.ref_die_vec()
            die = [0,0]
            llc = llc_origin.copy()
            #Calculating the 1 space
            while llc[1] <=self.wafer_diameter/2:

                while llc[0] <= self.wafer_diameter/2:
                    w.write(f'{tuple(die)}:{tuple(llc)}\n')
                    llc[0] += self.die_width
                    die[0] +=1
                llc[0] = llc_origin[0]
                llc[1]+=self.die_height
                die[0] = 0
                die[1] +=1
            
            #Calulationg the 2 space
            llc[0] , llc[1]= llc_origin[0] - self.die_width , llc_origin[1]
            die[0] , die[1] = -1 , 0 
            while llc[1] <=self.wafer_diameter/2:

                while llc[0] >= -self.wafer_diameter/2:
                    

                    w.write(f'{tuple(die)}:{tuple(llc)}\n')
                    llc[0] -= self.die_width
                    die[0] -=1
                llc[0] = -self.die_height
                llc[1]+=self.die_height
                die[0] = -1
                die[1] +=1

            print(llc_origin)
            #Calculation the 3 space
            llc[0] , llc[1]= llc_origin[0] - self.die_width , llc_origin[0] - self.die_height
            die[0] , die[1] = -1 , -1
            while llc[1] >= -self.wafer_diameter/2:

                while llc[0] >= -self.wafer_diameter/2 :
                    

                    w.write(f'{tuple(die)}:{tuple(llc)}\n')
                    llc[0] -= self.die_width
                    die[0] -=1
                llc[0] = -self.die_height
                llc[1]-=self.die_height
                die[0] = -1
                die[1] -=1   

            #Calculation the 4 space
            print("LLc",llc_origin)
            llc[0] , llc[1]= llc_origin[0] , llc_origin[0] - self.die_height
            die[0] , die[1] = 0 , -1
            while llc[1] >= -self.wafer_diameter/2:

                while llc[0] <= self.wafer_diameter/2:
                    

                    w.write(f'{tuple(die)}:{tuple(llc)}\n')
                    llc[0] += self.die_width
                    die[0] +=1
                llc[0] = llc_origin[0]
                llc[1]-=self.die_height
                die[0] = 0
                die[1] -=1  


obj = calculator("F:\KLA workshop\Workshop2024\Milestone3\Input\Testcase1.txt")



