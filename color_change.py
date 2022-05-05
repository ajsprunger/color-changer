from PIL import Image, ImageColor

img = Image.open('images/Headshot_altered.jpg')
img = img.convert('RGB')

d = img.getdata()

new_image = []
for item in d:
  if item[0] in list(range(30, 100)) and item[1] in list(range(60, 150)) and item[2] in list(range(100, 150)):
    new_image.append((142, 195, 208))
  else:
    new_image.append(item)

img.putdata(new_image)

img.save('Headshot_altered.jpg')