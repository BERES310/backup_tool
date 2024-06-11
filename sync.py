import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox

def sync(internal_folder, external_folder):
    try:
        if not os.path.exists(internal_folder) or not os.path.isdir(internal_folder):
            raise FileNotFoundError(f"Internal folder '{internal_folder}' does not exist or is not a directory.")

        if not os.path.exists(external_folder) or not os.path.isdir(external_folder):
            os.makedirs(external_folder)  # Create the external folder if it doesn't exist

        need_to_copy = False

        window = tk.Tk()
        window.title("Backup Progress")
        window.geometry("300x100")

        progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
        progress_bar.pack(pady=10)

        progress_label = tk.Label(window, text="")
        progress_label.pack()

        total_files = sum(len(files) for _, _, files in os.walk(internal_folder))
        copied_files = 0

        for root, _, files in os.walk(internal_folder):
            for file in files:
                internal_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(internal_file_path, internal_folder)
                external_file_path = os.path.join(external_folder, relative_path)

                external_file_dir = os.path.dirname(external_file_path)
                if not os.path.exists(external_file_dir):
                    os.makedirs(external_file_dir)  # Create the subdirectory in the external folder if it doesn't exist

                if os.path.exists(external_file_path):
                    internal_mtime = os.path.getmtime(internal_file_path)
                    external_mtime = os.path.getmtime(external_file_path)
                    if internal_mtime > external_mtime:
                        shutil.copy(internal_file_path, external_file_path)
                        copied_files += 1
                        need_to_copy = True
                else:
                    shutil.copy(internal_file_path, external_file_path)
                    copied_files += 1
                    need_to_copy = True

                progress = int((copied_files / total_files) * 100)
                progress_bar["value"] = progress
                progress_label.config(text=f"{progress}%")
                window.update()

        window.destroy()

        if not need_to_copy:
            messagebox.showinfo("Backup Info", "All files are up to date. No need to copy.")
        else:
            messagebox.showinfo("Backup Info", "Backup completed successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Paste your internal folder path here
internal_folder = " "

# Paste your external folder path here
external_folder = " "

# Call the function to create a backup
sync(internal_folder, external_folder)


