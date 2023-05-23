from math import *
import numpy as np
import scipy as sc
from Variables import *
from ambiance import Atmosphere
import matplotlib.pyplot as plt

h_sealevel = 0 #sea level altitude [m]
sealevel = Atmosphere(h_sealevel)
cruise = Atmosphere(h_cruise)
ceiling = Atmosphere(h_service)

#dynamic pressures
q_sea = 0.5 * sealevel.density * V_stall_approach**2
q_climb = 0.5 * sealevel.density * V_climb**2
q_cruise = 0.5 * cruise.density * V_cruise**2

#constants related to drag
e0 = 1.78*(1-0.045*AR**0.68)-0.64 #relation from "small unmanned fixed-wing a/c design: a practical approach
k = 1 / (np.pi * AR * e0) #drag polar coefficient
print("Approach speed: ", V_approach)
print("Stall speed at approach:", V_stall_approach)

#Ranges
dt = 0.01
WoS_range_kgm2 = np.arange(dt, WoS_max, dt)
WoS_range_Pa = WoS_range_kgm2 / Pa_kgm2
TtW_range = np.arange(dt, TtW_max, dt)
P_range_kW = np.arange(dt, P_max, dt)
PoW_range_kW = P_range_kW / DesignWeight


##################### THIS IS ALL THRUST-TO-WEIGHT RELATIONS #####################

#Sustained Turn (turn)
#n = 1/np.cos(theta/180*np.pi)
#TtW_turn = q_cruise * ( CD_min/WoS_range + k * (n/q_cruise)**2 * WoS_range)
#TtW_turn = q_sea * (CD_min/WoS_range + k * (n/q_cruise)**2 * WoS_range)

#Rate of Climb (ROC)
#TtW_ROC = ROC / V_cruise + (q_climb * CD_min)/WoS_range + (k * WoS_range)/q_climb
#TtW_ROC = ROC / V_climb + (q_sea*Cd0)/WoS_range + (k*WoS_range)/q_climb

#Cruise speed (cruise)
#TtW_cruise = (q_cruise * CD_min)/WoS_range + (k*WoS_range)/q_cruise
#TtW_cruise = (q_cruise * CD_min)/WoS_range + (k*WoS_range)/q_cruise

#Maximum Ceiling (hmax) = maximum altitude with
#minimum speed to maintain altitude, thus L=W
#V_stall_max = V_stall_approach * sealevel.density / service.density
#q_service = 0.5 * service.density * V_stall_max**2
#WoS_hmax = np.ones(len(TtW_range)) * q_service * np.sqrt(np.pi * AR * e0 * Cd0)
#print(V_stall_max, q_service)

#Endurance (end)
#WoS_end = np.ones(len(TtW_range)) * q_cruise * np.sqrt(3 * np.pi * AR * e0 * Cd0)


#plotting stuff
# plt.plot(WoS_range, TtW_turn)
# plt.plot(WoS_range, TtW_ROC)
# plt.plot(WoS_range, TtW_cruise)
# plt.plot(WoS_hmax, TtW_range)
# plt.plot(WoS_end, TtW_range)
# plt.xlim(0, WoS_max)
# plt.xlabel("W/S [N/m^2]")
# plt.ylim(0, TtW_max)
# plt.ylabel("P/W [N/W]")
# plt.show()



##################### THIS IS ALL POWER-TO-WEIGHT RELATIONS #####################

#Stall landing configuration
#WS_stall0 = np.ones(len(P_range)) * q_sea * CL_max_approach / 9.81

#Take-off performance (TO)
#PtW_TO = 1 / TOP_prop * WoS_range / CL_TO / sigma

#Cruise (cruise)
#PtW_TO_cruise = eta_prop * (sealevel.density / cruise.density)**(-0.75) * ( Cd0*q_cruise*V_cruise/WoS_range + k*WoS_range*V_cruise/q_cruise )**(-1)
#PtW_cruise =  eta_prop * ( Cd0*q_cruise*V_cruise/WoS_range + k*WoS_range*V_cruise/q_cruise )**(-1)

