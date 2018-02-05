#pavlovian learning phase

#### to strat ####
#import every package in order to run the experiment
from psychopy import visual, core, event, data, gui
import random
import csv
import itertools
from psychopy import prefs


#create a window were everything will be displayed
win = visual.Window(color = "black", fullscr = False)

##### generate a GUI to ask for participants' information #####
#this comes first that the window, because it doesn't work in full screen
#get some headings in the data
def ppdata ():
    outputFile = open("data.txt", "a")
    outputFile.write("{}\t{}\t{}\n".format("Gender", "Age", "ppcode"))
    outputFile.close()
    #subjects gender and age with GUI
    myDlg = gui.Dlg(title="Welcome to the experiment!")
    myDlg.addText('Please fill this with your information.')
    myDlg.addField('Gender:', choices = ["Male", "Female"])
    myDlg.addField('Age:')
    myDlg.addField('PPCODE:')
    #retrieve data from the participant
    ok_data = myDlg.show() 
    ppcode = int(myDlg.data[2])
    age = myDlg.data[1]
    gender = myDlg.data[0]
    #right down the data you retrieved
    if myDlg.OK:
        outputFile = open("data.txt", "a")
        outputFile.write("{}\t{}\t{}\n".format(ppcode, age, gender))
        outputFile.close()
    else:
        outputFile = open("data.txt", "a")
        outputFile.write('user cancelled')
        outputFile.close()

###############################################################################
####trial handler####
# import conditions with trial handler (loading excel files)
conditions = data.importConditions("pavloviantrial.csv")
conditionsq = data.importConditions("qtrial.csv")
conditions2 = data.importConditions("tdtrial.csv") 
conditionst = data.importConditions("transfertrial.csv") 
conditionsrate = data.importConditions("pavloviantrialforquery.csv")
conditionsask = data.importConditions("continue.csv")
#creat trial handler and the text and visual objects ill use for each part of the experiment

nReps = 1
trialspav = data.TrialHandler(conditions, nReps, method = "sequential")
pics = visual.ImageStim(win)
scale = .7
pics.size *= scale / max(pics.size)
words = visual.TextStim(win)


trialsquery = data.TrialHandler(conditionsq, nReps, method = "sequential")
pic1 = visual.ImageStim(win)
pic2 = visual.ImageStim(win)
scale = .7
pic1.size *= scale / max(pic1.size)
pic2.size *= scale / max(pic2.size)

nReps = 1
trialstd = data.TrialHandler(conditions2, nReps, method = "sequential")
tdss = visual.TextStim(win)
tdssd= visual.TextStim(win)
tdll = visual.TextStim(win)
tdlld= visual.TextStim(win)
tdllw= visual.TextStim(win)
tdllw2= visual.TextStim(win)
picsss = visual.ImageStim(win)
picsll = visual.ImageStim(win)
scale = .6
picsss.size *= scale / max(picsss.size)
picsll.size *= scale / max(picsll.size)

nReps = 1
trialst = data.TrialHandler(conditionst, nReps, method = "random")
ss = visual.TextStim(win)
ssd = visual.TextStim(win)
ll = visual.TextStim(win)
lld = visual.TextStim(win)
llw = visual.TextStim(win)
llw2 = visual.TextStim(win)
pavss = visual.ImageStim(win)
pavll = visual.ImageStim(win)
scale = .6
pavss.size *= scale / max(pavss.size)
pavll.size *= scale / max(pavll.size)

nReps = 1
trialsrate = data.TrialHandler(conditionsrate, nReps, method = "sequential")
item1 = visual.ImageStim(win)
ratingScale = visual.RatingScale(win, choices=range(1,11), stretch = (2), mouseOnly = False, markerColor = "yellow", marker = "hover")
scale = .7
item1.size *= scale / max(item1.size)


nReps = 1
trialsasking = data.TrialHandler(conditionsask, nReps, method = "sequential")
item = visual.ImageStim(win)
item2 = visual.ImageStim(win)
item3 = visual.ImageStim(win)
item4 = visual.ImageStim(win)
item5 = visual.ImageStim(win)

t = visual.TextStim(win)
valuet2 = visual.TextStim(win)
valuet3 = visual.TextStim(win)
scale = .35
item.size *= scale / max(item.size)
item2.size *= scale / max(item2.size)
item3.size *= scale / max(item3.size)
item4.size *= scale / max(item4.size)
item5.size *= scale / max(item5.size)

#add fixation cross
cross = visual.TextStim(win, text = "+")

