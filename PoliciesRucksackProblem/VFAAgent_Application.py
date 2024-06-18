#Test#
import Environment 
m = -2.4772506159816684e+40
c = -1.865846774926757e+41

def visitState( State):
 if Environment.Totalreward + m*Environment.weights[State]+c>= m*(Environment.KnapsackCapacity-Environment.weights[State])+c and Environment.weights[State] <=Environment.KnapsackCapacity:
     Environment.takeAction(1,State)
 else:
    Environment.takeAction(0,State)

for n in range(0,30):
   Environment.presentState(n)
   visitState(n)
Environment.getResults()

    
