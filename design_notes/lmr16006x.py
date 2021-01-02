import numpy as np

V_in_max = 26
V_out = 5
F_sw = 700e3
I_out = 0.3
K_ind = 0.4     # ripple factor, 0.1 means 20mA when i_out is 0.2A.

L_o_min = (V_in_max - V_out) / (I_out * K_ind) * V_out / (V_in_max * F_sw)
print("Minimum Inductance: " + str(L_o_min * 1e6) + " [uH]")
L_o = 47e-6
print("Selected Inductance: " + str(L_o * 1e6) + " [uH]")
I_ripple = V_out * (V_in_max - V_out) / (V_in_max * L_o * F_sw)
print("Inductor Current Ripple: " + str(I_ripple * 1e3) + " [mA]")
I_L_RMS = np.sqrt(np.power(I_out, 2) + 1/12 * np.power(I_ripple, 2))
print("RMS Inductor Current: " + str(I_L_RMS * 1e3) + " [mA]")
I_L_peak = I_out + I_ripple/2
print("Peak Inductor Current: " + str(I_L_peak * 1e3) + " [mA]")

Delta_I_out = I_out * 0.5
Delta_V_out = 0.1

C_o_min_1 = 2 * Delta_I_out / (F_sw * Delta_V_out)
print("Minimum Capacitance 1: " + str(C_o_min_1 * 1e6) + " [uF]")
C_o_min_2 = L_o * ((np.power(I_out, 2) - np.power(I_out*0.5, 2)) 
    / (np.power(V_out+0.2, 2) - np.power(V_out, 2)))
print("Minimum Capacitance 2: " + str(C_o_min_2 * 1e6) + " [uF]")
C_o_min_3 = 1/(8 * F_sw) * I_ripple / 0.1
print("Minimum Capacitance 3: " + str(C_o_min_3 * 1e6) + " [uF]")
ESR_o_min = 0.1 / I_ripple
print("Minimum ESR: " + str(ESR_o_min * 1e3) + " [mOhm]")

