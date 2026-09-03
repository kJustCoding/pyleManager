import customtkinter as ctk
from PIL import Image
import backend
from pathlib import Path


SCRIPT_DIR= Path(__file__).parent

root= ctk.CTk()
root.geometry("1000x600")

columnAmm=6
cRow=0

filesWindow=ctk.CTkScrollableFrame(root, width= 950, height=500)

# Opening images
folderIcon=Image.open(SCRIPT_DIR / "assets" / "folder.ico" )

folderIconForButton=ctk.CTkImage(light_image=folderIcon,dark_image=folderIcon,size=(96,96))

dirList= backend.getSubDirs()


for j in range(len(dirList)):

    i=j+1
    cItem= dirList[i-1]

    fileLabel=ctk.CTkButton(filesWindow, width=140, height=140, font=("Helvetica",10,"bold"), border_color="blue", border_width=3, corner_radius=10, text=cItem, anchor="s", image=folderIconForButton, compound="top" )
        
    columnNumber=((i-1)%columnAmm)
    fileLabel.grid(column=columnNumber,row=cRow, pady=5, padx=5)
    
    if i%columnAmm ==0:
        cRow+=1

filesWindow.pack(anchor="s")





root.mainloop()
