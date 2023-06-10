import tkinter as tk
from tkinter import *
from tkinter import ttk


def add_task():
    if not entry_line.get() == '':
        text = entry_line.get()
        current_todos.insert(tk.END, text)
        main_frame.update()
    else:
        return 'enter the task'
    
def delete_task():
    if current_todos.curselection():
        selected_task = current_todos.curselection()
        current_todos.delete(selected_task)
        finished_todos.delete(selected_task)

def update_task():
    selected_task = current_todos.curselection()
    if not entry_line.get() == '' and selected_task:
        current_todos.delete(selected_task)
        current_todos.insert(selected_task, entry_line.get())

def finish_task():
    if current_todos.curselection():
        selected_to_finish = current_todos.curselection()
        finished_todos.insert(tk.END, current_todos.get(selected_to_finish))
        current_todos.delete(selected_to_finish)


'''ЗАПУСК ГЛАВНОГО ОКНА'''
main_frame = tk.Tk()
main_frame.configure(bg='#6fffd9')
main_frame.wm_resizable(False,False)
main_frame.title('My List')

'''ПОЛЕ ВВОДА'''
entry_line = tk.Entry(main_frame, width=50, bg='blue')
entry_line.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)

ttk.Style().configure(".",  font="helvetica 13", foreground="white", background="#6fffd9")
add_button = ttk.Button(main_frame, text='add', command=add_task)
add_button.grid(row=0, column=0, sticky=EW, padx=5, pady=5, )
delete_button = ttk.Button(main_frame, text='delete', command=delete_task)
delete_button.grid(row=0, column=1, sticky=EW, padx=5, pady=5)
update_button = ttk.Button(main_frame, text='update', command=update_task)
update_button.grid(row=0, column=2, sticky=EW, padx=5, pady=5)
finish_button = ttk.Button(main_frame, text='finish', command=finish_task)
finish_button.grid(row=1, column=2, sticky=EW, padx=5, pady=5)

'''СПИСОК ТЕКУЩИХ ТУДУ'''
current_todos = Listbox(bg='blue', selectforeground='#00ff00')
current_todos.grid(row=2, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
'''ПОЛЕ ЗАВЕРШЕННЫХ ТУДУ'''
finished_todos = Listbox(bg='blue', selectforeground='#00ff00')
finished_todos.grid(row=3, column=0, columnspan=2, sticky=EW, padx=5, pady=5)

main_frame.mainloop()