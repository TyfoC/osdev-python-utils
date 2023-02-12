#	Converts an image to other formats
import sys
from PIL import Image
from os import linesep

arguments = sys.argv

if len(sys.argv) != 7:
	print("Error: wrong number of input parameters!")
	print("Usage:")
	print("\tpython3 img2data.py <input image> <start x> <start y> <shift x> <shift y> <output format> <output path>")
	exit(1)

input_image = Image.open(sys.argv[0], 'r')
x = sys.argv[1]
y = sys.argv[2]
shift_x = sys.argv[3]
shift_y = sys.argv[4]
output_format = sys.argv[5]
output_file = open(sys.argv[6], 'w')

width, height = input_image.size
pixels = list(input_image.getdata())
result = ""

if output_format == "c-array":
	result = '{' + linesep

	while y < height:
		while x < width:
			color = pixels[y * width + x]
			red = hex(color[0])[2:]
			green = hex(color[1])[2:]
			blue = hex(color[2])[2:]

			result += "\t{ "
			print("\t{ ", end="")
			
			if int(red, 16) == 0:
				red = "00"
			elif int(red, 16) < 0x10:
				red = "0" + red
			if int(green, 16) == 0:
				green = "00"
			elif int(green, 16) < 0x10:
				green = "0" + green
			if int(blue, 16) == 0:
				blue = "00"
			elif int(blue, 16) < 0x10:
				blue = "0" + blue
			
			result += f"0x{green}{blue}{red}" + "}," + linesep
			x += shift_x
		x = 0
		y += shift_y
	
	result += "}"
else:
	print("Unknown output format! Available:")
	print("\tc-array")
	exit(2)

output_file.write(result)
output_file.close()
input_image.close()