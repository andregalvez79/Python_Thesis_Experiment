
#### to strat ####
#import every package in order to run the experiment
from psychopy import visual, core, event, data, gui
import random
import csv
import itertools
from psychopy import prefs

#to shuffle things FIRST WRITE THE HEADINGS IN A .CSV
outputFile = open("pavloviantrial.csv", "a")
outputFile.write("{},{},{},{}\n".format("Trialnr", "Value","Figure", "color"))
outputFile.close()

outputFile = open("qtrial.csv", "a")
outputFile.write("{},{},{},{}\n".format("Image2", "Value2","Image3", "Value3"))
outputFile.close()

outputFile = open("pavloviantrialforquery.csv", "a")
outputFile.write("{},{},{},{}\n".format("Index", "Value","Image", "color"))
outputFile.close()

outputFile = open("continue.csv", "a")
outputFile.write("{},{},{},{},{},{},{},{},{},{}\n".format("Image","Value","Image2", "Value2", "Image3", "Value3", "Image4", "Value4", "Image5", "Value5"))
outputFile.close()

#SOME VARIABLES TO DEFINE
nrPavlStim    = 5
pRepeats      = 10

def pavtrial():
# Import stimuli and assign to condition
    fractals = ['circle.png','pentagon.png','rombhus.png','square.png','triangle.png']
    random.shuffle(fractals)
#SHUFFLE THEM
    ## The nrs 1-5 refer to the stimuli jpg picture files
    stimList = {   '1': fractals[0],
                   '2': fractals[1],
                   '3': fractals[2],
                   '4': fractals[3],
                   '5': fractals[4], }

    ## The outcomes 1-5 refer to the values for the different stimuli
    outcomeList = {'1': "+ 10 Euro",
                   '2': "+ 2 Euro",
                   '3': "0 Euro",
                   '4': "- 10 Euro",
                   '5': "-2 Euro",}

    colorList = {'1': "green",
                   '2': "green",
                   '3': "white",
                   '4': "red",
                   '5': "red",}

    ## Get a list with condition names
    conditions = ['+ 10 Euro',"+ 2 Euro", "0 Euro",'- 10 Euro','- 2 Euro'] 
    for n in range(1,nrPavlStim+1,1):
        a = n
        b = conditions[n-1]
        #c = outcomeList[str(n)]
        d = stimList[str(n)]
        e = colorList[str(n)]
        outputFile = open("pavloviantrialforquery.csv", "a")
        outputFile.write('{},{},{},{}\n'.format(a,b,d,e))
        outputFile.close()# we want this to delimit below in the pair definition to only use this ordered 5
        #SHUFFLE THEM 5 TIMES, THIS WILL GIVE YOU A DIFFERENT COMBINATION OF FRACTAL, VALUE, AND COLOR EACH TIME YOU RUN IT
#CREATE A LIST WHERE IT WILL SHUFFLE THOSE 5 SHUFFLED STIMULI, AND CREATE 60 ROWS EACH WITH THE SAME ORDER OF VALUE STIM AND COLOR 
    tempList = []
    for n in range(1, nrPavlStim+1, 1):
        tempList.append(str(n))          
    presRandom = 10*tempList         #because 10*5 is 50 which is 10 times each stimuli
    random.shuffle(presRandom) 
        
    ## create csv file for trialpresentation based on the presRandom list with indexnumbers
    
    
    
    #NOW YOU RETRIEVE THAT INFO FROM THE LIST, WRITE IT DOWN
    trialnr = 1
    for index in presRandom:
        a = trialnr
        #b = index
        c = outcomeList[str(index)]
        d = stimList[str(index)]
        e = colorList[str(index)]
        outputFile = open ("pavloviantrial.csv", "a")
        outputFile.write('{},{},{},{}\n'.format(a,c,d,e))
                      
        trialnr += 1
    outputFile.close()




used = []

