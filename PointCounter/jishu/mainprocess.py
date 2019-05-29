import cv2 as cv
from jishu.img2bin import img2bin
from jishu.count import Count
from jishu.colorDivision import CNT
def process(img):
    sbl = img2bin.Sobel(img)
    imgCut = img2bin.cutBackground(sbl)
    imgBin = img2bin.SetGrey(imgCut)
    count,fathers,fields=Count.counter(imgBin)
    #count:number of points
    #fathers:fathers of every pixels in each point
    #fields:an array size of(rows*cols) in which fathers are marked
    print("The number of points:")
    print(count)
    print("The position of fathers:")
    print(fathers)
    G_num, B_num = CNT.cnt(fathers,img,fields,count)
    #return G_num,B_num
    cv.namedWindow("Image1")
    cv.imshow("Image1", sbl)
    cv.namedWindow("Image2")
    cv.imshow("Image2", imgCut)
    cv.namedWindow("Image3")
    cv.imshow("Image3", imgBin)

    cv.namedWindow("yuantu")
    cv.imshow("yuantu", img)
    cv.waitKey(0)
    # 释放窗口
    cv.destroyAllWindows()

img = cv.imread("E:\\PointCounter\\images\\001_01.jpg")
process(img)