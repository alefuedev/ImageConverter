import sys
import os
from PIL import Image
from progress.bar import Bar

# grab the first and second argument
file_to_open = sys.argv[1]
file_to_make = sys.argv[2]
path = os.getcwd()
path = path + '/' + file_to_open

def from_jpg_to_png():
 bar = Bar('Processing', max=20)
 for i in range(20):
   jpgs = []
   names = []
   for f in files:
     if f.count('.jpg'):
       jpgs.append(f)       
       for f in jpgs:
          file = Image.open(f'{f}')
          # change save path folder
          f = f.rsplit('.jpg')
          f = str(f.pop(0))
          file_name = file.save(f'{f}.png', "png")
          os.rename(f'{f}.png', path + '/' + file_to_make + '/' + f'{f}.png')
   bar.next()
 bar.finish()

try:
 os.chdir(path)
except FileNotFoundError:
 print('please check the name folder to open')
else:
 files = os.listdir()
 if files.count(file_to_make) == 0:
     print(f'Creating folder {file_to_make}')
     os.mkdir(f'{file_to_make}')
     from_jpg_to_png()
 else:
     print('Folder found.')
     from_jpg_to_png()
