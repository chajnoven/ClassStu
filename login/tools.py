import  os, time, random, hashlib, datetime
from django.conf import settings


def GetFileMd5(file):
    '''计算文件md5值'''
    md5d = hashlib.md5()
    for chunk in file.chunks():
        md5d.update(chunk)
    return md5d.hexdigest()

def ReName(file):
    '''文件重命名'''
    times = time.strftime("%Y%m%d%H%M%S")
    ran = random.randint(0, 1000)
    ext = os.path.splitext(file.name)[1]
    newfile = "{}{}{}".format(times, ran, ext)
    path = os.path.join('media', newfile).replace('\\', '/')
    print(path)
    new_path = './model_1/data/original/shanghaitech/part_B_final/test_data/images/class.jpg'
    read = open(new_path, 'wb+')
    for chunk in file.chunks():
        read.write(chunk)
    read.close()
    return path

def JudgeType(ext):
    '''检查文件类型'''
    ImageType = [".png", ".jpg", ".gif", "jpeg", ".bmp"]
    if ext in ImageType:
        return True
    return False

def FileSize(size):
    '''限制文件大小'''
    limit = 5*1024*1024
    if size<limit:
        return True
    return False