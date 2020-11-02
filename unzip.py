import os
from zipfile import ZipFile
rootdir = "/home/eleboss/Documents/COMP3270_1A_2020-as1"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        # print (subdir + os.sep)
        if filepath.endswith(".zip"):
            # Create a ZipFile Object and load sample.zip in it
            with ZipFile(filepath, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
                zipObj.extractall(subdir + os.sep)
                print (filepath)