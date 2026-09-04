import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path
import getFileInfo


SCRIPT_DIR= Path(__file__).parent
cachedDirs= []


root= ctk.CTk()
root.geometry("1000x600")
root.title("Pyle Manager")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


filesWindow=ctk.CTkScrollableFrame(root, width= 950, height=500)

# Opening images
folderIcon=Image.open(SCRIPT_DIR / "assets" / "folder.ico" )
folderIconForButton=ctk.CTkImage(light_image=folderIcon,dark_image=folderIcon,size=(96,96))


textFileIcon=Image.open(SCRIPT_DIR / "assets" / "textFile.ico" )
textFileIconForButton=ctk.CTkImage(light_image=textFileIcon,dark_image=textFileIcon,size=(96,96))

imageIcon=Image.open(SCRIPT_DIR / "assets" / "image.ico" )
imageIconForButton=ctk.CTkImage(light_image=imageIcon,dark_image=imageIcon,size=(96,96))

applicationIcon=Image.open(SCRIPT_DIR / "assets" / "application.ico" )
applicationIconForButton=ctk.CTkImage(light_image=applicationIcon,dark_image=applicationIcon,size=(84,84))



def displayNewDirectory(parentDir, cRow=0, columnAmm=6, showHiddenFiles=False, buttonLength=140, isGoingBackward=False):

    global cachedDirs


    if not isGoingBackward: cachedDirs.append(parentDir)

    if len(filesWindow.winfo_children()) > 0:

        for fileEntry in filesWindow.winfo_children():
            fileEntry.destroy()

    dirList= backend.getSubDirs(parentDir,showHiddenFiles=showHiddenFiles)

    for j in range(len(dirList)):

        i=j+1
        cItem= dirList[i-1]

        absPath=parentDir + "/" + cItem

        fileLabel=ctk.CTkButton(filesWindow,
            width=buttonLength, height=buttonLength, font=("Adwaita Sans",13,"bold"), corner_radius=10, text=cItem,
            anchor="s", fg_color="transparent", compound="top",
            command= lambda cFolder=cItem: displayNewDirectory(parentDir + "/" + cFolder))

        fileLabel._text_label.configure(wraplength=buttonLength)

        fileType= (getFileInfo.getFileInfo(absPath))[0]

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
        
        if i%columnAmm ==0:
            cRow+=1


def displayBackwardsDirectory():
    global cachedDirs

    displayNewDirectory(cachedDirs[-2], isGoingBackward=True)

    print(cachedDirs)

    try: cachedDirs.remove(cachedDirs[-1])
    except: pass

    #try: cachedDirs.remove(cachedDirs[-1])
    #except: pass

    print(cachedDirs)

    

displayNewDirectory("~")





goBackwardsBtn= ctk.CTkButton(root, width=100, height=50, fg_color='transparent', text="<-",
                command=lambda: displayBackwardsDirectory())

goBackwardsBtn.grid(row=0,sticky="sw")
filesWindow.grid(row=1,column=0,sticky="nsew")


root.mainloop()
