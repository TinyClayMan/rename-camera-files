# Description 
A simple tool to change standard camera file namings.

<b>Important notice:</b> This tool works correctly only if your files have an underscore in the middle of their name.

Example:

DSC_NNNN.JPG to DSC_YYYYMMDD_HHMMSS.JPG

# Usage

To use, either import rename_camera_files in your own code or activate the main.py file and follow the instructions:

> python main.py

# How it works

It takes a file, gets its metadata tag relating to date and time of creation and changes the file name, replacing the iterative number with date and time.