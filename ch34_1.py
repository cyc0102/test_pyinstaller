import cv2 as openCV
openCV.namedWindow('Picture1')                          #使用預設值
openCV.namedWindow('Picture2', openCV.WINDOW_NORMAL)    #可調大小
img1 = openCV.imread('test.jpg')                        #彩色影像讀取
img2 = openCV.imread('test.jpg',0)                      #灰階影像讀取
openCV.imshow('Picture1', img1)                         #顯示Img1
openCV.imshow('Picture2', img2)                         #顯示Img2    
openCV.imwrite('out34_1.jpg', img2)                     #將Img2存檔為out34_2.jpg
openCV.waitKey(4000)                                    #wait key for 4 sec
openCV.destroyWindow('Picture1')                        #刪除Picture1
openCV.waitKey(5000)                                    #wait key for 5 sec
openCV.destroyAllWindows()                              #刪除所有Windows

