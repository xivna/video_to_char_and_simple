# OpenCV作为较大众的开源库，拥有了丰富的常用图像处理函数库，采用C/C++语言编写，可以运行在Linux/Windows/Mac等操作系统上，能够快速的实现一些图像处理和识别的任务
# 注意：安装的时候是 opencv_python，但在导入的时候采用 import cv2

import cv2  #安装指令：pip install opencv_python -i https://pypi.tuna.tsinghua.edu.cn/simple/ #后面的-i ... 是采用国内源安装，这样速度会很快；安装别的包也可以在后面加这个试试
import os   #自带库

def V2P(video_path,ImagePath):
    #video_path = 'BadApple.mp4' #要提取的视频
    #ImagePath='image_all'    #图片保存的目录   
    times=0 #给要保存的图片起名做编号用的变量

    if not os.path.exists(ImagePath):   #如果不存在'image_all'文件夹
        os.makedirs(ImagePath)          #创建'image_all'文件夹

    camera = cv2.VideoCapture(video_path)   #VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频，如vc = cv2.VideoCapture("../testi.mp4")
    frames_num=camera.get(7)    #获取视频总帧数
    while True: #传说中的死循环
        res,image = camera.read()   #camera.read()按帧读取视频，res,frame是获camera.read()方法的两个返回值。其中res是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。image就是每一帧的图像，是个三维矩阵。
        if res == False:    #如果文件读取到结尾，res为False就会执行以下两行循环体
            print('读取视频帧图像完毕')
            break       #读取完毕后用break退出死循环
        
        cv2.imwrite(ImagePath + 'i' + str(times)+'.jpg', image)   #函数 cv2.imwrite() 用于将图像保存到指定的文件;注意路径中不能有中文，否则不能正常保存（这里浪费了我好久时间）
        print('\r','视频提取中：',ImagePath + str(times)+'.jpg',end='')    #进度显示，可删掉;'\r'意思是打印完这一行后将光标移动到最左边；end=''意思是打印完不换行继续在本行打印
        times += 1    #每保存一张图片，此编号加1；等同于 times = times + 1
    print('图片提取结束')

    camera.release()    #释放软件/硬件资源
    #如果没有这句，例：
        #>>> camera = cv2.VideoCapture(0)
        #>>> #camera.release() 
        #>>> camera2 = cv2.VideoCapture(0)
        # 这样会报错
    return frames_num

def V_frames(video_path,ImagePath):
    camera = cv2.VideoCapture(video_path)
    frames_num=camera.get(7)
    return frames_num