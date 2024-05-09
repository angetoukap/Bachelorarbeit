import numpy as np 

#Array, welches die Rucksackkapazitäten nach positiven Entscheidungen speichert 
remainingCapacity = np.empty(0)
#Array,welchen den zunnehmenden Nutzen nach positiven Entscheidungen  speichert
gainedReward =np.empty(0)
# States, die angenommen werden 
chosen_states = np.empty(0)
Totalreward = 0
KnapsackCapacity = 1
#Steigung
m =0
#Y-Achsenabschnitt
c=0

def updateCapacity(currentcapacity): 
  global KnapsackCapacity
  KnapsackCapacity = KnapsackCapacity- currentcapacity
  return KnapsackCapacity

def updateReward(currentreward):
  global Totalreward
  Totalreward = Totalreward + currentreward
  return Totalreward


 # Datensatz mit allen States
idic ={}
for j in range(0,30):
   idic["State"+ str(j)]= {"weight" : np.random.normal(0.5,0.5), "reward" : np.random.normal(0.5,0.5)}
  
for k in range(0,28):
    # aktuelles Gewicht
    X= idic["State"+str(k)]["weight"]
    #aktuellen Nutzwert
    Y= idic["State"+str(k)]["reward"]
    # Gewicht des darauffolgenden States
    Xn=idic["State"+str(int(k)+1)]["weight"]
    # Nutzwert des darauffolgenden States 
    Yn= idic["State"+str(int(k)+1)]["reward"]
    #Vorhersage des aktuellen Nutzwertes 
    y_pred = (m*X)+c
    #Vorhersage des darauffolgenden Nutzwertes
    yn_pred = (m*Xn)+c
    
    # falls noch kein State angenommen wurde
if chosen_states.size == 0: 
     chosen_states = np.append(chosen_states,idic["State"+str(k)])
     updateCapacity(idic["State"+str(k)]["weight"])
     updateReward(idic["State"+str(k)]["reward"])
     remainingCapacity=np.append(remainingCapacity,KnapsackCapacity)
     gainedReward =np.append(gainedReward,Totalreward)

    # wenn die höherer Nutzen mit der VFA erzielt werden kann
    
    
elif Totalreward + y_pred >= yn_pred and X <=KnapsackCapacity:
     chosen_states = np.append(chosen_states,idic["State"+str(k)])
     updateCapacity(idic["State"+str(k)]["weight"])
     updateReward(idic["State"+str(k)]["reward"])
     remainingCapacity=np.append(remainingCapacity,KnapsackCapacity)
     gainedReward = np.append(gainedReward,Totalreward)
    
    #Abbruchskriterium
elif round(KnapsackCapacity,1) <= 0.0:
       print("Der Rucksack ist voll")
       profit= gainedReward[-1] - gainedReward[0]
       print ("With this VFA you made a profit of ", profit)
       exit()
    #Abbruchskriterium
elif k== 29:
      profit= gainedReward[-1] - gainedReward[0]
      print ("With this VFA you made a profit of ", profit)
      exit()







 


# mse =(1/n)*sum(np.square(y_pred -Y))
 #mse_m = (1/n)*sum(X*(y_pred -Y))
 #mse_c = (1/n)*sum(y_pred-Y)
 #m = m - learning_rate *mse_m
 #c = c -learning_rate*mse_c
 #accuracy = r2_score(Y,y_pred)
#print("Das Bestimmtheitsmaeß betraegt:",accuracy)


#TrainingEnde












