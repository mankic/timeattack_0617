from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserType(models.Model):
    type = models.CharField('타입', max_length=20)

    def __str__(self):
        return self.type


# custuom user model
class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50)
    password = models.CharField("비밀번호", max_length=128) # 해싱되기 때문에 길게 잡아놓는다.
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    join_date = models.DateField("가입일", auto_now_add=True)
    type = models.ForeignKey(UserType, verbose_name='타입', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=True)   # True일때 계정 활성화

    is_admin = models.BooleanField(default=False)   # admin 권한

    USERNAME_FIELD = 'email'    # ID로 사용할 필드 지정.

    REQUIRED_FIELDS: []    # createsuperuser 실행해서 입력받을 값들 지정.

    objects = UserManager()

    def __str__(self):  # 클래스 객체를 문자열로 표현
        return self.email    # object문자를 email로 보이게

    # 테이블의 접근 권한 관련
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




# class Hobby(models.Model):
#     name = models.CharField("취미", max_length=20)

#     def __str__(self):
#         return self.name


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, verbose_name="사용자", on_delete=models.CASCADE)
#     age = models.IntegerField("나이")
#     birthday = models.DateField("생일")
#     hobby = models.ManyToManyField(Hobby, verbose_name="취미")

#     def __str__(self):
#         return self.user.username
