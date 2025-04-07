from DescentEvent import DescentEvent


class OnBoardComputer:

    def __init__(self,descent): ############ i added
        self.descent = descent
    
    def get_next_burn(self, status):
        burn = 0
        print(burn)  # hack!
        return burn
    
    ##############################################################################################
    """
        this is where my changes start
    
    """
    
    def generate_burn_list(self):
        
        altitude = self.descent.get_altitude()
        fuel = self.descent.get_fuel()
        speed = self.descent.get_velocity()

        burn_list = []
        if altitude > 5000:
            burn_list.append(100)
        elif speed > 100:
            burn_list.append(200)
        pass
    


  