#get some headings for the next set of info
#this data is for the pavlovian phase
outputFile = open("outdatapav.csv", "a")
outputFile.write("{},{}\n".format("stimuli", "value"))
outputFile.close()

outputFile = open("outdataq.csv", "a")
outputFile.write("{},{},{},{},{},{}\n".format("queryleft","valueleft", "queryright","valueright" , "querychoiceImage", "querychoiceValue"))
outputFile.close()
#this data is for the transfer phase
outputFile = open("outdatatrans.csv", "a")
outputFile.write("{},{},{},{},{},{},{},{}\n".format("SS", "LL","choice", "Delay","pavll","pavss","valuell","valuess"))
outputFile.close()
#this data is for the TD task
outputFile = open("outdatatd.csv", "a")
outputFile.write("{},{},{},{}\n".format("SS", "LL","choice", "Delay"))
outputFile.close()
#this one is fro the pre ratings
outputFile = open("outpre_rating.csv", "a")
outputFile.write("{},{},{}\n".format("Image", "Value","Rate"))
outputFile.close()
#this one is fro the prost ratings
outputFile = open("outpost_rating.csv", "a")
outputFile.write("{},{},{}\n".format("Image", "Value","Rate"))
outputFile.close()
#this one is for the askingpart
outputFile = open("outasking.csv", "a")
outputFile.write("{},{},{},{}\n".format("askedvalue", "choiceimg", "selectedvalue", "response"))
outputFile.close()
#for the lottery
outputFile = open("outlottery.csv", "a") # now i save the data separtely

outputFile.write("{},{},{}\n".format("y", "result", "yourchoice"))

outputFile.close()

#for general instructions
def instructions1():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide1.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    
#for pavlovian pshae
def instructions2():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide2.jpg")
    msg.draw()
    win.flip()
    respond= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs

#instructions for ordering
def instructions3():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide3.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs

#instructions for Transfer phase
def instructions4():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide4.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    
#instructions for scale
def instructions5():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide5.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=70.0, keyList=["space"]) #press any key to continue or wait 8 secs
    
    
#for lottery
def instructions6():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide6.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=30.0, keyList=["space"])
    
    #ending message
def instructions7():
    msg = visual.ImageStim(win, image = "E:\\AndreMajor\\Slide7.jpg")
    msg.draw()
    win.flip()
    respond1= event.waitKeys(maxWait=30.0, keyList=["space"])


#mouse
def mouse_choice(win, feedback, *args):
    
    no_choice = True 
    mouse = event.Mouse(visible = True, newPos = None, win = win)

    rects = []
    
    for arg in args:
        rects.append(visual.Rect(win, width = arg.size[0], height = arg.size[0], pos = arg.pos))
    
    while no_choice == True:
        
        count = 0 
        
        for arg in args:
            arg.draw()
            rects[count].draw()
            #mouse.clickReset()
            count = count + 1
        
        win.flip()
        
        for i in range(count):
            if mouse.isPressedIn(rects[i]):
                #y= mouse.getPressed(getTime=True)
                x= mouse.getPos()
                no_choice = False
                confirm = visual.ImageStim(win, size = (rects[i].width + 0.1, rects[i].height + 0.1), pos = rects[i].pos, color = 'black')
#                confirm.draw()
                
                for arg in args:
                    arg.draw()
                
                #win.flip()
#               core.wait(2)
                output = args[i]
    
    return(x[0])
     
     




def mouse_choice2(win, feedback, *args):
    
    no_choice = True 
    mouse = event.Mouse(visible = True, newPos = None, win = win)

    rects = []
    
    for arg in args:
        rects.append(visual.Rect(win, width = arg.size[0], height = arg.size[0], pos = arg.pos, opacity = arg.opacity))
    
    while no_choice == True:
        
        count = 0 
        
        for arg in args:
            arg.draw()
            rects[count].draw()
            #mouse.clickReset()
            count = count + 1
        
        win.flip()
        
        for i in range(count):
            if mouse.isPressedIn(rects[i]):
                #y= mouse.getPressed(getTime=True)
                x= mouse.getPos()
                no_choice = False
                confirm = visual.ImageStim(win, size = (rects[i].width + 0.1, rects[i].height + 0.1), pos = rects[i].pos, color = 'black', opacity = 0)
#                confirm.draw()
                
                for arg in args:
                    arg.draw()
                
                win.flip()
#               core.wait(2)
                output = args[i]
    
    return(x[0])
          
          





