import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path
import getFileInfo


SCRIPT_DIR= Path(__file__).parent



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



def displayNewDirectory(parentDir, cRow=0, columnAmm=6, showHiddenFiles=False):

    if len(filesWindow.winfo_children()) > 0:

        for fileEntry in filesWindow.winfo_children():
            fileEntry.destroy()

    dirList= backend.getSubDirs(parentDir,showHiddenFiles=showHiddenFiles)

    for j in range(len(dirList)):

        i=j+1
        cItem= dirList[i-1]

        absPath=parentDir + "/" + cItem

        fileLabel=ctk.CTkButton(filesWindow,
            width=140, height=140, font=("Helvetica",10,"bold"), corner_radius=10, text=cItem,
            anchor="s", fg_color="transparent", compound="top",
            command= lambda cFolder=cItem: displayNewDirectory(parentDir + "/" + cFolder))

        fileType= (getFileInfo.getFileInfo(absPath))[0]

        match fileType:
            case '':
                fileLabel.configure(image=folderIconForButton)
            case 'text':
                fileLabel.configure(image=textFileIconForButton)
            case 'image':
                fileLabel.configure(image=imageIconForButton)
            
        columnNumber=((i-1)%columnAmm)
        fileLabel.grid(column=columnNumber,row=cRow, pady=5, padx=5)
        
        if i%columnAmm ==0:
            cRow+=1

displayNewDirectory("~",showHiddenFiles=True)





filesWindow.grid(row=0,column=0,sticky="nsew")


root.mainloop()
