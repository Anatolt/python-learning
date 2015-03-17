#this programm remove numbers from filenames
# put this file in folder near files need to rename
import os
flist = os.listdir(os.getcwd()) 
print(flist)
for fname in flist:
    os.rename(fname, fname.translate(None, "0123456789"))
