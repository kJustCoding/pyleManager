import os

homePath=os.path.expanduser("~")

def getSubDirs(dir=homePath, showHiddenFiles=False):

    dir=os.path.expanduser(dir)

    filesUnfiltered=os.listdir(dir)

    filesFiltered=[]

    if not showHiddenFiles:

        for i in filesUnfiltered:
            if i[0]!=".":
                filesFiltered.append(i)

    else:

        return filesUnfiltered

    return filesFiltered



