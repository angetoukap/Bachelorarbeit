
import matplotlib.pyplot as plt
import numpy as np 

# Plotten welche States von den Policies ausgewählt wurden


xwerte= np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
chosenStates_vfa = np.array([ 0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,0])
chosenStates_gre = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
chosenStates_ap = np.array([1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0])
chosenStates_cbp = np.array([1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
policies = np.array([chosenStates_vfa,chosenStates_gre,chosenStates_ap,chosenStates_cbp])

#plt.bar(xwerte,chosenStates_vfa, color = 'r',label = 'VFA')
#plt.bar(xwerte,chosenStates_gre, color = 'g',label = 'Greedy')
#plt.bar(xwerte,chosenStates_ap, color = 'dimgrey',label = 'Adaptive')
#plt.bar(xwerte,chosenStates_cbp, color = 'blue',label = 'Vorgänger')
#plt.title( ' Vorgänger (aufsteigende Reihenfolge)')

plt.ylabel('Aktion')
plt.xlabel('Zustand')

plt.show()
