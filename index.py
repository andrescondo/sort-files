# < andreescondo@gmail.com  Andres Condo>
from glob import glob
from os import walk
import pathlib
import shutil
import os

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
					

		# if os.path.isdir(file[count]) == os.path:
		# 	print('hola mundo')
		count+=1
	print(os.path.isdir('py'))



def run():
	mkdir()

	#======= VERIFICAR LOS ELEMENTOS DE LA CARPETA=======
	dire, subdirs, archi = next(walk('.'))
	print("Actual: ", dire)
	print("Subdirectorios: ", subdirs)
	print("Archivos: ", archi)
	#====================================================
	# algo = os.path.splitext(archi[0])[0]
	# print(algo)

	for folder in subdirs:
		print(folder)
		for file in archi:
			print('--',file,'---')


	

	# shutil.move('{}.txt'.format(algo), 'txt')



if __name__ == '__main__':
	run()