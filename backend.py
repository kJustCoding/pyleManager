import os
import mimetypes

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


def getFileInfo(absPath):

    mimeType, encoding= mimetypes.guess_type(absPath)

    try:
        fileType, fileExtension =mimeType.split("/")
    except:
        fileType, fileExtension = "",""

    
    return [fileType, fileExtension]

def getAbsPath(path):

    return os.path.expanduser(path)


def getParentDirectory(currentPath):
    currentAbsPath=getAbsPath(currentPath)
    
    return os.path.dirname(currentAbsPath)


