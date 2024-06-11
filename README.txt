File Synchronization Tool with Tkinter GUI

This Python script provides a simple file synchronization tool with a graphical user interface (GUI) built using Tkinter. It allows you to synchronize files and directories from an internal folder to an external folder, ensuring that any modifications or new files in the internal folder are copied to the external folder.

Usage

Setup:

Ensure you have Python installed on your system.
Install the necessary dependencies (tkinter should be included with Python by default).
Configuration:

Define the paths to your internal and external folders within the script.
- The internal_folder should contain the files and directories you want to synchronize.
- The external_folder is where the synchronized files will be copied to.


Execution:

- Run the script.
- The GUI window will display the progress of the synchronization process.
- Once synchronization is complete, a message box will inform you whether any files were copied.


Features
- Recursively synchronizes files and subdirectories from the internal folder to the external folder.
- Creates subdirectories in the external folder if they do not exist.
- Copies only modified or new files from the internal folder to the external folder.
- Provides progress updates during the synchronization process via a progress bar.


Error Handling
- Raises an error if the specified internal or external folder does not exist or is not a directory.
- Displays error messages in the console for easy debugging.


Notes
Ensure that the script has appropriate permissions to read from and write to the internal and external folders.
This script is suitable for basic file synchronization tasks. For more complex scenarios or larger datasets, consider using specialized synchronization tools.
