from PIL import Image, ImageColor

img = Image.open('images/squirtle.jpg')
img = img.convert('RGB')

d = img.getdata()

new_image = []
for item in d:
  if item[0] in list(range(200, 256)):
    new_image.append((255, 224, 100))
  else:
    new_image.append(item)

img.putdata(new_image)

img.save('squirtle_altered.jpg')