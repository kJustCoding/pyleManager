import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path


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



def displayNewDirectory(parentDir, cRow=0, columnAmm=6):

    dirList= backend.getSubDirs(parentDir)

    for j in range(len(dirList)):

        i=j+1
        cItem= dirList[i-1]

        fileLabel=ctk.CTkButton(filesWindow,
            width=140, height=140, font=("Helvetica",10,"bold"), corner_radius=10, text=cItem,
            anchor="s", image=folderIconForButton, fg_color="transparent", compound="top")
            
        columnNumber=((i-1)%columnAmm)
        fileLabel.grid(column=columnNumber,row=cRow, pady=5, padx=5)
        
        if i%columnAmm ==0:
            cRow+=1




displayNewDirectory("~")










filesWindow.grid(row=0,column=0,sticky="nsew")
root.mainloop()
