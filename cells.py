from PIL import Image
import numpy as np
import pylab
import mahotas as mh
celije=Image.open('cells3.jpg')
celije=celije.convert('L')
celije=np.array(celije)
celije2 = mh.thresholding.otsu(celije)
pylab.imshow(celije > celije2)
pylab.show()
celije2=pylab.gray()
celije3bw = mh.gaussian_filter(celije,1)
celije2=np.array(celije2)
celije3bw=celije3bw.astype('uint8')
celije2= mh.thresholding.otsu(celije3bw)
pylab.imshow(celije3bw > celije2)
pylab.show()
labeled,nr_objects = mh.label(celije3bw < celije2)
print(nr_objects)