#in the name of god
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("350x830")
root.minsize(350, 830)
root.maxsize(350, 830)
root.title("Colors")
root.configure(bg='#424242')

def Go(labl,btun,btnr,btng,btngy,btnw,btny,btnp,btnhp,btnm,btnc,btnyg,btnl):
    chanched = False
    color = btun['text']
    btnColor = btun['bg']
    if chanched == False: 
        btun.config(bg=color)
        chanched = True
        lab.config(bg=color)
        lab.config(text=color)
    if btnColor == color :
        btun.config(bg="#333333")
        chanched = False
        lab.config(bg="#636363")
        lab.config(text="Choice color")
        btnr.config(bg="#333333")
        btng.config(bg="#333333")
        btngy.config(bg="#333333")
        btnw.config(bg="#333333")
        btny.config(bg="#333333")
        btnp.config(bg="#333333")
        btnhp.config(bg="#333333")
        btnm.config(bg="#333333")
        btnc.config(bg="#333333")
        btnyg.config(bg="#333333")
        btnl.config(bg="#333333")
    labl.update()
    btun.update()
    
def set_color (textbox,labelshow) :
    m = textbox.get()
    labelshow.config(bg = m)
    backcol = labelshow['bg']
    if backcol == m:
        labelshow.config(text = m)
    if m == "#ff00ff":
        labelshow.config(text = "magenta")
    elif m == "#ffff00":
        labelshow.config(text = "yellow")
    elif m == "#ff0000":
        labelshow.config(text = "red")
    elif m == "#0000ff":
        labelshow.config(text = "blue")
    elif m == "#808080":
        labelshow.config(text = "gray")
    elif m == "#007f00" :
        labelshow.config(text = "green")
    elif m == "#ffffff" :
        labelshow.config(text = "white")
    elif m == "#ffffff" :
        labelshow.config(text = "white")
    elif m == "#9acd32" :
        labelshow.config(text = "yellowgreen")
    elif m == "#ff69b4" :
        labelshow.config(text = "hotpink")
    elif m == "#ffc0cb" :
        labelshow.config(text = "pink")
    elif m == "#00ffff" :
        labelshow.config(text = "cyan")
    elif m == "#00ff00" :
        labelshow.config(text = "lime")
        
def new(btnr,btng,btngy,btnw,btny,btnp,btnhp,btnm,btnc,btnyg,btnl,lab,textb):
    btnr.config(bg="#333333")
    btng.config(bg="#333333")
    btngy.config(bg="#333333")
    btnw.config(bg="#333333")
    btny.config(bg="#333333")
    btnp.config(bg="#333333")
    btnhp.config(bg="#333333")
    btnm.config(bg="#333333")
    btnc.config(bg="#333333")
    btnyg.config(bg="#333333")
    btnl.config(bg="#333333")
    lab.config(bg="#636363")
    lab.config(text="Choice color")
    textb.delete(0,END)

def cut(textb):
    root.clipboard_clear()
    root.clipboard_append(textb.get())
    textb.delete(0,END)

def copy(textb):
    root.clipboard_clear()
    root.clipboard_append(textb.get())

def paste(textb):
    textC = root.clipboard_get()
    textb.insert(0,textC)
    
'''__Start Menu Bar__'''
menubar = Menu(root,fg="white")
file = Menu(menubar, tearoff=False, background="#383838", fg = "#bdbdbd")
edit = Menu(menubar, tearoff=False, background='#383838', fg = "#bdbdbd")
file.add_command(label="New" ,command=lambda:new(btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime,lab,textbox))
file.add_command(label="Exit", accelerator="Alt+F4" , command=root.quit)
edit.add_command(label="Cut", command=lambda:cut(textbox))
edit.add_command(label="Copy",command=lambda:copy(textbox))
edit.add_command(label="Paste",command=lambda:paste(textbox))
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
'''__End Menu Bar__'''


lab = Label(root,text="Choice color",width=50,height=10,bg="#636363")
borderblock = Label(root,width=50,height=1,bg="#424242")
borderblock1 = Label(root,width=50,height=1,bg="#424242")
btnred = Button(root,bg="#333333",padx=50,pady=15,text="red",borderwidth=0,command=lambda:Go(lab,btnred,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btngreen = Button(root,bg="#333333",padx=43.4,pady=15,text="green",borderwidth=0,command=lambda:Go(lab,btngreen,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btngray = Button(root,bg="#333333",padx=47,pady=15,text="gray",borderwidth=0,command=lambda:Go(lab,btngray,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnwhite = Button(root,bg="#333333",padx=43.5,pady=15,text="white",borderwidth=0,command=lambda:Go(lab,btnwhite,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnyellow = Button(root,bg="#333333",padx=41.5,pady=15,text="yellow",borderwidth=0,command=lambda:Go(lab,btnyellow,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnpink = Button(root,bg="#333333",padx=47,pady=15,text="pink",borderwidth=0,command=lambda:Go(lab,btnpink,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnhotpink = Button(root,bg="#333333",padx=38,pady=15,text="hotpink",borderwidth=0,command=lambda:Go(lab,btnhotpink,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnmagenta = Button(root,bg="#333333",padx=35,pady=15,text="magenta",borderwidth=0,command=lambda:Go(lab,btnmagenta,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btncyan = Button(root,bg="#333333",padx=46,pady=15,text="cyan",borderwidth=0,command=lambda:Go(lab,btncyan,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnyellowgreen = Button(root,bg="#333333",padx=27,pady=15,borderwidth=0,text="yellowgreen",command=lambda:Go(lab,btnyellowgreen,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
btnlime = Button(root,padx=47,bg="#333333",pady=15,text="lime",borderwidth=0,command=lambda:Go(lab,btnlime,btnred,btngreen,btngray,btnwhite,btnyellow,btnpink,btnhotpink,btnmagenta,btncyan,btnyellowgreen,btnlime))
textbox = Entry(root,width=20,bg="#a3a3a3",borderwidth=0,highlightthickness=1)
btntextbox = Button(root,bg="#333333",text="Go Color",borderwidth=0,command=lambda:set_color(textbox,lab))
btnclean = Button(root,text="clean")
lab10 = Label(root,bg="#424242",text="Enter The hex code or color name : ")

'''separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.5, rely=0, relwidth=0.1, relheight=1)'''

lab.grid(row=1,column=0)
borderblock.grid(row=2,column=0)
borderblock1.grid(row=14,column=0)
btnred.grid(row=3,column=0)
btngreen.grid(row=4,column=0)
btngray.grid(row=5,column=0)
btnwhite.grid(row=6,column=0)
btnyellow.grid(row=7,column=0)
btnpink.grid(row=8,column=0)
btnhotpink.grid(row=9,column=0)
btnmagenta.grid(row=10,column=0)
btncyan.grid(row=11,column=0)
btnyellowgreen.grid(row=12,column=0)
btnlime.grid(row=13,column=0)
textbox.grid(row=16,column=0)
btntextbox.grid(row=17,column=0)
btnclean.grid(row=19,column=1)
lab10.grid(row=15,column=0)

textbox.config(highlightbackground = "#666666", highlightcolor= "#666666")



root.config(menu=menubar)
mainloop()