####################################################################################################################################
##############################################################################################################################
#######################################################
######################################################
#######################################################
#show everything using the previous generated data
###################################################

#define td task
#this task is very similar to the transfer phase in how it is built, the only difference is that the images are in the center, and it's transparent
#in order to make people click the option they prefer
#####################TD task
def blocktdtask():
    for trial in trialstd:
        core.wait(.3)
        tdll.setAutoDraw(True)
        tdlld.setAutoDraw(True)
        tdllw.setAutoDraw(True)
        tdllw2.setAutoDraw(True)
        tdss.setAutoDraw(True)
        tdssd.setAutoDraw(True)
        tdss.setText(trial["SS"])
        tdssd.text = ("Euro Now")
        tdss.pos = (-.5,.1)
        tdssd.pos = (-.5,-.1)
        tdll.setText(trial["LL"])
        tdlld.setText(trial["Delayweeks"])
        tdllw.text = ("     Euro in")
        tdllw2.text = ("weeks")
        tdll.pos = (.37,.1)
        tdllw.pos = (.58,.1)
        tdlld.pos = (.37,-.1)
        tdllw2.pos = (.58,-.1)
        picsll.setImage(trial["img"])
        picsll.pos = (.5,0)
        picsss.setImage(trial["img2"])
        picsss.pos = (-.5, 0)
        tdchoice = mouse_choice2 (win, True, picsss, picsll)
        if tdchoice < 0:
            tdchoice = 1
            ll.setAutoDraw(False)
            lld.setAutoDraw(False)
            llw.setAutoDraw(False)
            llw2.setAutoDraw(False)
            ss.setAutoDraw(False)
            ssd.setAutoDraw(False)
        else:
            tdchoice = 0
            ll.setAutoDraw(False)
            lld.setAutoDraw(False)
            llw.setAutoDraw(False)
            llw2.setAutoDraw(False)
            ss.setAutoDraw(False)
            ssd.setAutoDraw(False)
        outputFile = open("outdatatd.csv", "a")
        outputFile.write("{},{},{},{}\n".format(trial["SS"], trial["LL"], tdchoice, trial["Delayweeks"]))
        outputFile.close()


#define pavlvoian

####################pavlovian phase
lista = [5]
def blockpav():
    for trial in trialspav:
        if trial["Trialnr"] in lista:
            trialsquery.finished= False # somehow it is skiping one row
            for n,i in enumerate(lista):
                if i %5 ==0:
                    lista[n] = i + 5
            for trials in trialsquery:
                pic1.setImage(trials["Image3"]) #he encounter a pair of stimuli
                pic1.pos = (-.5,0)
                pic2.setImage(trials["Image2"])
                pic2.pos = (.5,0)
                query = mouse_choice (win, True, pic1, pic2) #the person just chooses the highest value, to reinforce learning 
                if query < 0:
                    queryv = trials["Value3"] #because we don't know the order beforehand
                    queryi = trials["Image3"]
                    trialsquery.finished= True # somehow it is skiping one row
                    outputFile = open("outdataq.csv", "a")
                    outputFile.write("{},{},{},{},{},{}\n".format(trials["Image3"], trials["Value3"] , trials["Image2"],trials["Value2"] , queryi, queryv))
                    outputFile.close()
                else:
                    queryv = trials["Value2"]
                    queryi = trials["Image2"]
                    trialsquery.finished= True
                    win.flip()
                    outputFile = open("outdataq.csv", "a")
                    outputFile.write("{},{},{},{},{},{}\n".format(trials["Image3"], trials["Value3"] , trials["Image2"],trials["Value2"] , queryi, queryv))
                    outputFile.close()
        else:#when it is not a query trial just show a shape for 3 secs and then add a text with the value
            cross.draw()
            win.flip()
            core.wait(.3)
            pics.setImage(trial["Figure"])
            pics.pos = (0,.3)
            pics.draw()
            win.flip()
            core.wait(3)
            words.setText(trial["Value"])
            pics.draw()
            words.size = (2.5)
            words.color = (trial["color"]) #I also painted the text
            words.pos = (0,-.4)
            words.draw()
            win.flip()
            core.wait(3) #draw the target word and show it for 
            query = 0
        #record the generated data of interest
        outputFile = open("outdatapav.csv", "a")
        outputFile.write("{},{}\n".format(trial["Figure"],trial["Value"]))
        outputFile.close()
    
    

