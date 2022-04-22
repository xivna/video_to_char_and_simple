from genericpath import exists
import tkinter as tk
from tkinter import W,filedialog,messagebox
import os
import V2I,I2C

def clicked1():
    path_ = filedialog.askopenfilename(title='视频选择',filetypes=[('视频','.mp4'),('视频','.flv'),('All Files','*')],initialdir='D:/RouteFolder/workspace/python/work/video_to_char')
    path_ = path_.replace("\\","\\\\")
    path1.set(path_)

    V_path = EntryPath1.get().replace("\\","\\\\")
    AllFrames= V2I.getFrames(V_path)
    tk.Label(root,text = '共' + str(AllFrames) + '帧').grid(row=0,column=3)

def clicked2():
    path_ = filedialog.askdirectory(title='缓存文件夹选择',initialdir='D:/TEMP')
    path_ = path_.replace("\\","\\\\")
    path2.set(path_)

def clicked3():
    V_path = EntryPath1.get().replace("\\","\\\\")
    try:
        StartFrames = int(EntryFrames1.get())
    except:
        messagebox.showwarning('提示','起始帧请输入数字')
    try:
        LongFrames = int(EntryFrames2.get())
    except:
        messagebox.showwarning('提示','持续帧请输入数字')
    CachePath = EntryPath2.get().replace("\\","\\\\")

    file_name = os.path.basename(V_path)
    image_path = CachePath + "\\" + file_name + "\\image_all\\"
    char_path = CachePath + "\\" + file_name + "\\char_all\\"

    if StartFrames + LongFrames <= V2I.getFrames(V_path):
        run = True
    else:
        run = False
        messagebox.showwarning('提示','输入的帧数量超过了视频总帧数')

    if StartFrames < 0:
        run = False
        messagebox.showwarning('提示','输入的起始帧的值应≥0')
    if LongFrames < 10:
        run = False
        messagebox.showwarning('提示','输入的帧持续的值应至少大于10')

    if run:
        #判断视频转换的图片文件夹是否存在，不存在则执行v2c
        if not os.path.exists(image_path):
            try:
                os.makedirs(image_path)
            except:
                messagebox.showerror('警告','请输入正确的缓存路径' + image_path)
        CheckI = StartFrames
        #messagebox.showwarning('提示',image_path)  #显示缓存路径
        while(CheckI < StartFrames + LongFrames):
            CheckPathI = image_path + 'Frame' + str(CheckI) + '.jpg'
            if os.path.exists(CheckPathI) == False:
                FramesNum = V2I.video2image(V_path,image_path,1,StartFrames,LongFrames)
                break
            else:
                CheckI += LongFrames//10
            FramesNum = V2I.video2image(V_path,image_path,0)

        #判断图片转换的字符画文本是否存在，不存在则创建
        if not exists(char_path):
            os.makedirs(char_path)
        CheckC = StartFrames
        while(CheckC < StartFrames + LongFrames):
            CheckPathC = char_path + 'Frame' + str(CheckC) + '.txt'
            if os.path.exists(CheckPathC) == False:
                I2C.Image2Char(image_path,char_path,FramesNum,int(multiple.get()),StartFrames,LongFrames)
                break
            else:
                CheckC += LongFrames//10
            #print("此视频的字符画文件之前已提取过了，那这步就跳过了啊...")

        #边加载边播放
        PlayCache = []
        for i in range(StartFrames,StartFrames + LongFrames):
            CharPath = char_path + 'Frame' + str(i) + '.txt'
            with open(CharPath,'r') as PlayFile:
                os.system('cls')
                print(PlayFile.read())
                
def clicked4(event):
    tip0 = tk.Label(root,text = '').grid(row=5,column=1)
    tip1 = tk.Label(root,text = 'Tips：从哪一帧开始播放？')
    tip1.grid(row=6,column=1,columnspan=3,sticky=W)

def clicked5(event):
    tip0 = tk.Label(root,text = '').grid(row=5,column=1)
    tip1 = tk.Label(root,text = '                                          ')
    tip1.grid(row=6,column=1,columnspan=3,sticky=W)
    tip2 = tk.Label(root,text = '                                          ')
    tip2.grid(row=7,column=1,columnspan=3,sticky=W)

def clicked6(event):
    tip0 = tk.Label(root,text = '').grid(row=5,column=1)
    tip1 = tk.Label(root,text = 'Tips：要播放的多少帧的视频？')
    tip1.grid(row=6,column=1,columnspan=3,sticky=W)
    tip2 = tk.Label(root,text = '（不建议超过1000）')
    tip2.grid(row=7,column=1,columnspan=3,sticky=W)
#-------------------------------------------------------------------------
root = tk.Tk()
root.title('字符动画')
root.geometry('371x512')

path1 = tk.StringVar()
path2 = tk.StringVar()

tk.Label(root,text = '视频路径：').grid(row=0,column=0)
EntryPath1 = tk.Entry(root,textvariable = path1)
EntryPath1.insert(0,'D:/RouteFolder/workspace/python/work/video_to_char/BadApple.mp4')
tk.Button(root,text = '选取',command= clicked1).grid(row=0,column=2)

tk.Label(root,text = '起始帧：').grid(row=1,column=0)
EntryFrames1 = tk.Entry(root,textvariable = '从哪一帧开始播放？',width=5)
EntryFrames1.bind('<Enter>',clicked4)
EntryFrames1.bind('<Leave>',clicked5)
EntryFrames1.insert(0,'0')
tk.Label(root,text = '').grid(row=1,column=4)
tk.Label(root,text = '持续帧：').grid(row=2,column=0)
EntryFrames2 = tk.Entry(root,textvariable = '要播放的多少帧的视频？',width=5)
EntryFrames2.insert(0,'1000')
EntryFrames2.bind('<Enter>',clicked6)
EntryFrames2.bind('<Leave>',clicked5)
tk.Label(root,text = '画面缩小倍数：').grid(row=3,column=0)
multiple = tk.Entry(root,textvariable = '',width=5)
multiple.insert(0,'5')

tk.Label(root,text = '缓存路径：').grid(row=4,column=0)
EntryPath2 = tk.Entry(root,textvariable = path2)
EntryPath2.insert(0,'D:/TEMP')
tk.Button(root,text = '选取',command= clicked2).grid(row=4,column=2)

tk.Button(root,text = '开始',command= clicked3,cursor="hand2").grid(row=5,column=1) #cursor="hand2" 鼠标悬停时手型；


EntryPath1.grid(row=0,column=1)
EntryPath2.grid(row=4,column=1)
multiple.grid(row=3,column=1,sticky=W)
EntryFrames1.grid(row=1,column=1,sticky=W)
EntryFrames2.grid(row=2,column=1,sticky=W)
root.mainloop()
