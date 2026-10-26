import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path


SCRIPT_DIR= Path(__file__).parent
forwardDirCache= []
currentDir=''

defaultButtonLength=140

uniFont="Adwaita Sans"

xScaling=1
yScaling=1
defColumnAmm=6


defaultWindowWidth=1000

defaultWindowHeight=600

root= ctk.CTk()
root.geometry(f"{defaultWindowWidth}x{defaultWindowHeight}")
root.title("Pyle Manager")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


filesWindow=ctk.CTkScrollableFrame(root, width= 950, height=500)


topBarFrame= ctk.CTkFrame(root, width=500, height=50,corner_radius=10)
currentDirEntry= ctk.CTkEntry(topBarFrame,width=500, height=50,corner_radius=10,fg_color='transparent',font=(uniFont,15,"bold"))
currentDirEntryConfirm=ctk.CTkButton(topBarFrame,width=75,height=50,corner_radius=10,text="Confirm",fg_color='transparent',font=(uniFont,15,"bold"))




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


def displayNewDirectory(parentDir, cRow=0, columnAmm=defColumnAmm, showHiddenFiles=False, buttonLength=defaultButtonLength):
    global currentDir

    
    if len(filesWindow.winfo_children()) > 0:

        for fileEntry in filesWindow.winfo_children():
            fileEntry.destroy()

    dirList= backend.getSubDirs(parentDir,showHiddenFiles=showHiddenFiles)

    for j in range(len(dirList)):

        i=j+1
        cItem= dirList[i-1]

        absPath=backend.getAbsPath(parentDir + "/" + cItem)

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

        
        currentDir=parentDir

        if i%columnAmm ==0:
            cRow+=1
    
    currentDirEntry.delete(0,"end")
    currentDirEntry.insert(0,parentDir)

lambdaDisplayDir= lambda p: displayNewDirectory(p)

def displayBackwardsDirectory():
    global forwardsDirCache, currentDir

    forwardDirCache.append(currentDir)

    newDir=backend.getParentDirectory(currentDir)
    displayNewDirectory(newDir)

def displayForwardsDirectory():
    global forwardDirCache

    displayNewDirectory(forwardDirCache[-1])

    forwardDirCache.pop()
        
def currentDirEntryConfirmFunc():
    path=currentDirEntry.get()
    absPath=backend.getAbsPath(path)

    if backend.doesPathExist(absPath)==True:
        displayNewDirectory(path)

        currentDirEntry.configure(text_color="white")

    else:
        currentDirEntry.configure(text_color="red")

def changeScaling(event=None):
    global defaultWindowWidth, currentDir,defColumnAmm

    xScale= (root.winfo_width()/defaultWindowWidth)
    yScale= (root.winfo_height()/defaultWindowWidth)

    columnAmm = int(defColumnAmm * xScale)

    print(f"columns {columnAmm}")



    

    displayNewDirectory(currentDir,columnAmm=max(1,columnAmm))


currentDirEntryConfirm.configure(command=currentDirEntryConfirmFunc)




displayNewDirectory(backend.getAbsPath("~"))

root.bind("<Configure>",changeScaling)


goBackwardsBtn= ctk.CTkButton(topBarFrame, width=80, height=50,corner_radius=10, fg_color='transparent',text='', image=backArrowIconForButton,
                command=lambda: displayBackwardsDirectory())

goForwardsBtn= ctk.CTkButton(topBarFrame, width=80, height=50,corner_radius=10, fg_color='transparent',text='', image=forwardArrowIconForButton,
                command=lambda: displayForwardsDirectory())



goBackwardsBtn.grid(column=0,row=0,sticky="sw")
goForwardsBtn.grid(column=1,row=0,sticky="sw")
currentDirEntry.grid(column=3,row=0,sticky="sw")
currentDirEntryConfirm.grid(column=4,row=0,sticky="sw")


topBarFrame.grid(sticky="sw",row=0,column=0)

filesWindow.grid(row=1,column=0,sticky="nsew")


root.mainloop()
