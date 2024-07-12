
import Environment



def visitState(State):
  Environment.takeAction(1,State)

for i in range (0,30):
# jedes State wird akzeptiert, solange genug  Kapazität vorhanden ist
 Environment.takeAction(1,i)
Environment.getResults()  
chosenStates = Environment.chosenStates  
