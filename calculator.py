
while True:

	print('==================')
	print('Area Calculator 📐')
	print('==================')

	print()

	print('1) Triangle')
	print('2) Rectangle')
	print('3) Square')
	print('4) Circle')
	print('5) Quit')

	print()

	shape = int(input('Wich shape: '))
	print()

	if shape == 1:
		base = int(input('Base: '))
		height = int(input('Height: '))
		areaT = (height * base)/2
		print(f' The area is {areaT}')
	elif shape == 2:
		length = int(input('length: '))
		width = int(input('width: '))
		areaR = length * width
		print(f' The area is {areaR}')
	elif shape == 3:
		side = int(input('side: '))
		areaS =  side * side
		print(f' The area is {areaS}')
	elif shape == 4:
		radius = int(input('length: '))
		areaC = 3.14 * (radius*radius)
		print(f' The area is {areaC}')
	elif shape == 5:
		break
	else:
		print('Invalid number')
