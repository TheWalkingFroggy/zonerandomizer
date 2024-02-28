import random
import sys
import os.path

path = './dummyzonemode.effectsettings'
pathdlc = './dummyzonemodedlc3.effectsettings'

def Randomizer():
    with open("dummyzonemode.effectsettings", "r") as f, open("zonemode.effectsettings", "w") as f1:
        for line in f:
            substr = line.split('=')
            numericValues = substr[1].split()

            i = 0
            while i<len(numericValues):
                if((substr[0].find('Fog') != -1) or (substr[0].find('scale') != -1) or (substr[0].find('Sky reflection') != -1) or (substr[0].find('Prelit') != -1)):
                    break
                else:
                    if(substr[0].find('tint') != -1):
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(random.randint(0, 255)))
                    else:        
                        if(substr[0].find('brightness') != -1):
                            numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 20), 6)))
                        else: 
                            if((substr[0].find('Lighting.Constant') != -1) or (substr[0].find('Sun') != -1)):
                                numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 0.5), 6)))
                            else: numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 4), 6)))
                i = i+1

            sys.stdout = f1
            print(substr[0] + "=", end="")
            for x in numericValues:
                print(x, "", end="")
            print("")
    return

def RandomizerDLC():
    with open("dummyzonemodedlc3.effectsettings", "r") as f, open("zonemodedlc3.effectsettings", "w") as f1:
        for line in f:
            substr = line.split('=')
            numericValues = substr[1].split()

            i = 0
            while i<len(numericValues):
                if((substr[0].find('Scene.Texture') != -1) or substr[0].find('Track.Base Colour Middle') != -1):
                    numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 3), 6)))
                else:
                    if((substr[0].find('Scene.Base Colour"') != -1) or (substr[0].find('Track.Texture') != -1)):
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 2), 6)))
                    else:
                        if(substr[0].find('Scene.Base Colour Middle') != -1):
                            numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0.77, 2), 6)))
                        else:
                            if(substr[0].find('Track.Near') != -1):
                                numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 0.298039), 6)))
                            else:
                                if(substr[0].find('Track.Base Colour"') != -1):
                                    numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 0.933333), 6)))
                i = i+1
            
            sys.stdout = f1
            print(substr[0] + "=", end="")
            for x in numericValues:
                print(x, "", end="")
            print("")
    return

if(os.path.isfile(path)):
    Randomizer()
else: print("zonemode.effectsettings file not found in directory. You sure you renamed it as 'dummyzonemode.effectsettings'?")

if(os.path.isfile(path)):
    RandomizerDLC()
else: print("zonemodedlc3.effectsettings file not found in directory. You sure you renamed it as 'dummyzonemodedlc3.effectsettings'?")
