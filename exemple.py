# Author: Lucas Marques Moreno
# Date: 01/18/2020 
# description: Exemple for a 
# simple contraint analysis

import numpy as np
import matplotlib.pyplot as plt
from constraint_analysis import design_space




#air properties
#==========================================================
g = 9.81#[m/s²] gravity 
p = 1.2 #[kg/m³] air mass specific
#==========================================================

analysis = design_space()

#set up analysis
#==========================================================
interations = 10 # number of interations
w_s_initial = 10 #[N/m²] initial W/S ratio
w_s_final = 60 #[N/m²] final W/S ratio
step = (w_s_final-w_s_initial)/interations
#==========================================================

# constraits
#==========================================================
V_cruise = 20 #[m/s] cruise flight speed
CDo = 0.022#[]parasite drag coefficient
CD_min =0.0025 # minimun drag coefficent
k = 0.0535 # lift-induced drag constant
n = 2# load factor
q = (p*V_cruise**2)/2 #[N/m² or Pa] dynamic pressure at selected speed and altitude
Ps = 1 # specific energy level
V = V_cruise #[m/s] airspeed
Vertical_speed = 10 #[m/s] climb speed
CL_to = 1.3 # Lift coefficient at takeoff
CD_to = CDo + k*CL_to**2 # Drag coefficient at takeoff
Sg = 100# [m] maximum ground run distance
V_lof = 10 #[m/s] speed at takeoff
stall_speed = [1,5,10,15]
#=========================================================

# list for calculations
#=========================================================
w_s = w_s_initial
W_S =[]
t_w_velocity_turn =[]
t_w_specifc_energy_level=[]
t_w_rate_climb = []
t_w_takeoff = []
t_w_cruise = []
t_w_service_ceiling = []
stall_isoline_1 = []
stall_isoline_5 = []
stall_isoline_10 = []
stall_isoline_15 = []
#=========================================================
while w_s <= w_s_final:
    
    t_w_velocity_turn.append(analysis.constant_velocity_turn(w_s,CD_min,k,n,q))

    t_w_specifc_energy_level.append(analysis.specifc_energy_level(w_s,CD_min,k,n,q,Ps,V))

    t_w_rate_climb.append(analysis.rate_of_climb(w_s,CD_min,k,q,Vertical_speed,V))

    t_w_takeoff.append(analysis.takeoff_distance(w_s,q,CL_to,CD_to,Sg,V_lof))

    t_w_cruise.append(analysis.cruise_airspeed(w_s,CD_min,k,q))

    t_w_service_ceiling.append(analysis.service_ceiling(w_s,k,CD_min,Vertical_speed)) 

    stall_isoline_1.append(analysis.cl_max_to_stall(w_s, 1))
    stall_isoline_5.append(analysis.cl_max_to_stall(w_s, 5))
    stall_isoline_10.append(analysis.cl_max_to_stall(w_s, 10))
    stall_isoline_15.append(analysis.cl_max_to_stall(w_s, 15))

    W_S.append(w_s)
    w_s +=step


#plt.figure(1)
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()


ax1.set_xlabel('W/S',size=14)
ax1.set_ylabel('T/W',size=14)
ax2.set_ylabel('Required Cl_max')
#ax1.title('Design Space',size=18)

ax1.plot(W_S,t_w_velocity_turn, label='Velocity Turn')


ax1.plot(W_S,t_w_specifc_energy_level,label='Specific Energy \nLevel')


ax1.plot(W_S,t_w_rate_climb,label='Rate Of Climb')

ax1.plot(W_S,t_w_takeoff,label='Takeoff')

ax1.plot(W_S,t_w_cruise,label='Cruise Speed')

ax1.plot(W_S,t_w_service_ceiling,label='Ceiling Service')

ax2.plot(W_S,stall_isoline_1, '--', label='Stall Isolines 1 m/s')
ax2.plot(W_S,stall_isoline_5,'--',label='Stall Isolines 5 m/s')
ax2.plot(W_S,stall_isoline_10,'--',label='Stall Isolines 10 m/s')
ax2.plot(W_S,stall_isoline_15,'--',label='Stall Isolines 15 m/s')

#plt.xlabel('W/S',size=14)
#plt.ylabel('T/W',size=14)
ax1.legend(bbox_to_anchor=(1.15, 1), loc=2, borderaxespad=0.)
ax1.grid()
ax2.legend(bbox_to_anchor=(1.15, 0.5), loc=2, borderaxespad=0.)
ax2.grid()

plt.show()