#####################transfer phase
#define transfer
listx= []
def blocktransfer():
    for trial in trialst:
        core.wait(.3) # here we draw a fixation cross
        ll.setAutoDraw(True) # because im gonna use the mouse click definition
        lld.setAutoDraw(True) # i use this function to draw the stimuli, otherwise it wont let me
        llw.setAutoDraw(True) # I'll have to know when the person clicks, and thats more complicated
        llw2.setAutoDraw(True) # i have many to set different texts, this is because the textstim doesnt allow to concatenate
        ss.setAutoDraw(True)
        ssd.setAutoDraw(True)
        ss.setText(trial["SS"])
        ssd.text = ("Euro Now")
        ss.pos = (-.5,-.2) # the position for each text
        ssd.pos = (-.5,-.3)
        ll.setText(trial["LL"])
        lld.setText(trial["Delayweeks"])
        llw.text = ("Euro in")
        llw2.text = ("weeks")
        ll.pos = (.35,-.2)
        llw.pos = (.6,-.2)
        lld.pos = (.4,-.3)
        llw2.pos = (.55,-.3)
        pavll.setImage(trial["Pavll"]) # now I call the images i want to use
        pavll.pos = (.5,.2) # i position them
        pavss.setImage(trial["Pavss"])
        pavss.pos = (-.5, .2)
        choice = mouse_choice (win, True, pavss, pavll) #and use them in the mouse function, i save the position of the mouse when it was pressed
        if choice < 0: # and code it if in the x axis it was negative give me 1 , meaning chose SS
            choice = 1
            choice2 = trial["SS"]
            listx.append (choice2)
            ll.setAutoDraw(False) #i stop drawing that stimuli for the trial once the person makes a choice so it draws a new pair again
            lld.setAutoDraw(False)
            llw.setAutoDraw(False)
            llw2.setAutoDraw(False)
            ss.setAutoDraw(False)
            ssd.setAutoDraw(False)
        else:
            choice = 0
            choice2 = trial["LL"]
            listx.append (choice2)
            ll.setAutoDraw(False) # regardelss of the choice
            lld.setAutoDraw(False)
            llw.setAutoDraw(False)
            llw2.setAutoDraw(False)
            ss.setAutoDraw(False)
            ssd.setAutoDraw(False)
        outputFile = open("outdatatrans.csv", "a") # now i save the data separtely
        outputFile.write("{},{},{},{},{},{},{},{}\n".format(trial["SS"], trial["LL"], choice, trial["Delayweeks"], trial["Pavll"], trial["Pavss"], trial["valuell"], trial["valuess"]))
        outputFile.close()




#############scale

def preratings():
    for trial in trialsrate:
        item1.setImage(trial["Image"])
        item1.pos = (0,.3)
        while ratingScale.noResponse:
            ratingScale.pos = (0,-.5)
            item1.draw()
            ratingScale.draw()
            win.flip()
        rating = ratingScale.getRating()
        ratingScale.reset ()
        outputFile = open("outpre_rating.csv", "a") # now i save the data separtely
        outputFile.write("{},{},{}\n".format(trial["Image"], trial["Value"], rating))
        outputFile.close()

def postratings():
    for trial in trialsrate:
        item1.setImage(trial["Image"])
        item1.pos = (0,.3)
        while ratingScale.noResponse:
            ratingScale.pos = (0,-.5)
            item1.draw()
            ratingScale.draw()
            win.flip()
        rating = ratingScale.getRating()
        ratingScale.reset ()
        outputFile = open("outpost_rating.csv", "a") # now i save the data separtely
        outputFile.write("{},{},{}\n".format(trial["Image"], trial["Value"], rating))
        outputFile.close()


############## continue?

def mouse_choice3(win, feedback, *args):
    
    no_choice = True 
    mouse = event.Mouse(visible = True, newPos = None, win = win)

    rects = []
    
    for arg in args:
        rects.append(visual.Rect(win, width = arg.size[0], height = arg.size[0], pos = arg.pos))
    
    while no_choice == True:
        
        count = 0 
        
        for arg in args:
            arg.draw()
            rects[count].draw()
            #mouse.clickReset()
            count = count + 1
        
        win.flip()
        
        for i in range(count):
            if mouse.isPressedIn(rects[i]):
                #y= mouse.getPressed(getTime=True)
                #x= mouse.getPos()
                no_choice = False
                confirm = visual.ImageStim(win, size = (rects[i].width+.05, rects[i].height+.05), pos = rects[i].pos, color = 'yellow')
                confirm.draw()
                output = i
                for arg in args:
                    arg.draw()
                
                win.flip()
                core.wait(2)
                
    
    return(output)
     
     
