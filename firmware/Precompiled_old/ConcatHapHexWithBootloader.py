import sys
import shutil 
import fileinput
import os
import glob
 
def deleteHexFiles():
    fileList = glob.glob('./hap2.5.1*/hap2.5.1*.hex', recursive=True)
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def deleteFiles():
    fileList = glob.glob('../hap2.5.11/hamcp2515_*.c')
    fileList.extend(glob.glob('../hap2.5.11/mv*.h'))
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def buildHexFile():
    os.system("make clean")
    os.system("make all")

def copyFiles():
    os.chdir("../2.5.11/")
    print(os.getcwd())  
    shutil.copy(os.path.join(os.getcwd(),"files","mv.h"), os.getcwd())
    shutil.copy(os.path.join(os.getcwd(),"files","hamcp2515_10kBit."), os.getcwd())

def concatFlashAndBootloader():
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

            for l in range(4,6):
                for i in range(15):
                    id = hex(int(i))[2:].zfill(1)

                    f1 = open(desFolder + "/haEOF.hex")
                    f1_contents = f1.read()
                    f1.close()

                    f2 = open("Bootloader/HAPBootLoader-2893" + str(l) + id + ".hex")
                    f2_contents = f2.read()
                    f2.close()

                    f3 = open(desFolder + "/" + desFolder + "BootLoader-2893" + str(l) + id + ".hex", "w") # open in `w` mode to write
                    f3.write(f1_contents + f2_contents) # concatenate the contents
                    f3.close()

copyFiles()
#deleteFiles()
#deleteHexFiles()
#buildHexFile()
#concatFlashAndBootloader()

