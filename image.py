from PIL import Image
import sys, os

#grab first and second arguments
img_dir = sys.argv[1]
new_dir = sys.argv[2]

#check if new/ exist if not create
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

#loop through pokedex
for filename in os.listdir(img_dir):
    img = Image.open(f'{img_dir}{filename}')
    clean_name = os.path.splitext(filename)[0]
    #convert imgs to png
    #save to new folder
    img.save(f'{new_dir}{clean_name}.png', 'png')
    print('done')

