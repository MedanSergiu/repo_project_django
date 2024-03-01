from django.contrib import admin
from django.contrib.auth.models import User

from users.models import UserModel

# Register your models here.

admin.site.register(UserModel)
