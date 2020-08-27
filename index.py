# < andreescondo@gmail.com  Andres Condo>
from os import walk
import pathlib
import shutil
import os


def move():
	dire, subdirs, archi = next(walk('.'))
	for folder in subdirs:
		for file in archi:
			if folder == os.path.splitext(file)[1].lstrip('.'):
				print('Moviendo... {}'.format(file))
				shutil.move(file, folder)


def mkdir():
	print('''
	********************************************
	*    Creando Carpetas de los Archivos	   *
	********************************************
	''')
	dir_actual = './'
	file = []
	count = 0

	directory = pathlib.Path(dir_actual)
	for fichero in directory.iterdir():
		file.append(os.path.splitext(fichero.name)[1].lstrip('.'))
		if not os.path.isdir(file[count]):
			if not file[count] == '':
				if not file[count] == 'py':
					os.mkdir(file[count])

		count+=1
		
	move()


def run():
	mkdir()


if __name__ == '__main__':
	run()