#Level turn (turn)
rho_correction_turn = (sealevel.density / cruise.density) ** 0.75
n = 1/np.cos(theta/180*np.pi)
TtW_turn = q_cruise * (CD_min / WoS_range_Pa + WoS_range_Pa * k * (n/q_cruise)**2)
PoW_turn_kW = TtW_turn * V_cruise / eta_prop * rho_correction_turn / 1000
P_turn_kW = PoW_turn_kW * DesignWeight
#P_turn_kW = TtW_turn * DesignWeight * V_cruise / eta_prop * rho_correction_turn / 1000

#Rate of Climb (ROC)
rho_correction_ROC = (sealevel.density / sealevel.density) ** 0.75
TtW_ROC = ROC / V_climb + CD_min * q_climb / WoS_range_Pa + k * WoS_range_Pa / q_climb
PoW_ROC_kW = TtW_ROC * V_climb / eta_prop * rho_correction_ROC / 1000
P_ROC_kW = PoW_ROC_kW * DesignWeight
#P_ROC_kW = TtW_ROC * DesignWeight * V_climb / eta_prop * rho_correction_ROC / 1000

#Cruise (cruise)
rho_correction_cruise = (sealevel.density / cruise.density) ** 0.75
TtW_cruise = q_cruise * CD_min / WoS_range_Pa + k / q_cruise * WoS_range_Pa
PoW_cruise_kW = TtW_cruise * V_cruise / eta_prop * rho_correction_cruise / 1000
P_cruise_kW = PoW_cruise_kW * DesignWeight
#P_cruise_kW = TtW_cruise * DesignWeight * V_cruise / eta_prop * rho_correction_cruise / 1000

#Maximum Ceiling (MC)
V_stall_MC = V_stall_approach * sealevel.density / ceiling.density
WoS_MC_Pa = 0.5 * cruise.density * V_stall_MC**2 * np.sqrt(np.pi * AR * e0 * Cd0)
WoS_MC_kgm2 = WoS_MC_Pa * Pa_kgm2
print(V_stall_MC, AR, e0, Cd0)

#Endurance (end)
V_stall_end = V_stall_approach * sealevel.density / ceiling.density
WoS_end_Pa = 0.5 * cruise.density * V_stall_end**2 * np.sqrt(3 * np.pi * AR * e0 * Cd0)
WoS_end_kgm2 = WoS_end_Pa * Pa_kgm2
print(V_stall_end)

#Approach speed (app)
WoS_app_Pa = q_sea * CL_max_approach
WoS_app_kgm2 = WoS_app_Pa * Pa_kgm2
print(CL_max_approach)




#define the graphs
plt.subplot(1, 2, 1)
plt.axvspan(WoS_MC_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.axvspan(WoS_end_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.axvspan(WoS_app_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, PoW_turn_kW, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, PoW_ROC_kW, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, PoW_cruise_kW, alpha=0.3, color="blue")
plt.title("Power over Weight")
plt.xlim(0, WoS_max)
plt.xlabel("W/S [kg/m^2]")
plt.ylim(0, P_max / DesignWeight)
plt.ylabel("P/W [kW/N]")
plt.subplot(1, 2, 2)
plt.axvspan(WoS_MC_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.axvspan(WoS_end_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.axvspan(WoS_app_kgm2[0], WoS_max+1, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, P_turn_kW, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, P_ROC_kW, alpha=0.3, color="blue")
plt.fill_between(WoS_range_kgm2, P_cruise_kW, alpha=0.3, color="blue")
plt.title("Power for Design Weight")
plt.xlim(0, WoS_max)
plt.xlabel("W/S [kg/m^2]")
plt.ylim(0, P_max)
plt.ylabel("P [kW]")

plt.show()

