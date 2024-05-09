

KnapsackCapacity = 1.0
Totalreward =0.0
States = []



def updateCapacity(currentcapacity): 
  global KnapsackCapacity
  KnapsackCapacity = KnapsackCapacity- currentcapacity
  return KnapsackCapacity


def updateReward(currentreward):
  global Totalreward
  Totalreward = Totalreward + currentreward
  return Totalreward

def getResults():
  print( "Your knapsack is full and you got a reward of ", Totalreward)
  print("You have chosen those states:",States)

def chosenStates(chosenstate):
  global States 
  States.append(chosenstate)
  return States

def takeAction(action,n): 
  global States
  if action == 0:
    return
  if action == 1: 
    if float(n["weight"])> KnapsackCapacity: 
      return
    if float(n["weight"])<= KnapsackCapacity and n["id"]=="State 20":
      updateCapacity(float(n["weight"]))
      updateReward(float(n["reward"]))
      chosenStates(n["id"])
      print("You've reached the end and you have a Totalreward of ", Totalreward, "and a remaining KnapsackCapacity of", KnapsackCapacity)
      print('Those are your chosen States', States)
      exit()
    if float(n["weight"])<= KnapsackCapacity:
      updateCapacity(float(n["weight"]))
      updateReward(float(n["reward"]))
      chosenStates(n["id"])
      return 
    if KnapsackCapacity == 0:
      getResults()
      exit()
    

 
