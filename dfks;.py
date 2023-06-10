import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
DELAY = 100
SNAKE_SIZE = 20

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.window.bind("<KeyPress>", self.on_key_press)
        
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        
        self.update()
        
    def create_food(self):
        x = random.randint(1, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(1, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        return x, y
    
    def draw(self):
        self.canvas.delete(tk.ALL)
        
        # Рисуем змейку
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="white")
        
        # Рисуем еду
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE, fill="red")
        
        # Отображаем счет
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", anchor="nw")
        
    def move(self):
        x, y = self.snake[0]
        
        if self.direction == "Up":
            y -= SNAKE_SIZE
        elif self.direction == "Down":
            y += SNAKE_SIZE
        elif self.direction == "Left":
            x -= SNAKE_SIZE
        elif self.direction == "Right":
            x += SNAKE_SIZE
            
        self.snake.insert(0, (x, y))
        
        # Проверяем столкновение со стенкой
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            self.game_over()
            return
        
        # Проверяем столкновение с самой змейкой
        if (x, y) in self.snake[1:]:
            self.game_over()
            return
        
        # Проверяем столкновение с едой
        if (x, y) == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()
        
    def update(self):
        self.move()
        self.draw()
        self.window.after(DELAY, self.update)
        
    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 20), anchor="center")
        
    def on_key_press(self, event):
        key = event.keysym
        
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.window.mainloop()