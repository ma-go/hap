import sys
import shutil 
import fileinput
import os

for j in range(1,5):
    
    for k in range(1,5):

        if k == 1:
            desFolder = "hap2.5.1" + str(j) + "_WithDimmer_WithoutSerial"
        elif k == 2:
            desFolder = "hap2.5.1" + str(j) + "_WithDimmer_WithSerial"
        elif k== 3:
            desFolder = "hap2.5.1" + str(j) + "_WithoutDimmer_WithoutSerial"
        else:
            desFolder = "hap2.5.1" + str(j) + "_WithoutDimmer_WithSerial"
        
        for i in range(15):
            id = hex(int(i))[2:].zfill(1)

            f1 = open(desFolder + "/haEOF.hex")
            f1_contents = f1.read()
            f1.close()

            f2 = open("Bootloader/HAPBootLoader-28934" + id + ".hex")
            f2_contents = f2.read()
            f2.close()

            f3 = open(desFolder + "/" + desFolder + "BootLoader-28934" + id + ".hex", "w") # open in `w` mode to write
            f3.write(f1_contents + f2_contents) # concatenate the contents
            f3.close()