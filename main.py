from tkinter import *
import speedtest as s
def speedcheck():
  sp = s.Speedtest()
  sp.get_servers()
  down = str(round(sp.download()/(10**6),3)) + "Mbps"
  up = str(round(sp.upload()/(10**6),3)) + "Mbps"
  lab_down.config(text=down)
  lab_up.config(text=up)
root = Tk()
root.title("Internet Speed Test")
root.geometry("500x650")
lab = Label(root, text="Internet Speed Test", font=("Time New Roman", 20, "bold"))
lab.place(x=30,y=60,height=20,width=300)
lab = Label(root, text="Download speed", font=("Time New Roman", 18, "bold"))
lab.place(x=30,y=130,height=60,width=300)
lab_down = Label(root, text="00", font=("Time New Roman", 18, "bold"))
lab_down.place(x=30,y=200,height=62,width=300)
lab = Label(root, text="Upload speed", font=("Time New Roman", 18, "bold"))
lab.place(x=30,y=250,height=80,width=300)
lab_up = Label(root, text="00", font=("Time New Roman", 18, "bold"))
lab_up.place(x=30,y=320,height=82,width=300)
button = Button(root, text="Check Speed", font=("Time New Roman", 18, "bold"),bg="gray", relief=RAISED, command=speedcheck)
button.place(x=70,y=420,height=70,width=230)
root.mainloop()
