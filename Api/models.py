from jalali_date import datetime2jalali, date2jalali
from extentions.Utils import jalali_converter
from jalali_date import datetime2jalali
from AddUser.models import MyUser
from django.db import models
from Task.models import Task


# Attach models
class Attach(models.Model):
    STATUS = (
        (1, 'disable'),
        (2, 'done'),
    )
    TYPE = ((0, 'image'),
            (1, 'pdf'),
            (2, 'doc'),
            (3, 'zip'),
            )

    name = models.CharField(max_length=200, verbose_name="نام ")
    type_id = models.IntegerField(choices=sorted(TYPE), verbose_name="نوع")
    path = models.FileField(upload_to='Attach/file', null=True, blank=True, verbose_name="آدرس ")
    status = models.IntegerField(choices=sorted(STATUS), verbose_name="وضعیت")
    doneDate = models.DateField(auto_now_add=True, null=True, verbose_name="تاریخ انجام ")
    createDate = models.DateField(auto_now=True, verbose_name="تاریخ ایجاد  ")
    creator_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name="نام ایجاد کننده")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ضمیمه"
        verbose_name_plural = "فایلهای ضمیمه"


# apiDevelop models
class Develop(models.Model):
    METHOD = (
        (1, 'get'),
        (2, 'put'),
        (3, 'post'),
        (4, 'delete'),
    )

    name = models.CharField(max_length=200, verbose_name="نام")
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="نام تسک")
    method = models.IntegerField(choices=sorted(METHOD), verbose_name=" متد")
    url = models.CharField(max_length=200, verbose_name="آدرس ")
    param = models.CharField(max_length=200, verbose_name="پارامتر", null=True, blank=True)
    response = models.TextField(max_length=200, verbose_name="بازخورد", null=True, blank=True)
    attach_ids = models.ManyToManyField(Attach, verbose_name="ضمیمه", null=True, blank=True)
    doneDate = models.DateField(auto_now=True, verbose_name="تاریخ انجام شدن")
    createDate = models.DateField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    creator_uid = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name="UserCreator",
                                    verbose_name="نام ایجاد کننده")

    def __str__(self):
        return self.name

    # convert date to jalali_date
    def jdoneDate(self):
        return jalali_converter(self.doneDate)

    # convert date to jalali_date

    def jcreateDate(self):
        return jalali_converter(self.createDate)

    class Meta:
        verbose_name = "توسعه "
        verbose_name_plural = "توسعه ها "


# apiValidation models
class Validation(models.Model):
    STATUS = (
        (1, 'disable'),
        (2, 'done'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان ")
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="نام تسک")
    description = models.TextField(max_length=5000, verbose_name="توضیحات")
    status = models.IntegerField(choices=sorted(STATUS), verbose_name="وضعیت", default=2, editable=False)
    doneDate = models.DateField(auto_now=True, verbose_name="تاریخ انجام ")
    creator_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, verbose_name="نام ایجاد کننده")
    createDate = models.DateField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد  ")

    def __str__(self):
        return self.title

    # convert date to jalali_date

    def jdoneDate(self):
        return jalali_converter(self.doneDate)

    # convert date to jalali_date

    def jcreateDate(self):
        return jalali_converter(self.createDate)

    class Meta:
        verbose_name = " اعتبار سنجی"
        verbose_name_plural = "اعتبار سنجی ها"


# apiMessage models
class Message(models.Model):
    STATUS = (
        (1, 'disable'),
        (2, 'done'),
    )
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="نام تسک")

    title = models.CharField(max_length=200, verbose_name="عنوان ")
    code = models.CharField(max_length=5000, verbose_name="کد")
    status = models.IntegerField(choices=sorted(STATUS), verbose_name="وضعیت", default=2, editable=False)
    doneDate = models.DateField(auto_now=True, verbose_name="تاریخ انجام ")
    creator_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, verbose_name="نام ایجاد کننده")
    createDate = models.DateField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد  ")

    def __str__(self):
        return self.title

    def my_view(request):
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

    # convert date to jalali_date

    def jdoneDate(self):
        return jalali_converter(self.doneDate)

    # convert date to jalali_date

    def jcreateDate(self):
        return jalali_converter(self.createDate)

    class Meta:
        verbose_name = "پیغام"
        verbose_name_plural = "پیغام ها"


# apiTesting models
class Testing(models.Model):
    STATUS = (
        (1, 'disable'),
        (2, 'done'),
    )
    task_id = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="نام تسک")

    title = models.CharField(max_length=200, verbose_name="عنوان ")
    status = models.IntegerField(choices=sorted(STATUS), verbose_name="وضعیت")
    doneDate = models.DateField(auto_now=True, verbose_name="تاریخ انجام ")
    creator_id = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, verbose_name="نام ایجاد کننده")
    createDate = models.DateField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد  ")

    def __str___(self):
        return self.title

    class Meta:
        verbose_name = "تست"
        verbose_name_plural = "تست ها "
