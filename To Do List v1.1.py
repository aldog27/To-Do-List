from tkinter import *
import tkinter.messagebox

# Create window and title
window = Tk()
window.title("Python To-Do List")

# Use frame to hold the listbox and scrollbar
frame_task = Frame(window)
frame_task.pack()

# Hold items in a listbox
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font = "Helvetica")
listbox_task.pack(side = tkinter.LEFT)

# Scrolldown in case size of list exceeds window
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side = tkinter.RIGHT, fill = tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#Define list
x = []

# Define functions   

def disablebuttons():
    entry_button['state'] = 'disabled' 
    delete_button['state'] = 'disabled' 
    mark_button['state'] = 'disabled' 
    edit_button['state'] = 'disabled' 
    delall_button['state'] = 'disabled' 

def enablebuttons():
    entry_button['state'] = 'normal' 
    delete_button['state'] = 'normal' 
    mark_button['state'] = 'normal' 
    edit_button['state'] = 'normal' 
    delall_button['state'] = 'normal' 

#Function when user closes window with X
def onclosing():
    enablebuttons()
    pass


def entertask():
    #A new window to pop up to take input
    input_text=""
    disablebuttons()
    #Check if list has 3 items
    if len(x)>2:
        tkinter.messagebox.showwarning(title="Warning!",message="You Already Have 3 Tasks")
        enablebuttons()
    else:
        def add():
            input_text=entry_task.get(1.0, "end-1c")
            if input_text=="":
                tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
            else:
                listbox_task.insert(END,input_text)
                #add 1 to list counter
                x.append(1)
                #enable buttons
                enablebuttons()
                #close the root1 window
                root1.destroy()
        root1=Tk()
        root1.title("Add task")
        entry_task=Text(root1,width=40,height=4)
        entry_task.pack()
        button_temp=Button(root1,text="Add task",command=add)
        button_temp.pack()
        root1.protocol("WM_DELETE_WINDOW", onclosing())
        root1.mainloop()


# Function to delete task
def deletetask():
    selected=listbox_task.curselection()
    if len(selected)==0:
        pass
    else:
        listbox_task.delete(selected[0])
        if len(x)==0:
            pass
        else:
            x.pop()

# Function to mark completed
def markcompleted():
    marked=listbox_task.curselection()
    if len(marked)==0:
        pass
    else:
        temp=marked[0]
        # Store the text of the selected item in a string
        temp_marked=listbox_task.get(marked)
        isDone=temp_marked[len(temp_marked)-6:]
        # Check if task already marked complete
        if isDone==" DONE!":
            pass
        else:
            # Update it
            temp_marked=temp_marked + " DONE!"
            # Delete it and insert it
            listbox_task.delete(temp)
            listbox_task.insert(temp,temp_marked)


def edittask():
    marked=listbox_task.curselection()
    if len(marked)==0:
        pass
    else:
        disablebuttons()
        temp=marked[0]
        temp_marked=listbox_task.get(marked)
        def add():
            temp_marked=entry_task.get(1.0, "end-1c")
            if temp_marked=="":
                tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
            else:
                #inserts new edited task
                listbox_task.insert(END,temp_marked)
                #deletes the old task
                listbox_task.delete(marked[0])
                enablebuttons()
                root1.destroy()
        root1=Tk()
        root1.title("Edit task")
        entry_task=Text(root1,width=40,height=4)
        #edit the selected task
        entry_task.insert("end",temp_marked)
        entry_task.pack()
        button_temp=Button(root1,text="Edit task",command=add)
        button_temp.pack() 
        #Activates when window is closed with X
        root1.protocol("WM_DELETE_WINDOW", onclosing())
        root1.mainloop()

def deleteall():
    listbox_task.delete(0, END)
    x.clear()

# Button widgets

entry_button=Button(window,text="Add task",width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed", width=50,command=markcompleted)
mark_button.pack(pady=3)

markun_button=Button(window,text="Mark as uncompleted", width=50)
markun_button.pack(pady=3)

edit_button=Button(window,text="Edit selected task", width=50,command=edittask)
edit_button.pack(pady=3)

delall_button=Button(window,text="Delete all tasks", width=50,command=deleteall)
delall_button.pack(pady=3)

window.mainloop()



            

