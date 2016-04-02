# -*- coding: utf-8-*-
from PIL import Image
import math
import os
def make_regular_image(img,size=(256,256)):
    return img.resize(size).convert('RGB')
def his_similar(lh,rh):
    sum=0.0
    for l,r in zip(lh,rh):
        if (l==r):
            temp=0
        else:
            temp=abs(i-r)/max(l,r)
            sum+=temp
    float(sum)
    sum=sum/len(lh)
    return 1-sum
                
def split_image(img,part_size=(64,64)):
    width ,height=(256,256)
    pwidth,pheight=part_size
    assert width%pwidth==height%pheight==0
    for i in xrange(0,width,pwidth):
        for j in xrange(0,height,pheight):
            return [img.crop((i, j, i+pwidth, j+pheight)).copy() for i in xrange(0, width, pwidth) for j in xrange(0, height, pheight)]
def calc_similar(li,ri):
    sum=0.0
    for l in split_image(li):
        for r in split_image(ri):
            sum+=his_similar(l.histogram(),r.histogram())/16.0
    return sum
    
def calc_similar_by_path(lf,rf):
    li,ri=make_regular_image(Image.open(lf)),make_regular_image(Image.open(rf))
    
    return calc_similar(li,ri)
if __name__=='__main__':
    
    print '请输入作为参照的图片'
    filename=raw_input()
    filenames=os.listdir("image")
    for i in range (len(filenames)):
        print i
        print'%d:%.3f%%'%(i,calc_similar_by_path('image/'+filenames[i], filename)*100)
    
    
