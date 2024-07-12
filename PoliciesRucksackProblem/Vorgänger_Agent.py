

import Environment
import statistics as st


flexibleThreshold =0 
weights=[]
rewards=[]
counter =0









def save_values(State):
  global weights
  global rewards
  weights.append(Environment.weights[State])
  rewards.append(Environment.rewards[State])
  return rewards, weights
def update_Threshold(State):
  counter=+1
 
  if Environment.id[State] == 0:
   global flexibleThreshold
   flexibleThreshold =0
  else:
  
   global rewards
   global weights
   flexibleThreshold = (rewards[counter-2]/weights[counter-2])
  
  return flexibleThreshold





def visitState(State): 
 
 

 

 update_Threshold(State)
 save_values(State)
 estimate =Environment.rewards[State]/Environment.weights[State] 
 if  estimate >= flexibleThreshold:
   
   Environment.takeAction(1,State)
  
   
 else:

  Environment.takeAction(0,State) 
  



for i in range(0,30):
#s Environment.presentState(i)
 visitState(i)
Environment.getResults() 
chosenStates = Environment.chosenStates