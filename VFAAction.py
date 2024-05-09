import numpy as np 
from sklearn.metrics import r2_score

Honey = {
"state1": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
},
"state2" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5)
 },
 "state3": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state4": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state5" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state6": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state7": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state8" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state9": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
"state10": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state11" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state12": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
"state13": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state14" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state15": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 }, 
 "state16": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state17" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state18": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state19": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state20" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state21": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state22": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state23" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state24": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state25": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state26" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state27": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 },
 "state28": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5) 
},
"state29" : {
"weights" : np.random.normal(0.5,0.5),
"values " : np.random.normal(0.5,0.5) 
 },
 "state30": {
"weights" : np.random.normal(0.5,0.5), 
"values " : np.random.normal(0.5,0.5)
 }}



values_state1 = np.array(list(Honey["state1"].values()))
values_state2 = np.array(list(Honey["state2"].values()))
values_state3 = np.array(list(Honey["state3"].values()))
values_state4 = np.array(list(Honey["state4"].values()))
values_state5 = np.array(list(Honey["state5"].values()))
values_state6 = np.array(list(Honey["state6"].values()))
values_state7 = np.array(list(Honey["state7"].values()))
values_state8 = np.array(list(Honey["state8"].values()))
values_state9 = np.array(list(Honey["state9"].values()))
values_state10 = np.array(list(Honey["state10"].values()))
joined_array = np.concatenate((values_state1,values_state2,values_state3,values_state4,values_state5,values_state6,values_state7,values_state8,values_state9,values_state10))

weights_array = np.empty(0)
rewards_array = np.empty(0)
print(joined_array)

i = 0
while i != 20:
 weights_array = np.append(weights_array,joined_array[i])
 i+=2

i=1
while i !=21:
 rewards_array = np.append(rewards_array,joined_array[i])
 i+=2

 

X = weights_array
Y = rewards_array

m =0
c =0
#Länge unser Daten 
n = len(X)

learning_rate =0.01
iter = 1000

for i in range(iter):
 y_pred = (m*X)+c

 mse =(1/n)*sum(np.square(y_pred -Y))
 mse_m = (1/n)*sum(X*(y_pred -Y))
 mse_c = (1/n)*sum(y_pred-Y)
 m = m - learning_rate *mse_m
 c = c -learning_rate*mse_c

accuracy = r2_score(Y,y_pred)
print("Das Bestimmtheitsmaß betraegt:",accuracy)
print("Die Steigung betraegt:",m)
print("Der Y-Achsenabschnit betraegt:",c)


KnapsackCapacity = 1
def updateCapacity(currentcapacity): 
  global KnapsackCapacity
  KnapsackCapacity = KnapsackCapacity- currentcapacity
  return KnapsackCapacity
Totalreward = 0
def updateReward(currentreward):
  global Totalreward
  Totalreward = Totalreward + currentreward
  return Totalreward

remainingCapacity = np.empty(0)


chosen_states = np.empty(0)


for i in Honey:

 if chosen_states.size == 0: 
  chosen_states = np.append(chosen_states,Honey[i])
  updateCapacity(Honey[i]["weights"])
  updateReward(Honey[i]["values "])
  remainingCapacity=np.append(remainingCapacity,KnapsackCapacity)
 
