
from unicodedata import category
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):


    def create_user(self, first_name, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            first_name=first_name,
            phone_number = phone_number
           
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,phone_number,  password):
        user = self.create_user(first_name,phone_number, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=64, blank=True)
    full_name = models.CharField(max_length=64, blank=True)
    phone_number = models.IntegerField(blank=True, unique=True)
    email = models.EmailField(verbose_name='email address', null=True, max_length=25)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    objects = MyUserManager()

    def get_full_name(self):
        return self.full_name 
        
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self) -> str:
        return self.full_name

    def save(self, *args, **kwargs):
        # password = self.password
        # self.set_password(password)
        return super(User,self).save(*args, **kwargs)

#Banner
class Banner(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

#detail product
class InfoProduct(models.Model):
    size = models.CharField(max_length=65)
    element = models.CharField(max_length=65)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/category_image')
    

#Product
class Product(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/product')
    info_product = models.ForeignKey(InfoProduct, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)





    def __str__(self):
        return self.name


#????????????.
class Printer(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/printer')


class InfoType(models.Model):
    size = models.CharField(max_length=65)
    type_paper = models.CharField(max_length=65)
    one_site_print = models.CharField(max_length=65)
    double_site_print = models.CharField(max_length=65)
    

    def __str__(self) -> str:
        return self.size
#???????????? ???????????? 	?????? ???????????? 	?????????????????????????? ???????????? (4+0) 	?????????????????????????? ???????????? (4+4)

class Type(models.Model):
    name = models.CharField(max_length=65)
    infotype = models.ForeignKey(InfoType, on_delete=models.CASCADE, related_name="types")
    

    def __str__(self) -> str:
        return self.name
    
# Reklama , Poligrafia, Suviner
class TypeService(models.Model):
    name = models.CharField(max_length=65)


    def __str__(self) -> str:
        return self.name


class MenuService(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/menuservice')
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

#M?? ????????????????????
class Tariff(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class MenuTariff(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/imagesTariff')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)


    def __str__(self) -> str:
            return self.name


class CEO(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/ceo')
    number = models.IntegerField()
    description = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
                return self.name


class Sponsors(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/sponsor')


    def __str__(self) -> str:
                return self.name


class Contact(models.Model):
    name = models.CharField(max_length=65)
    number = models.IntegerField()
    info = models.CharField(max_length=65)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/contact')


    def __str__(self) -> str:
                return self.name

#???????? ????????????.   
class Portfolio(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='media/portfolio')

    def __str__(self) -> str:
                return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=65)
    number = models.IntegerField()
    image = models.ImageField(upload_to='media/social_media')

    def __str__(self) -> str:
                return self.name





    