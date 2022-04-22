from email import message
from re import I
from tkinter import messagebox
import cv2,os

def video2image(V_path,image_path,v,StartFrames = 0,LongFrames = 1000): #StartFrames：起始帧位置；LongFrames：要提取多少帧
    EndFrames = StartFrames + LongFrames

    try:
        ImageFile = cv2.VideoCapture(V_path)
        FramesNum = int(ImageFile.get(7))
    except:
        messagebox.showerror('警告','视频文件打开失败，试试别的视频吧')
    while(v):   #如果v == 1，则提取图片；v == 0就跳过，只获得帧数就好
        ImageFile.set(cv2.CAP_PROP_POS_FRAMES,StartFrames)
        res,image = ImageFile.retrieve()
        if res == False or StartFrames > EndFrames:
            break
        cv2.imwrite(image_path + 'Frame' + str(StartFrames) + '.jpg' ,image) 
        print('\r','视频提取中...',StartFrames,"/",EndFrames,end='')
        StartFrames +=1

    if v:
        print('\r',"视频帧提取结束                ")
    else:
        print("此视频之前已提取过帧图像了，那么就跳过这一步吧...")

    ImageFile.release()

    if FramesNum > EndFrames:
        return EndFrames
    else:
        return FramesNum

def getFrames(V_path):
    ImageFile = cv2.VideoCapture(V_path)
    FramesNum = int(ImageFile.get(7))

    return FramesNum