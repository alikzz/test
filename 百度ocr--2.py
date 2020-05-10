from aip import AipOcr
from pathlib import Path

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

'''读取图片，写入txt'''
def ToTXT(path):
    image = open(path, 'rb').read()#给地址，读取图片
    results=client.basicGeneral(image);#调用api
    for result in results['words_result']:#按行提取文字
        text=result['words']
        f=open(str(path)+'.txt',mode='a')#打开文本
        f.write(text)#写入文本
        f.close#关闭文件
        
    

def main():
    '''文件名地址录入'''    
    PathInput=input('PICpath:')
    paths=Path(PathInput).glob('**/*.jpg')#find the path of *.jpg
    index=1
    for path in paths:
        print(index)
        ToTXT(path)
        index+=1


main()
    
    

        








