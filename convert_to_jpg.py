from PIL import Image
import os, sys

for file_in in sys.argv[1:]:
  f, e = os.path.splitext(file_in)
  file_out = f + '.jpg'
  if file_in != file_out:
    try:
      with Image.open(file_in) as image:
        image.convert("RGB").save(file_out)
        print(f"successfully converted {file_in}")
    except OSError as error:
      print(error)
      print('cannot convert', file_in)