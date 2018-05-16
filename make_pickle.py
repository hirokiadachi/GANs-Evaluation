import numpy as np
import glob
import pickle
import sys

from PIL import Image

Ims = []
Attr = []
Method = []

argv = sys.argv

All_Method = ['./Conditional_PGGAN', './Proposed_Method_PGGAN']

for method in All_Method:
    list_dir = glob.glob(method+'/*')
    Attr = []
    for path in list_dir:
	print(path)
        ims_path = glob.glob(path+'/*')
        ims_path = sorted(ims_path)
	Ims = []
        for im_path in ims_path:
            im = Image.open(im_path)
    	    #img = im.copy()
    	    #im.close()
    	    im_mat = np.array(im, np.float32)
    	    Ims.append(im_mat)
        Attr.append(Ims)
    Method.append(Attr)

print(len(Ims))
print(len(Attr))
print(len(Method))
with open('PGGAN_eval.pickle', 'wb') as f:
    pickle.dump(Method, f)
