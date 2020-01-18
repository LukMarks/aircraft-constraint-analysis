# aircraft-constraint-analysis
Constraint analysis used in an early stage of aircraft's design
## Methodology
  This is one of the first steps taken in the aircraft design, it consist in a superpositon of differentes kinds of constraints, in this case, the next constraints were used to generete **Design Space's** plot:
  
  - Constant Velocity Turn;
  - Specific Energy Level;
  - Rate of Climbing;
  - Takeoff Distance;
  - Cruise Airspeed;
  - Service Ceiling.
 
## How To Use
  This method only needs the definition of the contraints, in the [exemple](https://github.com/LukMarks/aircraft-constraint-analysis/blob/master/exemple.py) file, the following section ilustrates how it might be done.
  ``` python
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
#=========================================================
  ```


## Result
![space_design](/image_src/space_design_exemple.png)
Once the **Design Space** is defined the initial values for **T/W** and **W/S** will also be difined, the configuration must seek the empty space above the curves. The optimal configuration lies between the edge of the blank space and the tangent ofconstraint lines.

