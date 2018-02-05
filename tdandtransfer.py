
#### to strat ####
#import every package in order to run the experiment
from psychopy import visual, core, event, data, gui
import random
import csv
import itertools
from psychopy import prefs

#to shuffle things FIRST WRITE THE HEADINGS IN A .CSV
outputFile = open("tdtrial.csv", "a")
outputFile.write("{},{},{},{},{},{}\n".format("Trialnr", "SS","LL", "Delayweeks", "img", "img2"))
outputFile.close()

outputFile = open("transfertrial.csv", "a")
outputFile.write("{},{},{},{}\n".format("Pavll", "valuell","Pavss", "valuess"))
outputFile.close()
#########################################################################
##################################### TD TASK ############################################
#for the td task i create a set of 25 ss and ll pairs with a delay
ssnll = [] #set an empty list
def genssll():
    while len(ssnll)<25: #define how big is it going to be
        ss = str(random.randint(10,40)) #random number between 10 and 40 for ss
        ll = str(random.randint(35,75)) #rand number between 35 and 75 for ll
        delay = str(random.randint(1,25)) # the same 1 to 25 for delay in weeks
        if ll > ss: #so the ss is always smaller than the ll
            ssnll.append([ss,ll,delay])
    random.shuffle(ssnll) #shuffle them
    return ssnll
    


def extracttd():
    for i in range(len(ssnll)): #now using the list we just created with the ss ll and delay
        trial = i
        x = ssnll[i][0] #exctract the variables one by one 25 times
        y = ssnll[i][1]
        z = ssnll[i][2]
        img = "1.png" #add this every time because of the mouseclikcs
        img2 = "1.png" #i need two pics so two rows
        outputFile = open("tdtrial.csv", "a")
        outputFile.write('{},{},{},{},{},{}\n'.format(trial,x, y, z, img, img2)) # i write them down in a csv to use it in the pit as conditions
        outputFile.close()


ssnll = genssll()
extracttd()
#######################################################################################
####################################### transfer phase ################################################
def pairspav():
    listtotal = []
    for i in range (4):
        listfract = [x for x in itertools.permutations('12345', 2)]
        listfract.append (("1","1"))
        listfract.append (("2","2"))
        listfract.append (("3","3"))
        listfract.append (("4","4"))
        listfract.append (("5","5"))
        random.shuffle(listfract)
        listtotal += listfract
    return listtotal
    
    
    


def openPavlConditions(x):
    '''Extract information from previously saved pavlovian conditions file'''
    
    pStimList   = {}
    pConditions = {}
    pOutcomes   = {}
    
    ## READ CSVFILE AND ENTER ROWS TO DICTS
    
    with open("pavloviantrialforquery.csv", "rb") as p_Conditions:
        reader = csv.reader(p_Conditions, delimiter = ",")
        for nr, line in enumerate(reader):
            if nr > 0:                              # Start at second row (skip varnames), start when i = 1 """i dont have var names""" so i dont need this
                pStimList[nr]   = str(line[2])      # what JPG
                pConditions[nr] = str(line[1])      # what condition, e.g. delLarge, immMedium etc.
    ## CHECK WHAT DICTIONARY WAS CALLED FOR (X)
    if x == 1:
        return pStimList
    if x == 2:
        return pConditions
    #if x == 3:
        #return pOutcomes



def extract():
    for i in range(len(comparisonList)): # lengh of the list with the order
        x = pStimList.values()[int(comparisonList[i][0])-1] #get me the values from the list in that order
        y = pStimList.values()[int(comparisonList[i][1])-1] # the 0 is the first of the paris and the 1 is the second
        z = pConditions.values()[int(comparisonList[i][0])-1] # here i retrieve the value associated inseatd of the image itself
        a = pConditions.values()[int(comparisonList[i][1])-1] # same as above but for the other number 
        outputFile = open("transfertrial.csv", "a")
        outputFile.write('{},{},{},{}\n'.format(x,z, y, a)) #i do it two times because in the query tirals when i resume it skips one trial for a reason


# These below are 

extractFirst     = 1
extractSecond    = 2
#extractThird    = 3


pStimList        = openPavlConditions(extractFirst)
pConditions      = openPavlConditions(extractSecond)
#pConditions      = openPavlConditions(extractThird)
comparisonList = pairspav()
y = extract()
