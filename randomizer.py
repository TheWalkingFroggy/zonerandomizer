import random
import sys
import os.path

path = './zonemode.effectsettings'

def Randomizer():
    with open("zonemode.effectsettings", "r") as f, open("newzonemode.effectsettings", "w") as f1:
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
                    if((substr[0].find('Lighting.Constant') != -1) or (substr[0].find('Lighting.Prelit') != -1 )):
                        numericValues[i] = numericValues[i].replace(numericValues[i], '0.500000')
                        continue
                    if((substr[0].find('tint') != -1) or (substr[0].find('Sky reflection') != -1)):
                        newColor = max(0, (random.randint(0, 255) - black))
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))
                        continue        
                    if(substr[0].find('Lighting') != -1):   # Sun color
                        newColor = f'{max(0.00, (round(random.uniform(0, 1), 2) - black)):.6f}'
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))
                        continue
                    else:   # Scene and Track texture, base color /// Sky horizon and zenith color 
                        newColor = f'{max(0.00, (round(random.uniform(0, 3), 2) - black)):.6f}'
                        numericValues[i] = numericValues[i].replace(numericValues[i], str(newColor))

            sys.stdout = f1
            print(substr[0] + "=", end="")
            for x in numericValues:
                print(x, "", end="")
            print("")
        
        f.close()
        f1.close()
        os.remove(path)
        os.rename('./newzonemode.effectsettings', path)
    return

if(os.path.isfile(path)):
    Randomizer()
else: print("zonemode.effectsettings file not found in directory.")
