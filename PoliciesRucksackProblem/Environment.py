import numpy as np 
from operator import add



Totalreward =0.0
presentedStates = {}
States = []
iweights =[]
irewards = []
id = []




for n in range(0,30):
   iweights.append(np.random.uniform(0.0,1.0))
   irewards.append(np.random.uniform(0.0,1.0))
   id.append("State"+str(n))
#sumweights = sum(iweights)
#weights =  np.divide(iweights,sumweights)
#KnapsackCapacity= sum(weights)*0.3
#updatedweights= np.divide(weights,2)
#updatedirewards= np.divide(irewards,2)
#rewards = list(map(add,updatedirewards,updatedweights))

KnapsackCapacity = 0.3
weights= [0.045881706512030294,0.05544606508567219,0.059684550048801445,0.02421060925786729,0.013157014523997392,0.0476814659067865,
          0.040936098579703414,0.0065721327867051165,0.01543385789714602,0.04726412300800195,0.024867235163887867,0.05933948389220945,
          0.01102289355015819,0.019002143109537566,0.027605875942420786,0.034806698586222,0.009556616763779247,0.05844255449934978,
          0.02119835799517921,0.02251760357382355,0.05929539705082468,0.06119896130633723,0.027498342853645982,0.008414770847476062,
          0.014971784772950289,0.04756690680631336,0.04128727857343902,0.04628355388365777,0.0007697600980475369,0.04729525712402908]

rewards =[0.29394720853337636,0.51511618368154608,0.5186626583163421, 0.38970958371873066,0.09873403539220797,0.22045827105999066,
          0.39148620669691164,0.27037732370428985,0.1758360336335315,0.40998487510610065,0.49909599359602536,0.34228131283492896,
          0.05479409890800658,0.4006939755118854,0.14258319557564003,0.42839025197465436,0.4413712319990189,0.2634967944203992,
          0.07912949330493368,0.27731711301338274,0.09108213387366156,0.3150214966674184,0.24622658871864259,0.40596518654128,
          0.19386794835860757,0.3470655019860594,0.4984651427012398,0.2880331255046118,0.4526037249856839,0.41963641327495715] 
 



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

def presentState(n):
  global weights 
  global rewards
  global id 
  print("You're in State"+ str(n)+  "and got a weight of "+ str(weights[n])+"and a reward of "+ str(rewards[n]))
  


def takeAction(action,n): 
  global States
  if action == 0:
    return
  if action == 1: 
    if weights[n]> KnapsackCapacity: 
      return
    if weights[n]<= KnapsackCapacity and id[n]=="State29":
      updateCapacity(weights[n])
      updateReward(rewards[n])
      chosenStates(id[n])
      print("You've reached the end and you have a Totalreward of ", Totalreward, "and a remaining KnapsackCapacity of", KnapsackCapacity)
      print('Those are your chosen States', States)
      exit()
    if weights[n]<= KnapsackCapacity:
      updateCapacity(weights[n])
      updateReward(rewards[n])
      chosenStates(id[n])
      return 
    if KnapsackCapacity == round(0,3):
      getResults()
      exit()
    

 
