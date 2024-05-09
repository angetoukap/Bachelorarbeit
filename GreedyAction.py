import json 
import Environment


file_path = r"C:\Users\asus\Documents\Bachelorarbeit\PoliciesRucksackProblem\states.json"

with open(file_path,"r") as json_file:
 state = json.load(json_file)



for i in state['states']:
 Environment.takeAction(1,i)
Environment.getResults()    
