from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import Cachorro, Comedouro, Comentarios, Publicacoes, Tag, Usuario

admin.site.register(Cachorro)
admin.site.register(Comedouro)
admin.site.register(Tag)
admin.site.register(Publicacoes)
admin.site.register(Comentarios)
admin.site.register(Usuario)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password",'password_confirmation')}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


