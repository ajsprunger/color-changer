from PIL import Image, ImageColor

img = Image.open('images/pikachu.jpg')
img = img.convert('RGB')

d = img.getdata()

new_image = []
for item in d:
  if item[0] in list(range(200, 250)):
    new_image.append((142, 195, 208))
  else:
    new_image.append(item)

img.putdata(new_image)

img.save('pikachu_altered.jpg')