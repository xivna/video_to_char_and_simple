from PIL import Image

AscIIChar = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def GetChar(r,g,b,a = 256):
    if a == 0:
        return " "
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256/len(AscIIChar)

    return AscIIChar[int(gray/unit)]

def Image2Char(image_path,char_path,FramesNum,Resolution = 5,StartFrames = 0,LongFrames = 1000): #FramesNum,总帧数；Resolution,画缩小倍数
   
    for li in range(StartFrames,StartFrames + LongFrames):
        text = ""
        ImageName = image_path + 'Frame' + str(li) + '.jpg'
        im = Image.open(ImageName)
        width,height = im.size
        width //= Resolution;height //= (Resolution*2)
        im = im.resize((width, height))
        for i in range(height):
            for j in range(width):
                content = im.getpixel((j,i))
                text += GetChar(*content)
            text += "\n"
        print('\r',"保存字符画文本中...",li,"/",FramesNum,end='')

        CharPath = char_path + 'Frame' + str(li) + '.txt'
        with open(CharPath,'w') as CharFile:
            CharFile.write(text)
    print('\r',"字符画文件提取完毕              ")
