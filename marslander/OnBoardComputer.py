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

        burn_list = []
        if altitude > 5000:
            burn_list.append(100)
            print(100)
            return 100
        elif speed > 100:
            burn_list.append(200)
            print(200)
            return 200
        else:
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

    


  