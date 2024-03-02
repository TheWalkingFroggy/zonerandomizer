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

            for i in range(len(numericValues)):
                newColor = 0
                black = 0
                if(random.randint(0, 2) == 1):
                    black = 255
                if((substr[0].find('Fog') != -1) or (substr[0].find('scale') != -1) or (substr[0].find('brightness') != -1)):
                    break
                else:
                    if((substr[0].find('Lighting.C') != -1) or (substr[0].find('Lighting.P') != -1 )):
                        numericValues[i] = numericValues[i].replace(numericValues[i], '0.500000')
                        continue
                    if((substr[0].find('tint') != -1) or (substr[0].find('Sky reflection') != -1)):
                        newColor = max(0, (random.randint(0, 255) - black))
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))
                        continue        
                    if(substr[0].find('Lighting') != -1):
                        newColor = f'{max(0.00, (round(random.uniform(0, 1), 2) - black)):.6f}'
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))
                        continue
                    else:
                        newColor = f'{max(0.00, (round(random.uniform(0, 2), 2) - black)):.6f}'
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))

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
