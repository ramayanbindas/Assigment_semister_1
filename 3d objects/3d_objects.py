from vpython import *
from sys import exit

def tuple_to_vector(points:list[tuple]) -> list:
	''':about: function takes a list of tuple of stirngs and convert them into
		vector points eg: ["(1,3,5)", "(3,4,5)"]
		:return: list of vector points
	'''

	# Define points for the curve
	vector_points = []
	for p in points:
		vec = eval(p)
		vector_points.append(vector(vec[0], vec[1], vec[2]))

	return vector_points.copy()


running = True

while running:
	print("-------Enter any key to draw a curve-------")
	object_3d = input("Enter C->curve, S->sphere, CON->cone, A->arrow, R->ring, CYL->cylinder:\t").lower()

	if object_3d == "c":
		points = input("Input points 3d points and use ';' to seperate points\
			eg:-(1,2,3);(4,5,6):\t").split(";")
		radius = int(input("Input the radius of the curve:\t") or 0.1)

		# Define points for the curve
		vector_points = tuple_to_vector(points)

		# Create a 3D canvas
		scene = canvas(title="curve", caption=f'points {points}; radius {radius}')
		# Create the curve object
		curve(pos=vector_points, radius=radius)

	elif object_3d == "s":
		position = input("Enter the position of the sphere eg:-(1,2,3):\t").split(";")
		radius = int(input("Input the radius of the sphere:\t") or 2)

		vector_points = tuple_to_vector(position)

		# Create a 3D canvas
		scene = canvas(title="sphere", caption=f'position {position}; radius {radius}')
		# Create the sphere object
		sphere(pos=vector_points[0], radius=radius)

	elif object_3d == "con":
		position = input("Enter the position of the cone eg:-(1,2,3):\t").split(";")
		axis = input("Input the axis of the cone eg:-(1,2,3):\t").split(";")
		radius = int(input("Input the radius of the sphere:\t") or 1)

		vector_points_1 = tuple_to_vector(position)
		vector_points_2 = tuple_to_vector(axis)

		# Create a 3D canvas
		scene = canvas(title="cone", caption=f'position {position[0]}; axis {axis[0]}; radius {radius}')
		# Create the sphere object
		cone(pos=vector_points_1[0], axis=vector_points_2[0], radius=radius)

	elif object_3d == "a":
		position = input("Enter the position of the arrow eg:-(1,2,3):\t").split(";")
		axis = input("Input the axis of the arrow eg:-(1,2,3):\t").split(";")

		vector_points_1 = tuple_to_vector(position)
		vector_points_2 = tuple_to_vector(axis)

		# Create a 3D canvas
		scene = canvas(title="arrow", caption=f'position {position[0]}; axis {axis[0]}')
		# Create the sphere object
		arrow(pos=vector_points_1[0], axis=vector_points_2[0])

	elif object_3d == "r":
		osition = input("Enter the position of the ring eg:-(1,2,3):\t").split(";")
		axis = input("Input the axis of the ring eg:-(1,2,3):\t").split(";")
		radius = int(input("Input the radius of the ring:\t") or 1)
		thickness = int(input("Input the thickness of the ring:\t") or 0.2)

		vector_points_1 = tuple_to_vector(position)
		vector_points_2 = tuple_to_vector(axis)

		# Create a 3D canvas
		scene = canvas(title="ring", caption=f'position {position[0]}; axis {axis[0]}; radius {radius}; thickness {thickness}')
		# Create the sphere object
		ring(pos=vector_points_1[0], axis=vector_points_2[0], radius=radius, thickness=thickness)
	elif object_3d == "cyl":
		position = input("Enter the position of the cylinder eg:-(1,2,3):\t").split(";")
		axis = input("Input the axis of the cylinder eg:-(1,2,3):\t").split(";")

		vector_points_1 = tuple_to_vector(position)
		vector_points_2 = tuple_to_vector(axis)

		# Create a 3D canvas
		scene = canvas(title="cylind", caption=f'position {position[0]}; axis {axis[0]}')
		# Create the sphere object
		cylinder(pos=vector_points_1[0], axis=vector_points_2[0])
	else:
		print("plese select the valid option")

	quit = input("Do you want to quit? Y/N:\t").lower()
	if quit == "y":
		running = False
