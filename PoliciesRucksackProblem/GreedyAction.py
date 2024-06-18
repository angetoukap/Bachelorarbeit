
import Environment



def visitState(State):
  Environment.takeAction(1,State)

for i in range (0,30):
 Environment.presentState(i)
 Environment.takeAction(1,i)
Environment.getResults()    
