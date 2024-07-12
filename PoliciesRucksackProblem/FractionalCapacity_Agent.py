import Environment 
import json

counter = 0
remainingCapacity = 0
updatecounter =0





 #Ruckkapazität wird in vier Teilkapazitäten geteilt
def update_Capacity():
 global counter
 global remainingCapacity
 global KnapsackCapacity

 remainingCapacity = Environment.KnapsackCapacity*0.25

 return remainingCapacity
  



def visitState(State): 
 global counter
 global remainingCapacity
 global updatecounter

#Rucksackkapazität wird neu defineirt
 if round(remainingCapacity,2) <=0.0 and updatecounter<=4:
  
  updatecounter+=1
  update_Capacity()
  


   
 #Prüfen, ob das Gewicht des Zustandes  kleiner als die Kapazität ist
 if Environment.weights[State] <= remainingCapacity:
   counter +=1
   Environment.takeAction(1,State) # Zustand akzeptieren
   remainingCapacity-=Environment.weights[State] #Kapazität wird verringert
   
   
 else:
  counter +=1
  Environment.takeAction(0,State)  # Zustand ablehnen
  



for i in range(0,30):
 visitState(i)
Environment.getResults() 