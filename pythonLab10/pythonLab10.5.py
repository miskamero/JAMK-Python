import ctypes
import os
import platform

def is_admin():
	if platform.system() == 'Windows':
		try:
			return ctypes.windll.shell32.IsUserAnAdmin() != 0
		except AttributeError:
			return os.getuid() == 0
	else:
		return os.getuid() == 0

if not is_admin():
	print("Et ole admin")
	exit()

if platform.system() == 'Windows':
	path = "C:\\"
elif platform.system() == 'Linux':
	path = "/home/"
elif platform.system() == 'Darwin':
	path = "/Users/"
else:
	print("Tuntematon käyttöjärjestelmä")
	exit()

file_path = os.path.join(path, "tekstiTiedosto.txt")
with open(file_path, "w") as f:
	f.write("Testi1\n")
