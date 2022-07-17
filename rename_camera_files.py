import os
import sys
from PIL import Image

def get_date(filepath):
	image = Image.open(filepath)
	exifdata = image.getexif()
	
	# tag_id = 306 is "DateTime" per EXIF standard
	date = image.getexif()[306]
	
	return date
	
def rename_file(filepath, datetime):
	(dir, name) = os.path.split(filepath)
	tidied_dt = datetime.replace(':', '').replace(' ', '_')
	final_name = name.split('_', 1)[0] + '_' + tidied_dt
	final_path = f"{dir}/{final_name}{os.path.splitext(filepath)[1]}"
	os.rename(filepath, final_path)
	return final_path

def rename_files(filepath, verbose=False):
	# If the provided path leads to a dictionary, rename files in it
	if os.path.isdir(filepath):
		valid_extensions = ['.jpg', '.nef', '.crw', '.cr2', '.cr3', '.hif', '.mov', '.mp4', '.mxf', '.mts', '.crm', '.rmf', '.thm', '.wav']
		print(f"Renaming files in the directory: {filepath}")
		for entry in os.scandir(filepath):
			entrypath = entry.path
			if entry.is_file() and os.path.splitext(entrypath)[1].lower() in valid_extensions:
				datetime = get_date(entrypath)
				if verbose == True:
					print(f"{entry.name} to {os.path.basename(rename_file(entrypath, datetime))}")
				else:
					rename_file(entrypath, datetime)
	# If the provided path leads to a file, rename the file
	elif os.path.isfile(filepath):
		datetime = get_date(filepath)
		if verbose == True:
			print(f"Renaming file: {os.path.basename(filepath)} to {os.path.basename(rename_file(filepath, datetime))}")
		else:
			rename_file(filepath, datetime)
	else:
		print("Incorrect filepath or file doesn't exist. Skipping.")