import tkinter as tk
from tkinter import messagebox
import random
from collections import deque

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Game variables
        self.canvas_width = 400
        self.canvas_height = 400
        self.grid_size = 20
        self.snake = deque([(200, 200), (180, 200), (160, 200)])
        self.food = self.spawn_food()
        self.direction = (20, 0)  # Moving right
        self.next_direction = (20, 0)
        self.score = 0
        self.game_over = False
        
        # UI Setup
        self.create_ui()
        
        # Game loop
        self.update_game()
    
    def create_ui(self):
        # Title label
        title_label = tk.Label(self.root, text="🐍 SNAKE GAME 🐍", font=("Arial", 18, "bold"), bg="lightblue")
        title_label.pack(pady=10)
        
        # Canvas for game
        self.canvas = tk.Canvas(
            self.root, 
            width=self.canvas_width, 
            height=self.canvas_height, 
            bg="black",
            highlightthickness=2,
            highlightbackground="darkgreen"
        )
        self.canvas.pack(pady=10)
        self.canvas.focus()
        
        # Score label
        self.score_label = tk.Label(self.root, text=f"Score: 0", font=("Arial", 14, "bold"))
        self.score_label.pack()
        
        # Instructions
        instructions = tk.Label(
            self.root, 
            text="Use Arrow Keys to move | Space to pause | R to restart",
            font=("Arial", 10),
            fg="gray"
        )
        instructions.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        restart_btn = tk.Button(button_frame, text="Restart", command=self.restart_game, width=12, bg="green", fg="white")
        restart_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(button_frame, text="Quit", command=self.root.quit, width=12, bg="red", fg="white")
        quit_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind keys
        self.canvas.bind("<Up>", self.change_direction)
        self.canvas.bind("<Down>", self.change_direction)
        self.canvas.bind("<Left>", self.change_direction)
        self.canvas.bind("<Right>", self.change_direction)
        self.canvas.bind("<r>", lambda e: self.restart_game())
        self.canvas.bind("<space>", self.toggle_pause)
        
        self.paused = False
    
    def spawn_food(self):
        while True:
            x = random.randint(0, (self.canvas_width // self.grid_size) - 1) * self.grid_size
            y = random.randint(0, (self.canvas_height // self.grid_size) - 1) * self.grid_size
            if (x, y) not in self.snake:
                return (x, y)
    
    def change_direction(self, event):
        if self.game_over or self.paused:
            return
        
        key = event.keysym
        new_direction = self.direction
        
        if key == "Up" and self.direction[1] == 0:
            new_direction = (0, -20)
        elif key == "Down" and self.direction[1] == 0:
            new_direction = (0, 20)
        elif key == "Left" and self.direction[0] == 0:
            new_direction = (-20, 0)
        elif key == "Right" and self.direction[0] == 0:
            new_direction = (20, 0)
        
        self.next_direction = new_direction
    
    def toggle_pause(self, event):
        self.paused = not self.paused
    
    def update_game(self):
        if self.game_over or self.paused:
            self.root.after(100, self.update_game)
            return
        
        # Update direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        new_x = head_x + self.direction[0]
        new_y = head_y + self.direction[1]
        new_head = (new_x, new_y)
        
        # Check collisions with walls
        if (new_x < 0 or new_x >= self.canvas_width or 
            new_y < 0 or new_y >= self.canvas_height):
            self.end_game()
            return
        
        # Check collision with itself
        if new_head in self.snake:
            self.end_game()
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.snake.pop()
        
        # Draw game
        self.draw()
        
        # Schedule next update
        self.root.after(100, self.update_game)
    
    def draw(self):
        self.canvas.delete("all")
        
        # Draw food
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx + self.grid_size, fy + self.grid_size, fill="red", outline="darkred")
        
        # Draw snake
        for i, (sx, sy) in enumerate(self.snake):
            if i == 0:  # Head
                self.canvas.create_rectangle(sx, sy, sx + self.grid_size, sy + self.grid_size, fill="lime", outline="green")
            else:  # Body
                self.canvas.create_rectangle(sx, sy, sx + self.grid_size, sy + self.grid_size, fill="green", outline="darkgreen")
    
    def end_game(self):
        self.game_over = True
        messagebox.showinfo("Game Over", f"Game Over!\nFinal Score: {self.score}")
    
    def restart_game(self):
        self.snake = deque([(200, 200), (180, 200), (160, 200)])
        self.food = self.spawn_food()
        self.direction = (20, 0)
        self.next_direction = (20, 0)
        self.score = 0
        self.game_over = False
        self.paused = False
        self.score_label.config(text=f"Score: 0")
        self.draw()
        self.update_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
