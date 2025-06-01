import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import os


def filter_and_sort_passwords(input_path, output_path, options):
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    passwords = set([line.strip() for line in lines]) if options['remove_duplicates'] else [line.strip() for line in lines]

    def is_valid(pw):
        if len(pw) < options['min_length']:
            return False
        if options['max_length'] and len(pw) > options['max_length']:
            return False
        if options['only_alpha'] and not pw.isalpha():
            return False
        if options['only_numeric'] and not pw.isdigit():
            return False
        if options['only_alnum'] and not pw.isalnum():
            return False
        if options['no_special'] and not pw.isalnum():
            return False
        return True

    filtered = [pw for pw in passwords if is_valid(pw)]

    # Sort options
    if options['sort'] == 'Alphabetical':
        filtered.sort()
    elif options['sort'] == 'By Length':
        filtered.sort(key=len)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(filtered))

    return len(lines), len(filtered)


def run():
    input_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not output_file:
        return

    try:
        min_length = int(min_len_var.get())
        max_length = int(max_len_var.get()) if max_len_var.get() else None

        options = {
            'min_length': min_length,
            'max_length': max_length,
            'only_alpha': alpha_var.get(),
            'only_numeric': numeric_var.get(),
            'only_alnum': alnum_var.get(),
            'no_special': no_special_var.get(),
            'remove_duplicates': dedupe_var.get(),
            'sort': sort_var.get(),
        }

        total, kept = filter_and_sort_passwords(input_file, output_file, options)

        messagebox.showinfo("Done", f"Original: {total} lines\nFiltered: {kept} lines\nSaved to:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("Filter + Sort Password File")
root.geometry("400x450")

tk.Label(root, text="Minimum Length:").pack()
min_len_var = tk.StringVar(value="8")
tk.Entry(root, textvariable=min_len_var).pack()

tk.Label(root, text="Maximum Length (optional):").pack()
max_len_var = tk.StringVar()
tk.Entry(root, textvariable=max_len_var).pack()

tk.Label(root, text="Filters:").pack(pady=(10, 0))
alpha_var = tk.BooleanVar()
tk.Checkbutton(root, text="Only alphabetic", variable=alpha_var).pack()

numeric_var = tk.BooleanVar()
tk.Checkbutton(root, text="Only numeric", variable=numeric_var).pack()

alnum_var = tk.BooleanVar()
tk.Checkbutton(root, text="Only alphanumeric", variable=alnum_var).pack()

no_special_var = tk.BooleanVar()
tk.Checkbutton(root, text="No special characters", variable=no_special_var).pack()

dedupe_var = tk.BooleanVar()
tk.Checkbutton(root, text="Remove duplicates", variable=dedupe_var).pack()

tk.Label(root, text="Sort by:").pack(pady=(10, 0))
sort_var = tk.StringVar(value="Alphabetical")
ttk.Combobox(root, textvariable=sort_var, values=["Alphabetical", "By Length"]).pack()

tk.Button(root, text="Choose File, Filter & Save", command=run, bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
