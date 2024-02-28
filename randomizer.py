import random
import sys
separator = '='
with open("dummyzonemode.effectsettings", "r") as f, open("zonemode.effectsettings", "w") as f1:
    for line in f:
        substr = line.split(separator)
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
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(random.randint(0, 20)))
                    else: 
                        if((substr[0].find('Lighting.Constant') != -1) or (substr[0].find('Sun') != -1)):
                            numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 0.5), 6)))
                        else: numericValues[i] = numericValues[i].replace(numericValues[i], str(round(random.uniform(0, 4), 6)))
            i = i+1

        sys.stdout = f1
        print(substr[0] + "=", end="")
        for x in numericValues:
            print(x, " ", end="")
        print("")