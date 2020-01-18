# Author: Lucas Marques Moreno
# Date: 01/18/2020 
# description: Group of function
# to define the design space

class design_space:
    def __init__(self):
        pass
        return

    def constant_velocity_turn(self): # T/W for a level constante-velocity turn
        # Variables:
        # CD_min: minimun drag coefficent
        # k: lift-induced drag constant
        # q[N/m²]: dynamic pressure at selected speed and altitude
        # S[m²] : wing area
        # T[N]: Thrust
        # W[N]: weight
        # n: load factor or 1/cos(psi), where psi is the bank angle

        aux1 = CD_min/w_s
        aux2 = k*(n/q)**2
        t_w = q*(aux1*aux2*w_s)
        return t_w
    
    def specifc_energy_level(self):# T/W for a select energy level
        # Variables:
        # Ps: specific energy level
        # V[m/s]: airspeed 

        t_w = constant_velocity_turn()+Ps/V
        return t_w

    def rate_of_climb(self): # T/W for a specific rate of climb
        # Variables:
        # CD_min: minimun drag coefficent
        # k: lift-induced drag constant
        # q[N/m²]: dynamic pressure at selected speed and altitude
        # S[m²] : wing area
        # T[N]: Thrust
        # W[N]: weight
        # n: load factor or 1/cos(psi), where psi is the bank angle
        # V[m/s]: airspeed
        # vertical_speed[m/s]: Vertical speed
        
        aux1 = Vertical_speed/V
        aux2 = (q/w_s)*CD_min
        aux3 = (k/q)*w_s

        t_w = aux1 + aux2 + aux3
        return t_w

    def takeoff_distance(self):
        pass
        return
    
    def cruise_airspeed(self):
        pass
        return
    def service_ceiling(self):
        pass
        return