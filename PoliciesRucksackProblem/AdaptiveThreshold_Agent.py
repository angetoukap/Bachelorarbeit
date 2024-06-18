import numpy as np
import Environment
import statistics as st



counter =0.0
saved_ratios = []





flexibleThreshold = 0

def reduce_Threshold(saved_ratios):

  global flexibleThreshold
 
  flexibleThreshold = st.mean(saved_ratios)*0.2
  
  return flexibleThreshold

def increase_Threshold(saved_ratios):
   
   global flexibleThreshold
   flexibleThreshold = st.mean(saved_ratios)/0.2

   return flexibleThreshold



def visitState(State): 

 global counter 
 global saved_ratios

 if counter !=0 and counter%6==0: 
  if Environment.KnapsackCapacity >= 1.0-(0.2*(counter/6)):
    reduce_Threshold(saved_ratios)

  else:
     increase_Threshold(saved_ratios)

 if Environment.rewards[State]/Environment.weights[State] >= flexibleThreshold:
   counter +=1
   Environment.takeAction(1,State)
   saved_ratios.append(Environment.rewards[State]/Environment.weights[State])
   
 else:
  counter +=1
  Environment.takeAction(0,State) 
  saved_ratios.append(Environment.rewards[State]/Environment.weights[State])



for i in range(0,30):
 Environment.presentState(i)
 visitState(i)
Environment.getResults() 
  
 