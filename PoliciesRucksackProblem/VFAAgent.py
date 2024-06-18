import numpy as np 
from operator import add
from queue import PriorityQueue


#Array, welches die Rucksackkapazitäten nach positiven Entscheidungen speichert 
remainingCapacity = np.empty(0)
#Array,welchen den zunnehmenden Nutzen nach positiven Entscheidungen  speichert
gainedReward =np.empty(0)
# States, die angenommen werden 
chosen_values =[]
Totalreward = 0
totalreward=0
weights = []
rewards =[]
y_pred = np.empty(0)
iweights=[]
irewards=[]
X = []
Y=[]
KnapsackCapacity=0
knapsackCapacity=0
e =0.8
trade_off = ["exploration","exploitation"]



#Steigung
m =-0.000225
#Y-Achsenabschnitt
c=0.943317

# Lernrate 
L = 0.001

#Iterationen 
iter = 30000

def updateCapacity(currentcapacity): 
  global KnapsackCapacity
  KnapsackCapacity = KnapsackCapacity - currentcapacity
  return KnapsackCapacity

def updateReward(currentreward):
  global Totalreward
  Totalreward = Totalreward + currentreward
  return Totalreward

def updateexplorationrate():
  global e
  e =e-0.001

def update_Capacity(currentcapacity): 
  global knapsackCapacity
  knapsackCapacity = knapsackCapacity - currentcapacity
  return knapsackCapacity

def update_Reward(currentreward):
  global totalreward
  totalreward = totalreward + currentreward
  return totalreward




class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight):
        self.level = level      
        self.profit = profit    
        self.weight = weight   

    def __lt__(self, other):
        return other.weight - self.weight  

def bound(u, n, W, arr):
    
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    
    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    
    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):
   
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0)  # Dummy node at the starting
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0)  # Starting node
        elif u.level == n - 1:
            continue  
        else:
            v = Node(u.level + 1, u.profit, u.weight) 

        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value

       
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v_bound = bound(v, n, W, arr)
       
        if v_bound > max_profit:
            priority_queue.put(v)

        
        v = Node(u.level + 1, u.profit, u.weight)
        v_bound = bound(v, n, W, arr)
      
        if v_bound > max_profit:
            priority_queue.put(v)

    return max_profit






#######################################################################

for i in range(0,iter):
  #Array, welches die Rucksackkapazitäten nach positiven Entscheidungen speichert 
 remainingCapacity = np.empty(0)
#Array,welchen den zunnehmenden Nutzen nach positiven Entscheidungen  speichert
 gainedReward =np.empty(0)
# States, die angenommen werden 
 
 Totalreward = 0
 weights = []
 rewards =[]
 y_pred = np.empty(0)
 iweights=[]
 irewards=[]
 X = []
 Y=[]
 arr =[]
 KnapsackCapacity=0

 # determines the probability if we want to explore or exploite
 if i > 0 and i%10==0:
   if round(e,2)== 0.00:
     e=0.0
   else:
    updateexplorationrate()

 if i > 0 and i%30==0:
   i =0
   X_training = np.empty(0)
   Y_training = np.empty(0)
   Y_pred = np.empty(0)
   while i  <= len(chosen_values)-1:
    X_training =np.append(X_training,chosen_values[i])
    i+=2
   i=1
   while i <= len(chosen_values)-1:
     Y_training = np.append(Y_training,chosen_values[i])
     i+=2
  
   

   Y_pred = np.append(Y_pred,m*X_training + c) 
   
    
  
   D_m = (-2/30) * sum(X_training * (Y_training - Y_pred))  
   D_c = (-2/30) * sum(Y_training - Y_pred) 

   m = m - L * D_m  
   c = c - L * D_c  
   
 

 # Datensatz mit allen States
 
  
 for n in range(0,30):
   iweights.append(np.random.uniform(0.0,1.0))
   irewards.append(np.random.uniform(0.0,1.0))

 sumweights = sum(iweights)
 weights =  np.divide(iweights,sumweights)
 KnapsackCapacity= sum(weights)*0.3
 updatedweights= np.divide(weights,2)
 updatedirewards= np.divide(irewards,2)
 rewards = list(map(add,updatedirewards,updatedweights))

 for j in range(0,30):
    arr.append(Item(weights[j],rewards[j]))
 n=len(arr)

 maxprofit = knapsack(KnapsackCapacity,arr,n)


 
    # aktuelles Gewicht
 X= weights
    #aktuellen Nutzwert
 Y= rewards
  
 for i in range(0,30):
    y_pred= np.append(y_pred,m*X[i]+c)
 
 for k in range(0,30):

  if len(chosen_values) ==0:
     if np.random.choice(trade_off,p=[e,1-e])== "exploitation":
      remainingCapacity= KnapsackCapacity-weights[k]
      gainedReward =Totalreward+rewards[k]
      chosen_values.append(remainingCapacity)
      chosen_values.append(gainedReward)
      updateCapacity(weights[k])
      updateReward(rewards[k])
     else: 
      continue
     

  if k == 29: 
      print ("You visited all states and got a reward of ", Totalreward)
      print("Slope:",m,"and Intercept:",c)
      print("The Branch and Bound result:" + str(maxprofit))
      if Totalreward >= maxprofit*0.95:
        print("#######################################################")
        exit()
      continue


  if round(KnapsackCapacity,2) == 0.00 : 
     print("Your Knapsack is full and you got a reward of:", Totalreward)
     print("The Branch and Bound result:" + str(maxprofit))
     if Totalreward >= maxprofit*0.95:
         print("#####################################################")
         exit()
     continue

  estimate = m*(KnapsackCapacity-X[k])+c
  if Totalreward + y_pred[k]>= estimate and X[k] <=KnapsackCapacity:
     if np.random.choice(trade_off,p=[e,1-e])== "exploitation":
      remainingCapacity= KnapsackCapacity-weights[k]
      gainedReward =Totalreward+rewards[k]
      chosen_values.append(remainingCapacity)
      chosen_values.append(gainedReward)
      updateCapacity(weights[k])
      updateReward(rewards[k])
     else: 
      continue
     
  





#Test#

for n in range(0,30):
  iweights.append(np.random.uniform(0.0,1.0))
  irewards.append(np.random.uniform(0.0,1.0))

  sumweights = sum(iweights)
  weights = np.divide(iweights,sumweights)
  knapsackCapacity= sum(weights)*0.3
  updatedweights= np.divide(weights,2)
  updatedirewards= np.divide(irewards,2)
  rewards = list(map(add,updatedirewards,updatedweights))
  totalreward=0


   # aktuelles Gewicht
  X= weights
    #aktuellen Nutzwert
  Y= rewards
 

   #Vorhersage des aktuellen Nutzwertes 




 
for k in range(0,30):
 
  if k== 29: 
      print ("You visited all states and got a reward of ", Totalreward)
      print("Slope:",m,"and Intercept:",c,"and a exploration rate of:",e)
      
      


  if round(knapsackCapacity,2) ==0.00 : 
     print("Your Knapsack is full and you got a reward of:", Totalreward)
     print("Slope:",m,"and Intercept:",c,"and a exploration rate",e)
    
     
      
    
    
  if Totalreward + m*X[k]+c>= m*(knapsackCapacity-X[k])+c and X[k] <=knapsackCapacity:
     
      remainingCapacity= knapsackCapacity-weights[k]
      gainedReward =totalreward+rewards[k]
     
      chosen_values.append(remainingCapacity)
      chosen_values.append(gainedReward)
      update_Capacity(weights[k])
      update_Reward(rewards[k])

    
     
     





 


 
      
      


















