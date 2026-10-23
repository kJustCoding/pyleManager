import os
import datetime
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

    fileMetadata=os.stat(absPath)

    
    return [fileType, fileExtension, fileMetadata]

def getAbsPath(path):

    return os.path.expanduser(path)


def getParentDirectory(currentPath):
    currentAbsPath=getAbsPath(currentPath)
    
    return os.path.dirname(currentAbsPath)

def timestampToDateTime(timestamp):

    datetime.datetime.fromtimestamp(timestamp)

    return timestamp

def doesPathExist(path):
    if os.path.exists(path): return True
    else:return False

    




