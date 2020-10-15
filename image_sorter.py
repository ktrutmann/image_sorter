# A script to quickly sort pictures into different predefined folders

import os
import shutil
import keyboard
from PIL import Image, ImageTk
import tkinter as tk
import threading

# Setup: ---------------------
# All folders are relative to the scripts location
source_folder = 'WhatsApp_Images'

# Where to put the pictures. Use number keys as dict keys.
key_mappings = {'1': 'Keep_On_Phone',
				'2': 'Keep_In_Archive',
				'3': 'To_Be_Deleted'}

# Which filetypes to look for. Must be a tuple.
file_types = ('jpg', 'jpeg', 'png', 'bmp')

# The height in pixels at which the images should be displayed?
img_display_height = 1000


# The choosing runs in a seperate thred: ------
class ChoiceInputThread(threading.Thread):
	captured_key = ''

	def __init__(self, tk_root):
		self.root = tk_root
		threading.Thread.__init__(self)
		self.start()

	def run(self):
		self.root.update_idletasks()
		print('# --------------------')
		print(f'Deciding About picture nr. {pic_ix + 1}: {this_pic_source}:')
		for this_mapping in key_mappings:
			print(f'  {this_mapping} -> {key_mappings[this_mapping]}')
		print('  b -> go back one image')
		print('  a -> apply changes and quit')
		print('  q -> quit without applying changes')

		await_input = True
		while await_input:
			key = keyboard.read_event()
			if key.event_type == 'up':
				key = None

			elif key.name in key_mappings.keys() or\
					key.name in ['a', 'q', 'b']:
				self.captured_key = key.name
				await_input = False

			else:
				print('No function attached to this key.')

		self.root.quit()
		self.root.update_idletasks()


# The interactive part:
# Find Files: ----------------
all_source_files = os.listdir(source_folder)

all_picture_files = [i for i in all_source_files if i.endswith(file_types)]
n_pics = len(all_picture_files)

print(f'{n_pics} files detected')


# Loop over images: --------------
img_window = tk.Tk()
movement_dict = {}

do_apply_changes = True
pic_ix = 0
while pic_ix < n_pics:
	this_pic_source = all_picture_files[pic_ix]

	# Set up image
	this_pic = Image.open(os.path.join(
			source_folder, this_pic_source))
	this_ratio = this_pic.width / this_pic.height
	this_pic = this_pic.resize(
		(int(img_display_height * this_ratio), img_display_height))
	this_tk_pic = ImageTk.PhotoImage(this_pic)

	# Opening the Image and starting the choice thread
	lbl = tk.Label(img_window, image = this_tk_pic)
	lbl.pack()
	choice_input = ChoiceInputThread(img_window)
	img_window.mainloop()
	lbl.destroy()
	this_pic.close()

	# Evaluating the decision
	if choice_input.captured_key == 'q':
		should_quit = input('\nAre you sure you want to quit without applying '
			'the changes.\nType yes to quit, anything else to continue: ')
		print(should_quit)
		if should_quit == 'yes':
			do_apply_changes = False
			print('\nWe\'re done here.')
			break
		else:
			print('\nMoving on...')

	elif choice_input.captured_key == 'a':
		break

	elif choice_input.captured_key == 'b':
		if pic_ix > 0:
			print('\nOkay, going back one image')
			pic_ix -= 1
		else:
			print('\nThis is the first picture\n')

	else:
		movement_dict[this_pic_source] = key_mappings[choice_input.captured_key]
		print(f'\nSet to move to {key_mappings[choice_input.captured_key]}')
		pic_ix += 1
		if pic_ix == n_pics:
			print('And that was the last one!')

img_window.destroy()
if do_apply_changes:
	print('\nMoving your files')
	for this_pic in movement_dict:
		source = os.path.join(source_folder, this_pic)
		destination = os.path.join(movement_dict[this_pic], this_pic)
		shutil.move(source, destination)
		print(f'Moved {this_pic} to {movement_dict[this_pic]}')
	print('All done!')