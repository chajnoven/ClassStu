from django.db import models
#from rest_framework.permissions import IsAuthenticated
# Create your model_1 here.
import datetime
import time

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    # email = model_1.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Teacher(models.Model):
    '''老师名'''
    name = models.CharField(max_length=256)

class Room(models.Model):
    '''上课'''
    room = models.CharField(max_length=256)

class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    stu_numbers = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.room

    class Meta:
        db_table = 'class'
    #上课时间
'''class ConfirmString(model_1.Model):
    code = model_1.CharField(max_length=256)
    user = model_1.OneToOneField('User', on_delete=model_1.CASCADE)
    c_time = model_1.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
'''


class UpImage(models.Model):
    imgName = models.CharField(max_length=250, default="", verbose_name="文件名")
    imgMd5 = models.CharField(max_length=125, verbose_name="MD5")
    imgType = models.CharField(max_length=32, verbose_name="文件类型")
    imgSize = models.IntegerField(verbose_name="文件大小")
    imgPath = models.CharField(max_length=128, verbose_name="文件路径")
    imgCreated = models.CharField(max_length=64, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                  verbose_name="创建时间")
    imgUpdated = models.CharField(max_length=64, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                  verbose_name="更新时间")

    def GetimageByMd5(self, md5):
        try:
            return UpImage.objects.filter(imgMd5=md5).first()

        except:
            return None
    def __str__(self):
        return self.imgName
    class Meta:
        db_table = 'upImage'

