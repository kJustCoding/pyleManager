import os
import mimetypes

def getFileInfo(absPath):

    mimeType, encoding= mimetypes.guess_type(absPath)

    try:
        fileType, fileExtension =mimeType.split("/")
    except:
        fileType, fileExtension = "",""

    
    return [fileType, fileExtension]

