import numpy as np
import Environment
import statistics as st



counter =0   # gibt die Nummer des States an
saved_ratios = []  # speichert die Kosten-Nutzen-Verhältnis aller States 
extraCapacity =0  # übrig gebliebene Kapazität 
flexibleThreshold = 0 # Schwellenindex 


   
 # Reduktion des Schwellenindexes 
def reduce_Threshold(saved_ratios):

  global flexibleThreshold
  global counter
  flexibleThreshold = st.mean(saved_ratios)*0.0667
  
  return flexibleThreshold

# Erhöhung des Schwellenindexes
def increase_Threshold(saved_ratios):
   
   global flexibleThreshold
  
   flexibleThreshold = st.mean(saved_ratios)*1.0667

   return flexibleThreshold


# trifft eine Entscheidung bezüglich des vorgestellten States
def visitState(State): 

 global counter 
 global saved_ratios
 global extraCapacity
  
 # falls die Rucksackkapazität des Bereiches nicht aufgebraucht
 if counter!=0 and counter%2==0 and  Environment.KnapsackCapacity <= (Environment.KnapsackCapacity-Environment.KnapsackCapacity*(0.0667*(counter/2)))+extraCapacity: 
   extraCapacity = Environment.KnapsackCapacity-Environment.KnapsackCapacity*(0.0667*(counter/2))
   reduce_Threshold(saved_ratios)
 #falls  die Rucksackkapazität des Bereiches überstritten wurde
 elif counter!=0 and counter%2==0 and Environment.KnapsackCapacity > Environment.KnapsackCapacity-Environment.KnapsackCapacity*(0.0667*(counter/2)) :
     increase_Threshold(saved_ratios)
 
 # Prüfen, ob das aktuelle Kosten/Nutzen Verhältnis größer als der Schwellenindex ist
 if Environment.rewards[State]/Environment.weights[State] >= flexibleThreshold:
   counter +=1
   Environment.takeAction(1,State) # Zustand wird akzeptiert
   saved_ratios.append(Environment.rewards[State]/Environment.weights[State]) #Kosten-Nutzen-Verhältnis wird gespeichert 
   
 else:
  counter +=1
  Environment.takeAction(0,State) #  Zustand wird abgelehnt 
  saved_ratios.append(Environment.rewards[State]/Environment.weights[State]) #Kosten-Nutzen-Verhältnis wird gespeichert 
  



for i in range(0,30):
# Environment.presentState(i)
 visitState(i)
Environment.getResults() 
