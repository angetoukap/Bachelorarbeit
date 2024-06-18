

import Environment
import statistics as st


counter = 0
saved_ratios = []
flexibleThreshold = 1
weights=[]
rewards=[]








def save_values(State):
  global weights
  global rewards
  weights.append(Environment.weights[State])
  rewards.append(Environment.rewards[State])
  return rewards, weights
def update_Threshold(State):
  global counter 
  counter +=1
 
  if Environment.id[State] == "State0":
   global flexibleThreshold
   flexibleThreshold =1
  else:
  
   global rewards
   global weights
   flexibleThreshold = (rewards[counter-2]/weights[counter-2])
  
  
  return flexibleThreshold





def visitState(State): 
 
 

 global counter 
 global saved_ratios

 update_Threshold(State)
 save_values(State)

 if Environment.rewards[State]/Environment.weights[State] >= flexibleThreshold:
   
   Environment.takeAction(1,State)
  
   
 else:

  Environment.takeAction(0,State) 
  



for i in range(0,30):
 Environment.presentState(i)
 visitState(i)
Environment.getResults() 