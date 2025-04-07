from DescentEvent import DescentEvent


class OnBoardComputer:

    def __init__(self,descent): ############ i added
        self.descent = descent
    
    def get_next_burn(self, status):
        # burn = 0
        # print(burn)  # hack!
        # return burn
        altitude = self.descent.get_altitude()
        fuel = self.descent.get_fuel()
        speed = self.descent.get_velocity()

        adjust_point = self.descent.get_altitude() % 100

        burn_list = [100]
       
        
        if altitude > 6000:
            burn_list.append(100)
            print(100)
            return 100
        elif altitude > 1000 and speed > 100:
            burn_list.append(200)
            print(200)
            return 200
        elif altitude > 200 and speed == 100:
            burn_list.append(100)
            print(100)
            return 100
        elif altitude > 200 and adjust_point != 0:
            v = (speed + 100) - adjust_point
            burn_list.append(v)
            print(v)
            return v
        elif altitude > 50 and speed > 25:
            v = (speed + 100) - 25
            burn_list.append(v)
            print(v)
            return v
        # forgetting to use 100 to hold
        elif 10 < altitude < 50 and speed > 2:
            v = (speed + 100) - 25
            burn_list.append(v)
            print(v)
            return v
        else:
            print(burn_list[-1])
            return burn_list[-1]

    
    ##############################################################################################
    """
        this is where my changes start
    
    """
    
    # def generate_burn(self):
        
    #     altitude = self.descent.get_altitude()
    #     fuel = self.descent.get_fuel()
    #     speed = self.descent.get_velocity()

    #     burn_list = []
    #     if altitude > 5000:
    #         burn_list.append(100)
    #         print(100)
    #         return 100
    #     elif speed > 100:
    #         burn_list.append(200)
    #         print(200)
    #         return 200
    #     else:
    #         return burn_list[-1]

    #def get_burn(self, status):

    


  