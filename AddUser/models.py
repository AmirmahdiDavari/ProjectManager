from django.contrib.auth.models import User, AbstractUser
from django.db import models

class MyUser(AbstractUser):
    STATUSE = {
            (1,'Expert'),
            (2,'ScrumMaster'),
            (3,'Financial'),
            (4,'Admin'),
        }
    Skill=models.IntegerField(choices=sorted(STATUSE),default=1)







    # class User(User):
    #     pass
    #     STATUSE={
    #         (1,'expert'),
    #         (2,'scram'),
    #         (3,'fonshial'),
    #     }
    #     Skill=models.IntegerField(choices=sorted(STATUSE),default=1)






    # avatars = "avatars/3.png"
    # profile_image = models.ImageField(upload_to="images/user/", null=True, blank=True, default=avatars,
    #                                   verbose_name="عکس کاربری")
    # city = models.CharField(max_length=2000, verbose_name="شهر")
    # address = models.CharField(null=True, max_length=20000,verbose_name="آدرس")
    # phone_number = models.CharField(null=True, max_length=11,verbose_name="شماره تلفن")
    # post_code = models.CharField(null=True, max_length=11,verbose_name="کد پستی")
    # description = models.TextField(null=True, blank=True,verbose_name="نوشته ها")