import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import time

bye_snake_ascii_art = """$$\                          $$\ 
$$ |                         $$ |
$$$$$$$\  $$\   $$\  $$$$$$\ $$ |
$$  __$$\ $$ |  $$ |$$  __$$\$$ |
$$ |  $$ |$$ |  $$ |$$$$$$$$ \__|
$$ |  $$ |$$ |  $$ |$$   ____|   
$$$$$$$  |\$$$$$$$ |\$$$$$$$\$$\ 
\_______/  \____$$ | \_______\__|
          $$\   $$ |             
          \$$$$$$  |             
           \______/              """
snake_ascii_art = """██████  ███▄    █  ▄▄▄       ██ ▄█▀▓█████ 
▒██    ▒  ██ ▀█   █ ▒████▄     ██▄█▒ ▓█   ▀ 
░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓███▄░ ▒███   
  ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ 
▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ █▄░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░
░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░
░  ░  ░     ░   ░ ░   ░   ▒   ░ ░░ ░    ░   
      ░           ░       ░  ░░  ░      ░  ░"""


snake = [(100,100),(100,110),(100,120),(100,130),(100,140)]
direction = 'r'
game_canvas_size_w = 650
game_canvas_size_h = 420
timer_run_flag = True


# функция для обновления секундомера
def update_timer(start_time, timer_label):
        global root_tk
        elapsed_time = datetime.now() - start_time
        hours, remainder = divmod(elapsed_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        timer_label.configure(text=formatted_time)

# эта функция чистит главное меню(кнопки фреймы и т.д)
def destroy_menu():
    main_menu_frame.destroy()
    main_menu_title.destroy()
    start_button.destroy()
    test_button.destroy()
    exit_button.destroy()

# промежуточная функция для выхода из игры
def exit_step():
    destroy_menu()
    global snake_ascii_art
    ctk.CTkLabel(master=root_tk, text=bye_snake_ascii_art, font=("Courier New", 15)).grid(row=0, column=0, padx=200, pady=300)
    bye_button = ctk.CTkButton(master=root_tk, text='bye!',
                            corner_radius=0,
                            border_width=5,
                            border_spacing=15,
                            fg_color='#819c8d',
                            hover_color=('#abb9b1','#819c8d'),
                            border_color=('#819c8d','#819c8d'),
                            command=lambda: quit()
                            )
    bye_button.grid(row=0, column=0, pady=(0, 200))

# функция запуска игры
def start_game():
    destroy_menu()
    start_time = datetime.now()
    main_menu_frame = ctk.CTkFrame(master=root_tk, width=680, height=480)
    main_menu_frame.configure(fg_color="#abb9b1")
    main_menu_frame.grid(padx=10, pady=10,
                        row=0, column=0)
    
    global segment_size
    segment_size = 10
    
    global game_canvas
    game_canvas = ctk.CTkCanvas(master=root_tk, width=game_canvas_size_w, height=game_canvas_size_h, bg='#819c8d')
    game_canvas.grid(row=0, column=0, padx=(0,0), pady=(30,0))

    timer_label = tk.Label(root_tk, text="00:00:00", font=("Courier New", 20), fg="#819c8d")
    timer_label.grid(row=0, column=0,
                padx=(450,0), pady=(0,437))
    
    update_timer(start_time, timer_label)
    
    snake_update(start_time, timer_label)

# функция отрисовки меню
def draw_menu():
    global main_menu_frame
    global main_menu_title
    global start_button
    global test_button
    global exit_button

    main_menu_frame = ctk.CTkFrame(master=root_tk, width=680, height=480)
    main_menu_frame.configure(fg_color="#abb9b1")
    main_menu_frame.grid(padx=10, pady=10,
                        row=0, column=0)

    main_menu_title = ctk.CTkLabel(master=root_tk, text=snake_ascii_art, bg_color='#abb9b1')
    main_menu_title.configure(width=100, height=20, font=("Courier New", 15), corner_radius=5)
    main_menu_title.grid(row=0, column=0, pady=(0, 300))

    start_button = ctk.CTkButton(root_tk, text='START GAME',
                                corner_radius=0,
                                border_width=5,
                                border_spacing=15,
                                fg_color=('#abb9b1','#abb9b1'),
                                hover_color=('#819c8d','#abb9b1'),
                                border_color=('#abb9b1','#abb9b1'),
                                command=start_game
                                )

    test_button = ctk.CTkButton(root_tk, text='TEST',
                                corner_radius=0,
                                border_width=5,
                                border_spacing=15,
                                fg_color=('#abb9b1','#abb9b1'),
                                hover_color=('#819c8d','#abb9b1'),
                                border_color=('#abb9b1','#abb9b1')
                                )

    exit_button = ctk.CTkButton(root_tk, text='EXIT',
                                corner_radius=0,
                                border_width=5,
                                border_spacing=15,
                                fg_color=('#abb9b1','#abb9b1'),
                                hover_color=('#819c8d','#abb9b1'),
                                border_color=('#abb9b1','#abb9b1'),
                                command=exit_step
                                )

    start_button.grid(row=0, column=0, pady=(0, 50))
    test_button.grid(row=0, column=0, pady=(75, 0))
    exit_button.grid(row=0, column=0, pady=(200, 0))

def draw_snake():
    game_canvas.delete(ctk.ALL)
    for x, y in snake:
        rect = game_canvas.create_rectangle(x, y, x+segment_size, y+segment_size, fill='#a9bbb1')

def move():
    global timer_run_flag
    x, y = snake[0]
        
    if direction == "u":
        y -= segment_size
    elif direction == "d":
        y += segment_size
    elif direction == "l":
        x -= segment_size
    elif direction == "r":
        x += segment_size

    # обработка столкновения со змейкой
    if (x,y) in snake[1:] or x > game_canvas_size_w-segment_size or y > game_canvas_size_h-segment_size or x < 0 or y < 0:
        ctk.CTkLabel(root_tk, text="GAME OVER", bg_color='#abb9b1', font=("Courier New", 40)).grid(row=0, column=0)
        timer_run_flag = False
        
        root_tk.bind("<KeyPress>", block_keyboard)
        return 

    snake.insert(0, (x, y))
    snake.pop()

def block_keyboard(event):
    key = event.keysym

def on_key_press(event):
    key = event.keysym
    global direction

    if key == "Up" and direction != "d":
        direction = "u"
    elif key == "Down" and direction != "u":
        direction = "d"
    elif key == "Left" and direction != "r":
        direction = "l"
    elif key == "Right" and direction != "l":
        direction = "r"

def snake_update(start_time, timer_label):
    if timer_run_flag:
        root_tk.after(1000, update_timer, start_time, timer_label)

    move()
    draw_snake()
    root_tk.after(100, snake_update, start_time, timer_label)

root_tk = tk.Tk()
root_tk.geometry("700x500")
root_tk.title('Snake game')
root_tk.configure(bg='#819c8d')
root_tk.resizable(False, False)
root_tk.bind("<KeyPress>", on_key_press)

draw_menu()

root_tk.mainloop()