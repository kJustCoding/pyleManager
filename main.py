import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path


SCRIPT_DIR= Path(__file__).parent
backwardDirCache= []
forwardDirCache= []

uniFont="Adwaita Sans"


root= ctk.CTk()
root.geometry("1000x600")
root.title("Pyle Manager")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


filesWindow=ctk.CTkScrollableFrame(root, width= 950, height=500)


topBarFrame= ctk.CTkFrame(root, width=500, height=50,corner_radius=10)
currentDirLabel= ctk.CTkLabel(topBarFrame, width=200, height=50,corner_radius=10,fg_color='transparent',font=(uniFont,15,"bold"))



# Opening images
folderIcon=Image.open(SCRIPT_DIR / "assets" / "folder.ico" )
folderIconForButton=ctk.CTkImage(light_image=folderIcon,dark_image=folderIcon,size=(96,96))


textFileIcon=Image.open(SCRIPT_DIR / "assets" / "textFile.ico" )
textFileIconForButton=ctk.CTkImage(light_image=textFileIcon,dark_image=textFileIcon,size=(96,96))

imageIcon=Image.open(SCRIPT_DIR / "assets" / "image.ico" )
imageIconForButton=ctk.CTkImage(light_image=imageIcon,dark_image=imageIcon,size=(96,96))

applicationIcon=Image.open(SCRIPT_DIR / "assets" / "application.ico" )
applicationIconForButton=ctk.CTkImage(light_image=applicationIcon,dark_image=applicationIcon,size=(84,84))


backArrowIcon=Image.open(SCRIPT_DIR / "assets" / "backArrow.png" )
backArrowIconForButton=ctk.CTkImage(light_image=backArrowIcon,dark_image=backArrowIcon,size=(32,32))

forwardArrowIcon=Image.open(SCRIPT_DIR / "assets" / "forwardArrow.png" )
forwardArrowIconForButton=ctk.CTkImage(light_image=forwardArrowIcon,dark_image=forwardArrowIcon,size=(32,32))




def displayNewDirectory(parentDir, cRow=0, columnAmm=6, showHiddenFiles=False, buttonLength=140, isGoingBackward=False):

    global backwardDirCache


    if not isGoingBackward: backwardDirCache.append(parentDir)

    if len(filesWindow.winfo_children()) > 0:

        for fileEntry in filesWindow.winfo_children():
            fileEntry.destroy()

    dirList= backend.getSubDirs(parentDir,showHiddenFiles=showHiddenFiles)

    for j in range(len(dirList)):

        i=j+1
        cItem= dirList[i-1]

        absPath=parentDir + "/" + cItem

        fileLabel=ctk.CTkButton(filesWindow,
            width=buttonLength, height=buttonLength, font=(uniFont,13,"bold"), corner_radius=10, text=cItem,
            anchor="s", fg_color="transparent", compound="top",
            command= lambda cFolder=cItem: displayNewDirectory(parentDir + "/" + cFolder))

        fileLabel._text_label.configure(wraplength=buttonLength)

        fileType= (backend.getFileInfo(absPath))[0]

        match fileType:
            case '':
                fileLabel.configure(image=folderIconForButton)
            case 'image':
                fileLabel.configure(image=imageIconForButton)
            case 'application':
                fileLabel.configure(image=applicationIconForButton)
            case _:
                fileLabel.configure(image=textFileIconForButton)
            
        columnNumber=((i-1)%columnAmm)
        fileLabel.grid(column=columnNumber,row=cRow, pady=5, padx=5)

        currentDirLabel.configure(text=parentDir)
        
        if i%columnAmm ==0:
            cRow+=1


def displayBackwardsDirectory():
    global backwardDirCache, forwardDirCache

    try:
        forwardDirCache.append(backwardDirCache[-2])
        displayNewDirectory(backwardDirCache[-2], isGoingBackward=True)
    
    except:
        currentPath=backwardDirCache[-1]
        displayNewDirectory(parentDir:= backend.getParentDirectory(currentPath), isGoingBackward=True)
        backwardDirCache.append(parentDir)
        


        


    print(backwardDirCache)

    try: backwardDirCache.remove(backwardDirCache[-1])
    except: pass

    #try: backwardDirCache.remove(backwardDirCache[-1])
    #except: pass

    print(backwardDirCache)

    

displayNewDirectory("~")





goBackwardsBtn= ctk.CTkButton(topBarFrame, width=80, height=50,corner_radius=10, fg_color='transparent',text='', image=backArrowIconForButton,
                command=lambda: displayBackwardsDirectory())

goForwardsBtn= ctk.CTkButton(topBarFrame, width=80, height=50,corner_radius=10, fg_color='transparent',text='', image=forwardArrowIconForButton,
                command=lambda: displayBackwardsDirectory())



goBackwardsBtn.grid(column=0,row=0,sticky="sw")
goForwardsBtn.grid(column=1,row=0,sticky="sw")
currentDirLabel.grid(column=3,row=0,sticky="sw")


topBarFrame.grid(sticky="sw",row=0,column=0)

filesWindow.grid(row=1,column=0,sticky="nsew")


root.mainloop()
