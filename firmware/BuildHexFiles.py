import sys
import shutil 
import fileinput
import os
import glob
import os.path
 
def deletePrecompiledHexFiles():
    fileList = glob.glob('./precompiled/ha2.5.1*/ha*.hex', recursive=True)
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def deleteFiles():
    fileList = glob.glob('./hamcp2515.c')
    fileList.extend(glob.glob('./mv.h'))
    fileList.extend(glob.glob('./haam.h'))
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def copySourceFiles(mv,hamcp2515,haam):
    shutil.copy(os.path.join(os.getcwd(),"files",mv), os.path.join(os.getcwd(),"mv.h"))
    shutil.copy(os.path.join(os.getcwd(),"files",hamcp2515), os.path.join(os.getcwd(),"hamcp2515.c"))
    shutil.copy(os.path.join(os.getcwd(),"files",haam), os.path.join(os.getcwd(),"haam.h"))

def buildHexFile():
    os.system("make all")

def copyHexFile(destinationPath):
    if not os.path.exists(os.path.join("../precompiled",destinationPath)):
        os.makedirs(os.path.join("../precompiled",destinationPath))
    shutil.copy(os.path.join(os.getcwd(),"ha.hex"), os.path.join("../precompiled",destinationPath,"ha.hex"))

def cleanUp():
    os.system("make clean")

def concatFlashAndBootloader(destinationPath):
    for l in range(4,6):
        for i in range(16):
            id = hex(int(i))[2:].zfill(1)

            f1 = open(destinationPath + "/ha.hex")
            f1_contents = f1.read()
            f1_without_last_line = f1_contents[:f1_contents.rfind(':00000001FF\n')]
            f1.close()

            f2 = open("Bootloader/HAPBootLoader-2893" + str(l) + id + ".hex")
            f2_contents = f2.read()
            f2.close()

            f3 = open(destinationPath + "/" + "ha_withBootLoader-2893" + str(l) + id + ".hex", "w") # open in `w` mode to write
            f3.write(f1_without_last_line + f2_contents) # concatenate the contents
            f3.close()

def deleteHexFiles():
    fileList = glob.glob('./ha2.5.1*/ha.hex', recursive=True)
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

haam_List = ["4shutter","8shutter"]
hamcp2515_List = ["10kBit","125kBit"]
mv_List = ["DimmerNoSerialCan","DimmerSerialCan","DimmerSerialNoCan","NoDimmerNoSerialCan","NoDimmerSerialCan","NoDimmerSerialNoCan"]

deletePrecompiledHexFiles()

os.chdir("./2.5.11/")

for m in range(len(haam_List)): 
    for n in range(len(hamcp2515_List)): 
        for o in range(len(mv_List)):
            copySourceFiles(''.join(["mv_",mv_List[o],".h"]),''.join(["hamcp2515_",hamcp2515_List[n],".c"]),''.join(["haam_",haam_List[m],".h"]))
            buildHexFile()
            copyHexFile(''.join(["ha2.5.11_",mv_List[o],"_",hamcp2515_List[n],"_",haam_List[m]]))
            cleanUp()
            deleteFiles()

os.chdir("../precompiled/")

for m in range(len(haam_List)): 
    for n in range(len(hamcp2515_List)): 
        for o in range(len(mv_List)):
            concatFlashAndBootloader(''.join(["ha2.5.11_",mv_List[o],"_",hamcp2515_List[n],"_",haam_List[m]]))
					
os.chdir("../2.5.13/")

for m in range(len(haam_List)): 
    for n in range(len(hamcp2515_List)): 
        for o in range(len(mv_List)):
            copySourceFiles(''.join(["mv_",mv_List[o],".h"]),''.join(["hamcp2515_",hamcp2515_List[n],".c"]),''.join(["haam_",haam_List[m],".h"]))
            buildHexFile()
            copyHexFile(''.join(["ha2.5.13_",mv_List[o],"_",hamcp2515_List[n],"_",haam_List[m]]))
            cleanUp()
            deleteFiles()

os.chdir("../precompiled/")

for m in range(len(haam_List)): 
    for n in range(len(hamcp2515_List)): 
        for o in range(len(mv_List)):
            concatFlashAndBootloader(''.join(["ha2.5.13_",mv_List[o],"_",hamcp2515_List[n],"_",haam_List[m]]))

os.chdir("../")

deleteHexFiles()