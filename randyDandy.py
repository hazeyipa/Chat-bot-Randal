
#import needed modules 
import json #READ JSON GOD I JHATE JSON FILES WITH EVERYTHING IN ME AHHHHH
import re #re
import randomResponse #imports my python file 

#imports json data file 
file_path = 'C:\\Users\\CSCamp22\\myEDU camp\\newfloder.py\\RandyBot\\responses.json'

#function to load json file 
def loadJson(): #function name 
    with open(file_path) as botResponses: #open the thing thing 
        responseData = json.load(botResponses) #stor data 
        return responseData #return data :) 

responseData = loadJson() #store data in variable responseData 
print(responseData)



def getResponse(inputStr):
    splitMessage = re.split(r'\s+[.;?!,]\s*', inputStr.lower()) #this does something important but I dunno what 
    scoreList = []  #stores score 

        #checks all responses 
    for response in responseData:
        responseScore= 0
        requiredScore = 0
        requiredWords = response["requiredWords"] #LITERALLY DID NOT KNOW THIS WAS SUPPOSED TO BE IN BRACKETS WHAT
             
         #checks if any of the required words (defined in json file ) are present
        if requiredWords:
            for word in splitMessage:
                if word in requiredWords:
                    requiredScore +=1 

                 
            if requiredScore == len(requiredWords):
                for word in splitMessage:
                  if word in response["userInput"]:
                    responseScore += 1

        scoreList.append(responseScore)


        bestResponse = max(scoreList)
        responseIndex = scoreList.index(bestResponse)

        if inputStr == "":
            return "Uhh, can I help you with anything?"
    
        
             
        if bestResponse != 0:
            return responseData[responseIndex]["botResponse"]
                  
        return randomResponse.randomStr()


while True:
    userInput = input("You: ")
    print("Bot: ",getResponse(userInput))
