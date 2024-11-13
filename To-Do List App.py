from tkinter import *
from tkinter import messagebox
from tkinter import ttk

tasks = []
def add_task():
    task = task_field.get()
    if len(task) == 0:
        messagebox.showinfo('Error', "Field is Empty.")
    else:
        tasks.append(task)
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected.Cannot Delete.')

def delete_all_task():
        if len(tasks) != 0:
            message_box = messagebox.askyesno("Delete All", 'Are you sure?')
            if message_box == True:
                while (len(tasks)!=0):
                    tasks.pop()
                list_update()
        else:
            messagebox.showinfo('Error','No Task Available')


def clear_list():
    task_listbox.delete(0,'end')

def close():
    print(tasks)
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("To-Do List Program")
    root.geometry("500x500")
    root.resizable(0,0)
    root.configure(bg = '#FAEBD7')

    header_frame = Frame(root, bg = '#FAEBD7')
    function_frame = Frame(root, bg = '#FAEBD7')
    tasklistbox_frame = Frame(root, bg = '#FAEBD7')

    header_frame.pack(fill = 'both')
    function_frame.pack(side = 'left', fill = 'both', expand = True)
    tasklistbox_frame.pack(side = 'right', fill = 'both', expand = True)

    header_label = ttk.Label(
        header_frame, text = 'The To-Do List', font = ("Georgia",30),
        background= '#FAEBD7', foreground = '#8B0000'
    )
    header_label.pack(pady = 20, padx = 20)

    task_label = ttk.Label(
        function_frame, text = 'Enter A Task', font = ("Roman Times New",'11', 'bold'),
        background= '#FAEBD7', foreground = '#000000'
    )

    task_label.place(x = 30, y = 40)

    task_field = ttk.Entry(
        function_frame, font = ("Consolas",'11'),
        width = 18, background = '#FFF8DC', foreground = '#8B4513'
    )

    task_field.place(x = 30, y = 80)

    add_button = ttk.Button(
        function_frame, text = 'Add Task',
        command = add_task, 
        width= 24
    )

    del_button = ttk.Button(
        function_frame, text = 'Delete Task',
        command = delete_task, 
        width= 24
    )

    del_all_button = ttk.Button(
        function_frame, text = 'Delete All Task',
        command = delete_all_task,
        width= 24
    )

    exit_button = ttk.Button(
        function_frame, text = 'Exit',
        command = close, 
        width= 24
    )

    add_button.place(x = 30, y= 120)
    del_button.place(x = 30, y = 160)
    del_all_button.place(x = 30 , y = 200)
    exit_button.place(x = 30, y = 240)

    task_listbox = Listbox(
        tasklistbox_frame, width = 26, height = 13,
        selectmode= 'single', font=('Arial', 11), 
        background = '#F5F5DC', foreground = '#000000',
        selectbackground= "#8B4513", selectforeground= '#FFFFFF'
    )
    task_listbox.place(x = 10, y = 20)

    root.mainloop()


