import numpy as np 
from operator import add
from queue import PriorityQueue
import matplotlib.pyplot as plt





gainedReward =0
saved_rewards =[]
residue_capacity=[]

Totalreward = 0
totalreward=0
weights = []
rewards =[]
y_pred = np.empty(0)
iweights=[]
irewards=[]
X = []
Y=[]
KnapsackCapacity = 0
knapsackCapacity=0
e =0.8
trade_off = ["exploration","exploitation"]




#Steigung
m = 0
#Y-Achsenabschnitt
c = 0

# Lernrate 
L = 0.001

#Iterationen 
iter = 100000
 
 #Reduktion der Rucksackkapazität
def updateCapacity(currentcapacity): 
  global KnapsackCapacity
  KnapsackCapacity = KnapsackCapacity - currentcapacity
  return KnapsackCapacity
# Erhöhung des Gesamtnutzen
def updateReward(currentreward):
  global Totalreward
  Totalreward = Totalreward + currentreward
  return Totalreward
#Reduktion der Rucksackkapazität 
def update_Capacity(currentcapacity): 
  global knapsackCapacity
  knapsackCapacity = knapsackCapacity - currentcapacity
  return knapsackCapacity

def update_Reward(currentreward):
  global totalreward
  totalreward = totalreward + currentreward
  return totalreward


########### Implementation des Branch and Bound Algorithmus ###########


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
    u = Node(-1, 0, 0)  
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0) 
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
#######################################################################  Ende der Implementation des Branch and Bound Algoruthmus#################################################



################################ Training der VFA ####################
for i in range(0,iter):

 
  #Array, welches die Rucksackkapazitäten nach positiven Entscheidungen speichert 

#Array,welchen den zunnehmenden Nutzen nach positiven Entscheidungen  speichert
 gainedReward =0
# States, die angenommen werden 
 
 Totalreward = 0
 weights = []
 rewards =[]
 iweights=[]
 irewards=[]
 X = []
 Y=[]
 arr =[]



######## Aktualisieren der Explorationsrate ###########
 if i > 0 and i%100==0:
   if round(e,1)<= 0.0:
     e=0.0
    
   else:
    e = 0.8**(i/100) 
     


################# Aktualisierung der  Steigung und des Y-Achsenabschnittes #####################
 if i > 0 and i%50==0:
   
   
   X_training = np.empty(0)
   Y_training = np.empty(0)
   Y_pred = np.empty(0)
  
   for a in range(0,len(residue_capacity)):
    X_training =np.append(X_training,residue_capacity[a])
  
   
   gainedReward=sum(saved_rewards)
   Y_training = np.append(Y_training,gainedReward)
   for j in range(1,len(saved_rewards)):
    gainedReward= gainedReward-saved_rewards[j-1]
    Y_training = np.append(Y_training,gainedReward)
     
  
   

   Y_pred = np.append(Y_pred,(m*X_training + c)) 

  
   
   n = len(Y_pred)
   if n != 0:
    D_m = -(2/n) * sum(X_training * (Y_training - Y_pred))  
    D_c = -(2/n) * sum(Y_training - Y_pred) 
   
    

    m = m - (L * D_m)  
    c = c - (L * D_c) 
    print("counter:", i)
    print("The Slope:", m, "and the intercept:", c)   
    
   saved_rewards =[]
   residue_capacity=[]
   gainedReward=0
   
 
########## Erstellung der Trainingsdaten ##############
 
  
 for n in range(0,30):
  iweights.append(np.random.uniform(0.0,1.0))
  irewards.append(np.random.uniform(0.0,1.0))

 sumweights = sum(iweights)
 weights =  np.divide(iweights,sumweights)
 KnapsackCapacity= sum(weights)*0.3
 updatedweights= np.divide(weights,2)
 updatedirewards= np.divide(irewards,2)
 rewards = list(map(add,updatedirewards,updatedweights))


####### Anwendung des Branch and Bound Algorithmus auf die Trainingsdaten#######
 for j in range(0,30):
  arr.append(Item(weights[j],rewards[j]))
 n=len(arr)
 maxprofit = knapsack(KnapsackCapacity,arr,n)


##### Wenden die VFA auf die Trainingsdaten an #########
 
    # aktuelles Gewicht
 X= weights 
    #aktuellen Nutzwert
 Y=  rewards 
  

 
 
 for k in range(0,30):
     

      
    
  if k== 29: 
      print ("You visited all states and got a reward of ", Totalreward)
      print("The Branch and Bound result:" + str(maxprofit))
      print("The Slope:", m, "and the intercept:", c)
       

  if round(KnapsackCapacity,2) == 0.00 : 
     print("Your Knapsack is full and you got a reward of:", Totalreward)
     print("The Branch and Bound result:" + str(maxprofit))
     print("The Slope:", m, "and the intercept:", c)
       
   
 
  if Totalreward +Y[k]+(m*(KnapsackCapacity-X[k])+c)>= (m*(KnapsackCapacity)+c)+Totalreward and X[k] <=KnapsackCapacity:
    if np.random.choice(trade_off,p=[e,1-e])== "exploitation":
      saved_rewards.append(Y[k])   
      residue_capacity.append(KnapsackCapacity-X[k])
      updateCapacity(X[k])
      updateReward(Y[k])
    else: 
      continue
     




######### Ende des Training ##########






########## Anwendung der VFA auf Testdaten   ##########
Iweights =[]
Irewards =[]


for n in range(0,30):
  Iweights.append(np.random.uniform(0.0,1.0))
  Irewards.append(np.random.uniform(0.0,1.0))

  Sumweights = sum(Iweights)
  Weights = np.divide(Iweights,Sumweights)
  knapsackCapacity= Sumweights*0.3
  Updatedweights= np.divide(Iweights,2)
  Updatedirewards= np.divide(Irewards,2)
  Rewards = list(map(add,Updatedirewards,Updatedweights))
  totalreward=0


   # aktuelles Gewicht
 
    #aktuellen Nutzwert

 
 
for w in range(0,30):
 
  if w== 29: 
      print ("You visited all states and got a reward of ", Totalreward)
      
      
      


  if round(knapsackCapacity,2) ==0.00 : 
     print("Your Knapsack is full and you got a reward of:", Totalreward)
    
     
    
     
      
    
    
  if totalreward +Rewards[k]+ (m*(knapsackCapacity-Weights[k])+c) >= totalreward+(m*(knapsackCapacity)+c) and Weights[k] <=knapsackCapacity:
      update_Capacity(Weights[k])
      update_Reward(Rewards[k])

    
     
     





 


 
      
      


















