# Author: Lucas Marques Moreno
# Date: 01/18/2020 
# description: Group of function
# to define the design space

class design_space:
    def __init__(self):
        pass
        return

    def constant_velocity_turn(self,w_s,CD_min,k,n,q): # T/W for a level constante-velocity turn
        # Variables:
        # CD_min: minimun drag coefficent
        # k: lift-induced drag constant
        # q[N/m²]: dynamic pressure at selected speed and altitude
        # S[m²] : wing area
        # T[N]: Thrust
        # W[N]: weight
        # n: load factor or 1/cos(psi), where psi is the bank angle
        # w_s[N/m²]: weight and area wing ration(W/S)

        aux1 = CD_min/w_s
        aux2 = k*(n/q)**2
        t_w = q*(aux1*aux2*w_s)
        return t_w
    
    def specifc_energy_level(self,w_s,CD_min,k,n,q,Ps,V):# T/W for a select energy level
        # Variables:
        # Ps: specific energy level
        # V[m/s]: airspeed

        t_w = self.constant_velocity_turn(w_s,CD_min,k,n,q)+Ps/V
        return t_w

    def rate_of_climb(self,w_s,CD_min,k,q,Vertical_speed,V): # T/W for a specific rate of climb
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
        # w_s[N/m²]: weight and area wing ration(W/S)
        
        aux1 = Vertical_speed/V
        aux2 = (q/w_s)*CD_min
        aux3 = (k/q)*w_s

        t_w = aux1 + aux2 + aux3
        return t_w

    def takeoff_distance(self,w_s,q,CL_to,CD_to,Sg,V_lof,mi = 0.05,g = 9.81): # T/W for a specific ground run distance
        # Variables:
        # CL_to: lift coefficient during the takeoff
        # CD_to: drag coefficient during the takeoff
        # q[N/m²]: dynamic pressure
        # Sg[m]: ground run
        # V_lof[m/s]: liftoff speed
        # mi: ground friction constant
        # g[m/s²]: acceleration due the gravity
        # w_s[N/m²]: weight and area wing ration(W/S)

        aux1 = V_lof**2/(2*g*Sg)
        aux2 = (q*CD_to)/w_s
        aux3 = (q*CL_to)/w_s

        t_w = aux1 + aux2 + mi*(1 - aux3)
        return t_w
    
    def cruise_airspeed(self,w_s,CD_min,k,q): # T/W for the cruise airspeed
        # Variables:
        # CD_min: minimun drag coefficent
        # k: lift-induced drag constant
        # q[N/m²]: dynamic pressure at selected speed and altitude
        # S[m²] : wing area
        # T[N]: Thrust
        # W[N]: weight
        # w_s[N/m²]: weight and area wing ration(W/S)
        aux1 = q*CD_min*(1/w_s)
        aux2 = k*(1/q)*w_s
        t_w = aux1+aux2
        return t_w

    def service_ceiling(self,w_s,k,CD_min,vertical_speed,p = 1.225): # T/W for a specific rate of climb
        # Variables:
        # CD_min: minimun drag coefficent
        # k: lift-induced drag constant
        # S[m²] : wing area
        # T[N]: Thrust
        # W[N]: weight
        # vertical_speed[m/s]: Vertical speed
        # p[kg/m³]: specifc mass of the air
        # w_s[N/m²]: weight and area wing ration(W/S) 

        aux1 = (k/(3*CD_min))**(1/2)
        aux2 = ((2/p)*w_s*aux1)**(1/2)
        aux3 = (k*CD_min/3)**(1/2)
        t_w = vertical_speed/aux2 + 4 * aux3 
        return t_w

    def cl_max_to_stall(self, w_s, v_stall, p = 1.225):
        # Variables:
        # v_stall[m/s]: stall speed
        # p[kg/m³]: specifc mass of the air
        # w_s[N/m²]: weight and area wing ration(W/S) 
        q_stall = (p*v_stall**2)/2 #dynamic pression for stall conditions
        cl_max = w_s/q_stall
        
        return cl_max