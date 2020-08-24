# < andreescondo@gmail.com  Andres Condo>
import datetime
import os
# frocomm os.path import isfile, isdir
import glob
import pathlib


def run():
	print('''
	********************************************
	*    Separando los archivos en carpetas    *
	********************************************
	''')

	example_dir = './'
	file = []

	directory = pathlib.Path(example_dir)
	for fichero in directory.iterdir():
		file.append(os.path.splitext(fichero.name)[1])


		# for i in file:
		if not os.path.isdir(file[fichero]):
			os.mkdir()
		print('creado carpeta')
	print(file)








if __name__ == '__main__':
	run()