from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # inlines = (DocProfileInline, PatProfileInline)

    list_display = [
        # "id",
        "email",
        "username",
        # "first_name",
        # "last_name",
        # "phone_no",
        # "street",
        # "city",
        # "state",
        # "country",
        # "is_doctor",
        # "is_patient",
    ]


actions = ["delete_selected"]


admin.site.register(CustomUser, CustomUserAdmin)
