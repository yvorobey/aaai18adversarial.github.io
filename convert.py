from PIL import Image
import os 
import sys
prefix = sys.argv[1]
fnames = os.listdir(prefix)
for fname in fnames:
	full_fname = prefix + fname
	im = Image.open(full_fname)
	rgb_im = im.convert('RGB')
	rgb_im.save(full_fname.split('.png')[0] + '.jpg')
	