import math
import numpy as np
import constants as cons
import isa
import matplotlib.pyplot as plt
import generalCalc as gC

"""for ws in range(500, 7000, 500):
    q = 0.5*isa.isa_model(0,0)[2]*gC.v_TO(ws)[2]**2
    gC.calcFactorK(cons.e_TO)
    #k_OEI = 1/(np.pi*cons.AR+cons.e_TO)
    gC.calcParasiticDrag(cons.c_Lmax_Start,cons.e_TO)
    #c_D_TO = cons.c_Lmax_Start*cons.epsilon_TO-k_OEI*cons.c_Lmax_Start**2
    epstein = gC.calcEpsilon(q,ws,cons.c_Lmax_Start,cons.e_TO)
    #epstein = q*c_D_TO/ws+k_OEI*ws/q
    print(1/epstein)

print(calcVCruise(cons.H_CRUISE,0))"""
ws = 5000
AR = 10
e_0_to = 0.7
c_lto = 2
eps = 1/10
v=math.sqrt(2*ws/(isa.isa_model(0,0)[2]*c_lto))
q = 0.5*isa.isa_model(0,0)[2]*v*v
k = 1/(3.141*AR*e_0_to)
cd_0 = eps*c_lto-k*c_lto**2
epsilon = q*cd_0/ws+k*ws/q
print(v,1/epsilon)

#########################################################################


def P_W_RollingDistance(W_S, s1):
        T_W = 1.15*W_S/(isa.g0*isa.isa_model(cons.h_TO,cons.dT_TO)[2]*s1*(1-1/(2*cons.N_E))*(1-cons.u_roll-cons.u_aero))
        return round(T_W*0.71*gC.v_TO(W_S)[1]/(cons.TRthr_TO*cons.ntrans*cons.n_prop_TO),2)

def P_W_ClimbingDistance(W_S, s3):
        #q_OEI = 0.5*isa.isa_model(cons.h_TO,cons.dT_TO)[2]*gC.v_TO(W_S)[2]**2
        #k_OEI = 1/(np.pi*cons.AR+cons.e_TO)
        #k_OEI = gC.calcFactorK(cons.e_TO)
        #c_D_TO = cons.c_Lmax_Start*cons.epsilon_TO-1/(np.pi*cons.AR*cons.e_TO)*cons.c_Lmax_Start**2
        #c_D_TO = gC.calcParasiticDrag(cons.c_Lmax_Start,cons.e_TO)
        #e_TO_OEI = q_OEI * c_D_TO / W_S + k_OEI * W_S / q_OEI
        e_TO_OEI = eps
        T_W = (math.sin(math.atan(cons.h_scr/s3))+e_TO_OEI)/(1-1/cons.N_E)
        return round(T_W*0.5*(gC.v_TO(W_S)[1]+gC.v_TO(W_S)[2])/(cons.TRthr_TO*cons.ntrans*cons.n_prop_TOCl),2)

def takeOff_pw_ws(W_S):
        datenpunkte = 200
        disList = []
        rollDisList = []
        climDisList = []
        diffList = []

        for i in range (0, datenpunkte-1):
                s = 2200/datenpunkte*(i+1)
                disList.append(s)
                rollDisList.append(P_W_RollingDistance(W_S,s))
                climDisList.append(P_W_ClimbingDistance(W_S,2200-s))
                diffList.append(round(abs(P_W_RollingDistance(W_S,s)-P_W_ClimbingDistance(W_S,2200-s)),2))

        indexmin = diffList.index(min(diffList)) #Gibt Listenindex mit kleinstem Wert aus

        #print(indexmin)
        #print(rollDisList[indexmin])
        #print(climDisList[indexmin])
        #print(disList[indexmin])

        return rollDisList[indexmin]*cons.pwsafetyfactor

#################################### T E S T ###########################################
xlist =[]
ylist=[]

for w_s in range (500, 8000, 500):
        xlist.append(w_s)
        ylist.append(takeOff_pw_ws(w_s))

x = np.array(xlist)
y1 = np.array(ylist)
#y2 = np.array(climDisList)
#y3 = np.array(diffList)
#plt.ylim([0, 100])
plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
plt.show()