# < andreescondo@gmail.com  Andres Condo>
import datetime
import os
# frocomm os.path import isfile, isdir
import glob
import pathlib
from os import walk



def run():
	print('''
	********************************************
	*    Separando los archivos en carpetas    *
	********************************************
	''')

	example_dir = './'
	file = []
	File = []
	count = 0

#======= VERIFICAR LOS ELEMENTOS DE LA CARPETA=======
	dire, subdirs, archi = next(walk(example_dir))
	print("Actual: ", dire)
	print("Subdirectorios: ", subdirs)
	print("Archivos: ", archi)
#====================================================

	directory = pathlib.Path(example_dir)
	for fichero in directory.iterdir():
		file.append(os.path.splitext(fichero.name)[1].lstrip('.'))

		if not os.path.isdir(file[count]):
			if not file[count] == '':
				if not file[count] == 'py':
					os.mkdir(file[count])

		# if file[count] == os

		count+=1


		# print(fichero)
	# print(file)




		# # for i in file:
		# if not os.path.isdir(file[fichero]):
		# 	os.mkdir()
		# print('creado carpeta')


if __name__ == '__main__':
	run()