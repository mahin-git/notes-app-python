import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE = "notes.json"

# Load notes from file
def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save notes to file
def save_notes():
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note():
    title = simpledialog.askstring("Title", "Enter note title:")
    if title:
        content = text_area.get("1.0", tk.END).strip()
        notes[title] = content
        save_notes()
        refresh_notes()
        text_area.delete("1.0", tk.END)

def load_note(event):
    if listbox.curselection():  #
        selected = listbox.get(listbox.curselection())
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, notes[selected])

def delete_note():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        confirm = messagebox.askyesno("Delete", f"Delete note '{selected}'?")
        if confirm:
            del notes[selected]
            save_notes()
            refresh_notes()
            text_area.delete("1.0", tk.END)

def refresh_notes():
    listbox.delete(0, tk.END)
    for title in notes:
        listbox.insert(tk.END, title)

# Main GUI
root = tk.Tk()
root.title("Notes App")
root.geometry("700x450")

notes = load_notes()

# Layout
listbox = tk.Listbox(root, width=30)
listbox.pack(side="left", fill="y")
listbox.bind("<<ListboxSelect>>", load_note)

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(side="left", fill="both", expand=True)

frame = tk.Frame(root)
frame.pack(side="bottom", fill="x")

tk.Button(frame, text="Save Note", command=add_note).pack(side="left", padx=5, pady=5)
tk.Button(frame, text="Delete Note", command=delete_note).pack(side="left", padx=5, pady=5)

refresh_notes()
root.mainloop()
