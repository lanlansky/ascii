# -*- coding:utf-8 
_author_='lhw'
import argparse
#argparse 用于解析命令行参数和选项的标准模块
from PIL import Image
#命令行输入参数处理
#创建一个解析对象
parser = argparse.ArgumentParser()
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 40) #输出字符画宽
parser.add_argument('--height', type = int, default = 30) #输出字符画高
#解析 获取参数
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
#定义一个字符表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft:. ")
#获取对应的字符
def get_char(r,g,b,alpha = 256):
	if alpha==0:#空白处
		return '';
	#获取字符表的长度
	length=len(ascii_char)
	#计算图片的灰度值
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	# ascii_char中的一个字符所能表示的灰度值区间
	unit=(256.0)/length
	#返回对应的字符 相同灰度值的对应同一个字符
	return ascii_char[int(gray/unit)]
if __name__=='__main__':
	im = Image.open(IMG) #打开图片
	im = im.resize((WIDTH,HEIGHT), Image.NEAREST) #更改图片的显示比例
	txt = "        " #txt初始值为空
	for i in range(HEIGHT): #i代表纵坐标
		for j in range(WIDTH): #j代表横坐标
			txt += get_char(*im.getpixel((j,i))) 
			#把图片按照横纵坐标解析成r,g,b以及alpha这几个参数，然后调用get_char函数，把对应的图片转换成灰度值，把对应值得字符存入txt中
		txt += '\n        ' #每行的结尾处，自动换行
	print(txt) #在界面打印txt文件

