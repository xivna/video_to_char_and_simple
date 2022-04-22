import os   #自带库
import V,P  #我们自己写的P.py文件和V.py文件

VideoPath = 'work\\video_to_char\\BadApple.mp4'  #要提取的视频路径
ImagePath = 'work\\video_to_char\\V2C\\image_all\\'  #从视频提取出的图片保存位置
Charpath = 'work\\video_to_char\\V2C\\Char_all\\'  #转换好的字符画存储位置

if __name__=='__main__':    #当 .py 直接运行的时候 __name__ 的值是 __main__ 而当 .py 被当作模块导入的时候 __name__ 的值是模块的名称
    if not os.path.exists(ImagePath): 
        L_num = int(V.V2P(VideoPath,ImagePath))  #调用V.py中的从视频提取图片的方法   #L_num：要播放的帧数量
    else:
        L_num = int(V.V_frames(VideoPath,ImagePath))

    if not os.path.exists(Charpath):    #若存在字符文件夹就不再运行这段了
        cache = []
        os.makedirs(Charpath)
        for i in range(0,L_num):
            url = ImagePath + 'i' + str(i) + '.jpg' #组合要提取的目标图片的路径
            text = P.main(file_name=url,Resolution = 5) #调用P.py中的从图片中提取字符数据的函数
            #text = P.main_color(file_name=url,Resolution = 5)   #彩色的
            file = open(Charpath + str(i) + '.txt','w')
            file.write(text)
            file.close()
            print('\r','保存字符画文件中：',i,'/',L_num,end='')  #进度显示，可删掉（为了使用体验不建议删除）

    #将字符画加载到内存然后输出
    CharCache = []
    for i1 in range(L_num):
        CharUrl = Charpath + str(i1) + '.txt'
        Char = open(CharUrl,'r')
        CharRead = Char.read()
        CharCache.append(CharRead)
        Char.close()
        print('\r','加载字符画文件中：',i1,'/',L_num,end='')
    #播放字符画
    for i2 in range(L_num):
        os.system('cls')
        print(CharCache[i2])
        op = 1000
        while(op <= 0):
            op -= 1