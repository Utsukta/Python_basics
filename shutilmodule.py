#Provides higher level interface for workig with the file and folders.
#shutil is the short for shell
import shutil

# #It will make the exact copy of shutilmodule.py
shutil.copy2("shutilmodule.py","shutilmodulecopy.py")

# #this will create the new folder containing exact files available in calculator
shutil.copytree("calculator",".calculator")

# #This will move the file testmove.py from inside the folder
shutil.move("shutiltest/testmove.py","testmove.py")

#this will removes the folder 
#this recursively delets the directory located at that path, along with all the content
shutil.rmtree("shutiltest")