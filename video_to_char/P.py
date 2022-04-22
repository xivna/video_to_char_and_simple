    # PIL，全称 Python Imaging Library，是 Python 平台一个功能非常强大而且简单易用的图像处理库。
    # 但是，由于 PIL 仅支持到Python 2.7，加上年久失修，于是一群志愿者在 PIL 的基础上创建了兼容 
    # Python 3 的版本，名字叫 Pillow ，我们可以通过安装 Pillow 来使用 PIL。
from PIL import Image   #此库安装指令：pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/

def get_char(content):  #将获取到的数据用get_char()函数转行成' '空格（白色像素）与'x'（黑色像素）
    if content == 255:  #判断像素是是黑是白
        return " "
    else:
        return 'x'

def main(file_name,Resolution = 10):    #file_name为要提取的图片的路径，Resolution为要将图片缩小的倍数(Resolution=10意思是如果不输入这个参数那默认为缩小十倍)
    text = ""
    im = Image.open(file_name)  #打开目标图片
    width,height = im.size  # 获得图像尺寸
    width //= Resolution;height //= (Resolution*2)  #分别将图片的宽和高整除Resolution倍，Resolution变量的值就是函数第二个参数的值
    im = im.resize((width, height))   #Image.resize（宽，高，重采样）返回此图像的调整大小后的副本; 重采样–可选的重采样过滤器（可不输入这个参数）。这可以是PIL.Image.NEAREST（使用最近的邻居），PIL.Image.BILINEAR（线性插值），PIL.Image.BICUBIC（三次样条插值）或PIL.Image.LANCZOS（高质量的下采样滤波器）之一)。如果省略，或者图像的模式为“ 1”或“ P”，则将其设置为PIL.Image.NEAREST。返回类型：一个Image对象。
    im2=im.convert("1") #'1'模式（模式“1”为二值图像，非黑即白。它每个像素用8bit表示，0表示黑，255表示白）
    for i in range(height):
        for j in range(width):
            content = im2.getpixel((j, i))   #getpixel（）函数是用来获取图像中某一点的像素的RGB颜色值，getpixel的参数是一个像素点的坐标。对于图象的不同的模式，getpixel函数返回的值不同。
            text += get_char(content)       #将获取到的数据用get_char()函数转行成' '空格（白色像素）与'x'（黑色像素）
        text += "\n"            #获取完一行像素的值后加'\n'换行符，开始第二行像素数据的采集
    return text     #返回采集到的这一帧图像数据；

    # print(im2.mode)  #获得此时像素模式;(默认为“RGB”模式(RED，GREEN，BLUE))
    # print(im2.getpixel((30,25))) #返回坐标点（30,25）处的red，green，blue的数值

#file_name = "D:\暂存\workspace\python\work\图片转字符串\i.png",Resolution = 10
def get_char_color(r,g,b,alpha=256):
    if alpha == 0:
        return " "
    gary = (r*299 + g*587 + b*114 + 500)/1000   #RGB转灰度公式;为避免低速的浮点运算，所以需要整数算法;RGB一般是8位精度，现在缩放1000倍，所以上面的运算是32位整型的运算。注意后面那个除法是整数除法，所以需要加上500来实现四舍五入。
    ascii_char = list("$@B%8&WM#*oahkbdpwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
    x = int((gary / (alpha + 1.0)) * len(ascii_char))
    return ascii_char[x]

def main_color(file_name,Resolution = 10):
    text = ""
    im = Image.open(file_name)
    width,height = im.size  # 获得图像尺寸
    width //= Resolution;height //= (Resolution*2)
    im = im.resize((width, height))
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j, i))
            text += get_char_color(*content)
        text += "\n"
    return text