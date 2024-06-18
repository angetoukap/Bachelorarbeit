import Environment 
import json

counter = 0
KnapsackCapacity = 1.0
remainingCapacity = 0
updatecounter =0






def update_Capacity():
 global counter
 global remainingCapacity
 global KnapsackCapacity

 remainingCapacity = KnapsackCapacity*0.25

 return remainingCapacity
  



def visitState(State): 
 global counter
 global remainingCapacity
 global updatecounter

 if round(remainingCapacity,2) <=0.0 and updatecounter<=4:
  
  updatecounter+=1
  update_Capacity()
  


   

 if Environment.weights[State] <= remainingCapacity:
   counter +=1
   Environment.takeAction(1,State)
   remainingCapacity-=Environment.weights[State]
   
   
 else:
  counter +=1
  Environment.takeAction(0,State) 
  



for i in range(0,30):
 visitState(i)
Environment.getResults() 