def asking():
    for trial in trialsasking:
        if trialsasking.thisIndex == 0:
            valuet.setAutoDraw (True)
            valuet.setText(trial["Value"])
            valuet.pos = (.8,-.6)
            item.setImage(trial["Image"])
            item.pos = (0,0)
            item2.setImage(trial["Image2"])
            item2.pos = (.4,0)
            item3.setImage(trial["Image3"])
            item3.pos = (.8,0)
            item4.setImage(trial["Image4"])
            item4.pos = (-.4,0)
            item5.setImage(trial["Image5"])
            item5.pos = (-.8,0)
            choice = mouse_choice3 (win, True, item, item2, item3, item4, item5)
            if choice == 4:
                choice = trial["Image5"]
                valuet.setAutoDraw (False)
                selectedv = trial["Value5"]
                asked = trial["Value"]
                response = "incorrect"
            elif choice == 3:
                choice = trial["Image4"]
                valuet.setAutoDraw (False)
                selectedv = trial["Value4"]
                asked = trial["Value"]
                response = "incorrect"
            elif choice == 0:
                choice = trial["Image"]
                valuet.setAutoDraw (False)
                selectedv = trial["Value"]
                asked = trial["Value"]
                response = "correct"
            elif choice == 1:
                choice = trial["Image2"]
                valuet.setAutoDraw (False)
                selectedv = trial["Value2"]
                asked = trial["Value"]
                response = "incorrect"
            else:
                choice = trial["Image3"]
                valuet.setAutoDraw (False)
                selectedv = trial["Value3"]
                asked = trial["Value"]
                response = "incorrect"
        elif trialsasking.thisIndex == 1:
            valuet2.setAutoDraw (True)
            valuet2.setText(trial["Value2"])
            valuet2.pos = (.8,-.6)
            item.setImage(trial["Image"])
            item.pos = (0,0)
            item2.setImage(trial["Image2"])
            item2.pos = (.4,0)
            item3.setImage(trial["Image3"])
            item3.pos = (.8,0)
            item4.setImage(trial["Image4"])
            item4.pos = (-.4,0)
            item5.setImage(trial["Image5"])
            item5.pos = (-.8,0)
            choice = mouse_choice3 (win, True, item, item2, item3, item4, item5)
            if choice == 4:
                choice = trial["Image5"]
                valuet2.setAutoDraw (False)
                selectedv = trial["Value5"]
                asked = trial["Value2"]
                response = "incorrect"
            elif choice == 3:
                choice = trial["Image4"]
                valuet2.setAutoDraw (False)
                selectedv = trial["Value4"]
                asked = trial["Value2"]
                response = "incorrect"
            elif choice == 0:
                choice = trial["Image"]
                valuet2.setAutoDraw (False)
                selectedv = trial["Value"]
                asked = trial["Value2"]
                response = "incorrect"
            elif choice == 1:
                choice = trial["Image2"]
                valuet2.setAutoDraw (False)
                selectedv = trial["Value2"]
                asked = trial["Value2"]
                response = "correct"
            else:
                choice = trial["Image3"]
                valuet2.setAutoDraw (False)
                selectedv = trial["Value3"]
                asked = trial["Value2"]
                response = "incorrect"
        else:
            valuet3.setAutoDraw (True)
            valuet3.setText(trial["Value3"])
            valuet3.pos = (.8,-.6)
            item.setImage(trial["Image"])
            item.pos = (0,0)
            item2.setImage(trial["Image2"])
            item2.pos = (.4,0)
            item3.setImage(trial["Image3"])
            item3.pos = (.8,0)
            item4.setImage(trial["Image4"])
            item4.pos = (-.4,0)
            item5.setImage(trial["Image5"])
            item5.pos = (-.8,0)
            choice = mouse_choice3 (win, True, item, item2, item3, item4, item5)
            if choice == 4:
                choice = trial["Image5"]
                valuet3.setAutoDraw (False)
                selectedv = trial["Value5"]
                asked = trial["Value3"]
                response = "incorrect"
            elif choice == 3:
                choice = trial["Image4"]
                valuet3.setAutoDraw (False)
                selectedv = trial["Value4"]
                asked = trial["Value3"]
                response = "incorrect"
            elif choice == 0:
                choice = trial["Image"]
                valuet3.setAutoDraw (False)
                selectedv = trial["Value"]
                asked = trial["Value3"]
                response = "incorrect"
            elif choice == 1:
                choice = trial["Image2"]
                valuet3.setAutoDraw (False)
                selectedv = trial["Value2"]
                asked = trial["Value3"]
                response = "incorrect"
            else:
                choice = trial["Image3"]
                valuet3.setAutoDraw (False)
                selectedv = trial["Value3"]
                asked = trial["Value3"]
                response = "correct"
        outputFile = open("outasking.csv", "a") # now i save the data separtely
        outputFile.write("{},{},{},{}\n".format(asked, choice, selectedv, response))
        outputFile.close()
    



