import tkinter as tk
from tkinter import filedialog
import os

def split_file(input_file, num_parts):
    try:
        with open(input_file, 'rb') as f:
            content = f.read()
            total_size = len(content)
            part_size = total_size // num_parts

            for i in range(num_parts):
                start = i * part_size
                end = (i + 1) * part_size if i < num_parts - 1 else total_size

                output_file = f"{os.path.splitext(input_file)[0]}_part{i + 1}.txt"
                with open(output_file, 'wb') as part_file:
                    part_file.write(content[start:end])

        print(f"File split into {num_parts} parts successfully.")
    except Exception as e:
        print(f"Error splitting file: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def split_button_click():
    input_file = file_entry.get()
    num_parts = int(parts_entry.get())

    if os.path.isfile(input_file) and num_parts > 0:
        split_file(input_file, num_parts)
    else:
        print("Invalid input. Please provide a valid file and a positive number of parts.")

# Create main window
root = tk.Tk()
root.title("File Splitter")

# File Entry
file_label = tk.Label(root, text="Select File:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5)

file_button = tk.Button(root, text="Browse", command=browse_file)
file_button.grid(row=0, column=2, padx=5, pady=5)

# Number of Parts Entry
parts_label = tk.Label(root, text="Number of Parts:")
parts_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

parts_entry = tk.Entry(root)
parts_entry.grid(row=1, column=1, padx=5, pady=5)

# Split Button
split_button = tk.Button(root, text="Split File", command=split_button_click)
split_button.grid(row=2, column=1, pady=10)

# Run the Tkinter event loop
root.mainloop()