from PIL import Image, ImageColor

img = Image.open('images/pikachu.jpg')
img = img.convert('RGB')

d = img.getdata()

new_image = []
for item in d:
  if item[0] in list(range(240, 256)) and item[1] in list(range(40, 60)) and item[2] in list(range(20, 45)):
    new_image.append((142, 195, 208))
  else:
    new_image.append(item)

img.putdata(new_image)

img.save('pikachu_altered.jpg')