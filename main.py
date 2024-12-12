from Take_Off_Distance import takeOff_pw_ws
from isa import isa_model
from Landing_Distance import getLandingDistance
from WS_Max import getWS_Max
from cruise import calcPowerToWeightCruiseBaseOEI, calcPowerToWeightCruiseBase

from Climb_OEI_V1 import Climb_OEI_Out
#import Climb OEI

from Climb_service_V1 import Clim_Serv_out

import constants
import matplotlib.pyplot as plt
import numpy as np


#Values Landing




#plotting
x_max = 7000

Values_Climb_OEI = []
Values_calcPowerToWeightCruiseBaseOEI = []
Values_calcPowerToWeightCruiseBase = []
Values_TO = []
WS_Max_Landing = []

#x = range(0,x_max,10)
WS_Values = np.linspace(100,x_max,100)



for i in WS_Values:
    Values_Climb_OEI.append(Climb_OEI_Out(i))
    Values_calcPowerToWeightCruiseBaseOEI.append(calcPowerToWeightCruiseBaseOEI(i))
    Values_calcPowerToWeightCruiseBase.append(calcPowerToWeightCruiseBase(i))
    Values_TO.append(takeOff_pw_ws(i))



x = WS_Values
plt.axvline(x = getWS_Max(), color='tab:grey', label='W/S Max')
plt.axvline(x = getLandingDistance(), color='tab:red', label='Landing Distance')
plt.axvline(x = Clim_Serv_out(), color='tab:green', label='Service Ceiling')
plt.plot(x, Values_Climb_OEI, color='tab:olive', label='Climb OEI')
plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI, color='tab:cyan', label='Cruise OEI')
plt.plot(x, Values_calcPowerToWeightCruiseBase, color='tab:purple', label='Cruise')

plt.plot(x, Values_TO, color='tab:pink', label='Take-off')
plt.xlim([0, x_max])
plt.ylim([0, 100])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.legend()
plt.show()



