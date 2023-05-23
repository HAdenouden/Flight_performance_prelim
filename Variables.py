#Conversion Factors
Pa_kgm2 = 0.101971621
ft_m = 0.3048
kts_mps = 0.5144
kph_mps = 1 / 3.6
ftpm_mps = 0.00508

#Weight
g0 = 9.81 #gravitational acceleration [m/s^2]
DesignWeight = 32 * g0 #design gross weight [N]

#Cruise
h_cruise = 120 #cruise altitude [m]
V_cruise = 80*kph_mps #cruise speed [m/s]
#P_a_cruise = 1500 #power available during cruise [W]

#Climb performance (after VTOL part)
ROC = 3 #Rate of Climb [m/s]
V_climb = V_cruise * 0.8

#Turn performance
theta = 45 #bank angle [degree]

#Service Ceiling
h_service = 3150 #service ceiling [m]
V_max_service = 120 / kph_mps #maximum velocity at service ceiling [m/s]

#Approach and Landing
V_approach = 29.5 * kts_mps #approach speed [m/s]
margin_stall = 1.1 #stall reserve factor [-]
V_stall_approach = V_approach / margin_stall #stall speed in approach configuration [m/s]
CL_max_approach = 1.46 #maximum lift coefficient in approach configuration [-]
h_max_approach = 30 #maximum altitude to initialise approach [m]

#Basic Geometry and Initial Guesses
AR = 7 #aspect ratio [-]
CD_min = 0.0418 #minimum drag coefficient [-]
Cd0 = 0.03 #zero-lift drag coefficient [-]
WoS_max = 20 #maximum wing loading [kg/m^2]
TtW_max = 0.8 #maximum thrust-to-weight ratio [-]
P_max = 5 #maximum power available??? [W]
eta_prop = 0.85 #propeller efficiency [-]
#TOP_prop = 100 #take-off parameter [-]










