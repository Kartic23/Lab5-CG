# credits: Margarida Moura, CGr 2022
#
"""Read vertices from OBJ file"""
from typing import List

def my_obj_reader(filename :str) -> List:
	"""Get the vertices from the file"""
	position_list = list()
	vertices = list()

	list_uv = list()
	uv = list()

	with open(filename, 'r') as in_file:
			for line in in_file:
				if line[0:2] == 'v ':
					point = [float(value) for value in line.strip().split()[1:]]
					vertices.append(point)
				elif line[0:2] == 'vt':
					p = [float(value) for value in line.strip().split()[1:]]
					uv.append(p)
				elif line[0] == 'f':
					face_description_position = [int(value.split('/')[0])-1 for value in line.strip().split()[1:]]
					for elem in face_description_position:
						position_list.append(vertices[elem])
					face_description_UV = [int(value.split('/')[1])-1 for value in line.strip().split()[1:]]
					for elem in face_description_UV:
						list_uv.append(uv[elem])

	return position_list,list_uv

if __name__ == '__main__':
	f_in = input("File? ")
	result = my_obj_reader(f_in)
	print(result)