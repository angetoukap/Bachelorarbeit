#Test#
import Environment 
m = 11.648777781703993
c = 83.65737088499667


def visitState( State):
 estimate =Environment.rewards[State]+ Environment.Totalreward+(m*(Environment.KnapsackCapacity-Environment.weights[State])+c) 
 future =(m*(Environment.KnapsackCapacity)+c)+Environment.Totalreward 
 if estimate>=  future and Environment.weights[State] <=Environment.KnapsackCapacity:
     Environment.takeAction(1,State)
 else:
    Environment.takeAction(0,State)

for n in range(0,30):
  # Environment.presentState(n)
   visitState(n)
Environment.getResults()
chosenStates = Environment.chosenStates

    
