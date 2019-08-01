from django.db import models

# Create your models here.


class User(models.Model):
    '''该表为注册页面专用
       去掉邮箱验证，由于本网站特性不需要严格验证
       注册后的用户为评论专用，除此外无其他特殊用途 '''
    id = models.AutoField(primary_key=True)
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    # email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    #has_confirmed = models.BooleanField(default=False)

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
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #上课时间
'''class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
'''

class Picture(models.Model):
    #title = models.CharField("标题", max_length=100, blank=True, default='')
    image = models.ImageField("图片", upload_to="pictures", blank=True)
    date = models.DateField(auto_now_add=True)

    '''def __str__(self):
        return self.title'''