######## raffle/lottery #######

picso = visual.ImageStim(win, image = "ticket.png", pos=(0, 0))
scale = .7
picso.size *= scale / max(picso.size)
msg1 = visual.TextStim(win)
words2 = visual.TextStim(win)
words3 = visual.TextStim(win)
number1 = visual.TextStim(win)
ticket = visual.TextStim(win)
raf = visual.TextStim(win)
number2 = visual.TextStim(win)
number3 = visual.TextStim(win)
res = visual.TextStim(win)
msg2 = visual.TextStim(win)

listab = []
def getchoice():
    choice = random.randint(0, len(listx))
    towin = listx[choice]
    return towin



raffle = [] #set an empty list
def genssll(x,y):
    while len(raffle)< 100-y: #define how big is it going to be
        nr = random.randint(0,500) #random number between 
        raffle.append(nr)
    for i in range(y):
        raffle.append (x) #append the choice
        random.shuffle(raffle) #shuffle them
    return raffle
    

def getnum():
    nr2 = random.randint(0, 100)
    win = raffle[nr2]
    return win


def show():
    for i in range(len(listx)):
        msg1.text = ("How much can you win?")
        y = str(listx[i])
        ticket.text = (y)
        ticket.draw()
        msg1.pos = (0,.6)
        msg1.draw()
        win.flip ()
        core.wait(.1)
    words2.text = ("This is your ticket!")
    number1.text = (yourchoice)
    words3.text = ("Good luck!")
    words2.pos = (0,.6)
    words3.pos = (0,-.6)
    number1.pos = (0,0)
    number1.color = ("black")
    words2.draw ()
    words3.draw ()
    picso.draw()
    number1.draw()
    win.flip()
    core.wait(15)

def show2():
    for n in range(len(hundred)):
        msg2.text = ("Good luck!")
        msg2. pos = (0,.6)
        y = str(hundred[n])
        raf.text = (y)
        raf.draw()
        win.flip()
        core.wait(.1)
    if result == yourchoice:
        number2.text = ("This is the result!")
        number2.pos = (0,.6)
        picso.draw()
        number3.text = (result)
        number3.color = ("black")
        number3.draw()
        res.text = ("CONGRATULATIONS! YOU WON!")
        res.pos = (0,.6)
        res.draw()
        win.flip()
        core.wait(30)
        outputFile = open("outlottery.csv", "a") # now i save the data separtely for wins
        outputFile.write("{},{},{}\n".format(y, result, yourchoice))
        outputFile.close()
    else:
        number2.text = ("This is the result!")
        number2.pos = (0,.6)
        picso.draw()
        number3.text = (result)
        number3.color = ("black")
        number3.draw()
        res.text = ("YOU DID NOT WIN THIS TIME")
        res.pos = (0,.6)
        res.draw()
        win.flip()
        core.wait(30)

        outputFile = open("outlottery.csv", "a") # now i save the data separtely for not wins
        outputFile.write("{},{},{}\n".format(y, result, yourchoice))
        outputFile.close()

####to create csv files####
#run the createcsv script
### first part (TD task) ###
#ppdata()
#instructions()
#blocktdtask()
#intrusctionsrating()
#preratings()
### Pavlovian phase ###
#ppdata()
#instructions1()
#instructions2()
#blockpav()
#instructions3()
#asking()
### transfer phase ###
#instructions4()
blocktransfer()
#instructions5()
#postratings()
#instructions6()
#yourchoice  = getchoice() #with this you get a rand number between the lenght of the list of the choices... this in order to randomly call a number that will the be used to call one of the chocies inside the list
#hundred = genssll (yourchoice,5) #here you can define the chance.. so how many repetitions in a series of 100
#result = getnum() # the same just creates one rand num from the whole set of 100 that includes the choice appended in order to get a random number to call the order of a number of the list
#show()
#show2()
#instructions7()

#close window
win.close()