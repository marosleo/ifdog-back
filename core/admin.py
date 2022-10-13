from django.contrib import admin

from core.models import Cachorro, Comedouro, Comentarios, Publicacoes, Tag

admin.site.register(Cachorro)
admin.site.register(Comedouro)
admin.site.register(Tag)
admin.site.register(Publicacoes)
admin.site.register(Comentarios)
# admin.site.register(User)


