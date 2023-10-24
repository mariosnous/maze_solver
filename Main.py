# ADD MORE FUNCTIONALITY


import sys
import tkinter as tk
from Graphics import Window
from Maze import Maze


def main():
    def create_maze():
        num_rows = int(rows_entry.get())
        num_cols = int(cols_entry.get())
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        sys.setrecursionlimit(10000)
        win = Window(screen_x, screen_y)

        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
        print(f"{num_rows} x {num_cols} maze created")

        is_solvable = maze.solve()
        if not is_solvable:
            print("maze can not be solved!")
        else:
            print("maze solved!")

    root = tk.Tk()
    root.title("Maze Generator")
    root.protocol("WM_DELETE_WINDOW", root.quit)

    create_maze_button = tk.Button(root, text="Create Maze", command=create_maze)
    create_maze_button.pack()

    rows_label = tk.Label(root, text="Rows:")
    rows_label.pack()
    rows_entry = tk.Entry(root)
    rows_entry.pack()

    cols_label = tk.Label(root, text="Columns:")
    cols_label.pack()
    cols_entry = tk.Entry(root)
    cols_entry.pack()

    root.mainloop()


main()
