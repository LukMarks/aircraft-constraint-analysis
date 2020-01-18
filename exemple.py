# Author: Lucas Marques Moreno
# Date: 01/18/2020 
# description: Exemple for a 
# simple contraint analysis

import numpy as np
import matplotlib.pyplot as plt
from constraint_analysis import design_space

analysis = design_space()
interations = 1000 # number of interations
w_s_initial = 0.5 #[N/m²] initial W/S ratio
w_s_final = 50. #[N/m²] final W/S ratio
step = (w_s_final-w_s_initial)/interations

CD_min =0.0025 # minimun drag coefficent
k =0.2116 # lift-induced drag constant
n =10 # load factor
q =50 #[N/m²] dynamic pressure at selected speed and altitude


w_s = w_s_initial
W_S =[]
t_w_velocity_turn =[]


while w_s <= w_s_final:
    t_w_velocity_turn.append(analysis.constant_velocity_turn(w_s,CD_min,k,n,q))
    W_S.append(w_s)
    w_s +=step

plt.figure(1)
plt.plot(W_S,t_w_velocity_turn)
plt.fill_between(W_S,t_w_velocity_turn)

plt.show()