def getPairs():
    '''This function creates a list of lists, with every combination of pavlovian stimuli index numbers'''
    while len(used) < 10:
        ## First pick two numbers between 1-6
        L = str(random.randint(1,5))
        R = str(random.randint(1,5))
        ## If they are the same, pick a new number for R
        while L == R:
            R = str(random.randint(1,5))
        ## Test if this pair is already presented before, both Left/Right and Right/Left combination
        temp1 = [L,R]
        temp2 = [R,L]
        ## If the combination in either way is not presented before, add it to the used list. Otherwise start over
        if temp1 not in used and temp2 not in used: 
            used.append([L,R])   
    return used      

def openPavlConditions(x):
    '''Extract information from previously saved pavlovian conditions file'''
    
    pStimList   = {}
    pConditions = {}
    pOutcomes   = {}
    
    ## READ CSVFILE AND ENTER ROWS TO DICTS
    
    with open("pavloviantrialforquery.csv", "rb") as p_Conditions:
        reader = csv.reader(p_Conditions, delimiter = ",")
        for nr, line in enumerate(reader):
            if nr > 0:                              # Start at second row (skip varnames), start when i = 1
                pStimList[nr]   = str(line[2])      # what JPG
                pConditions[nr] = str(line[1])      # what condition, e.g. delLarge, immMedium etc.
            #pOutcomes[nr] = str(line[3])
    ## CHECK WHAT DICTIONARY WAS CALLED FOR (X)
    if x == 1:
        return pStimList
    if x == 2:
        return pConditions
    #if x == 3:
        #return pOutcomes




def extract():
    for i in range(len(pComparisonsList)): # lengh of thge list with the order
        x = pStimList.values()[int(pComparisonsList[i][0])-1] #get me the values from the list in that order
        y = pStimList.values()[int(pComparisonsList[i][1])-1] # the 0 is the first of the paris and the 1 is the second
        z = pConditions.values()[int(pComparisonsList[i][0])-1] # here i retrieve the value associated inseatd of the image itself
        a = pConditions.values()[int(pComparisonsList[i][1])-1] # same as above but for the other number 
        #print x
        #print y
        outputFile = open("qtrial.csv", "a")
        outputFile.write('{},{},{},{}\n'.format(x,z, y, a)) #i do it two times because in the query tirals when i resume it skips one trial for a reason
        outputFile.write('{},{},{},{}\n'.format(x, z ,y,a)) #so this is how i solved it




#############for continue trial ############
def continuetrial():
    listall = []
    for i in range (3):
        listfract = [x for x in itertools.permutations('12345', 1)]
        random.shuffle(listfract)
        listall += listfract
    return listall



def extract2():
    for i in range(len(orderlist)): # lengh of the list with the order
        outputFile = open("continue.csv", "a")
        if i < 4:
            x = pStimList.values()[int(orderlist[i][0])-1] #get me the values from the list in that order
            z = pConditions.values()[int(orderlist[i][0])-1] # here i retrieve the value associated inseatd of the image itself
            outputFile.write('{},{},'.format(x,z))
        elif i == 4 or i == 9:
            #x = pStimList.values()[int(orderlist[i][0])-1] #get me the values from the list in that order
            #z = pConditions.values()[int(orderlist[i][0])-1] # here i retrieve the value associated inseatd of the image itself
            x = pStimList.values()[int(orderlist[i][0])-1] #get me the values from the list in that order
            z = pConditions.values()[int(orderlist[i][0])-1] # here i retrieve the value associated inseatd of the image itself
            outputFile.write('{},{}\n'.format(x,z))
        elif i >= 5 and i != 9:
            x = pStimList.values()[int(orderlist[i][0])-1] #get me the values from the list in that order
            z = pConditions.values()[int(orderlist[i][0])-1] # here i retrieve the value associated inseatd of the image itself
            outputFile.write('{},{},'.format(x,z))





# These below are 

extractFirst     = 1
extractSecond    = 2
#extractThird    = 3

pavtrial()
pStimList        = openPavlConditions(extractFirst)
pConditions      = openPavlConditions(extractSecond)
#pConditions      = openPavlConditions(extractThird)
pComparisonsList = getPairs()
extract()
orderlist = continuetrial ()
extract2()
