'''
Code by Bruno Miguel

this code, takes a folder of images with different sizes and do a slide window to extract patches using a distance from eache patch. 

Runing it, it will ask to select a folder to extract, then to choose a folder to store de results.

'''
import os.path as osp

from scipy import misc

from img_basics import fileImageIo as imgio

#define the size of the patch
patch_size = 299
#define the distance to move the slide
distance = patch_size-150

#open a folder of images
folder = imgio.openImgFolder("Select a folder of the images to patch")

#folder to storeNew Imgs
folderstore = imgio.returnFolder("Select a folder to store new images")
baseFolder = osp.basename(folderstore)
countPatch=0
for img in folder:
    print("reading img: "+img)
    imgMatrix = misc.imread(img)
    height = len(imgMatrix)
    width = len(imgMatrix[0])
    imgBaseName = osp.basename(img)
    if (width>patch_size and height>patch_size):
        x0=0
        y0=0
        xf = patch_size
        yf=patch_size
        final_y=True
        #create a name for the patches
        while(yf<height):
            while(xf<width):
                countPatch = countPatch+1
                newpatch = imgMatrix[y0:yf,x0:xf]
                #save new img
                #if(fire.temFogo(newpatch)):
                 #   imgio.saveimg(folderstore+'\\fire\\'+baseFolder+'_'+str(countPatch)+".jpg",newpatch)
                #else:
                imgio.saveimg(folderstore + '\\' + imgBaseName + '_' + str(countPatch) + ".jpg", newpatch)
                x0 = x0+distance
                xf = xf+distance
            x02 = width - patch_size - 1
            xf2 = width - 1
            if(xf!=xf2):
                countPatch = countPatch + 1
                newpatch = imgMatrix[y0:yf, x02:xf2]
                imgio.saveimg(folderstore + '\\' + imgBaseName + '_' + str(countPatch) + ".jpg", newpatch)
            x0=0
            xf=patch_size
            y0 = y0+distance
            yf = yf+distance
            if(yf>height and final_y):
                if((yf-height)>80):
                    y0 = height - patch_size - 1
                    yf = height - 1
                    final_y = False
    else:
        #image is smaller than the patch, so, resize the image to the patch size
        w = patch_size
        h = patch_size
        newpatch = misc.imresize(imgMatrix, (w, h))
        imgio.saveimg(folderstore + '\\' + imgBaseName + '_0.jpg', newpatch)
