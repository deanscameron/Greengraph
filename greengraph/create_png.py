"""png creation file"""

# Module counts the green parts of a image, and creates a image diaplaying them


# Define the green areas of an image
def is_green(r,g,b):
  threshold=1.1
  return g>r*threshold and g>b*threshold

  
import png
from itertools import izip


# Counts the green parts of a png image
def count_green_in_png(data):
    image=png.Reader(file=StringIO(data.content)).asRGB()
    count = 0
    for row in image[2]:
        pixels=izip(*[iter(row)]*3)
        count+=sum(1 for pixel in pixels if is_green(*pixel))
    return count

	
from StringIO import StringIO


# Creates a png image displaying the green parts of the image
def show_green_in_png(data):
    image=png.Reader(file=StringIO(data.content)).asRGB()
    count = 0
    out=[]
    for row in image[2]:
        outrow=[]
        pixels=izip(*[iter(row)]*3)
        for pixel in pixels:
            outrow.append(0)
            if is_green(*pixel):
                outrow.append(255)
            else:
                outrow.append(0)
            outrow.append(0)
        out.append(outrow)
    buffer=StringIO()
    result = png.from_array(out,mode='RGB')
    result.save(buffer)
    return buffer.getvalue()