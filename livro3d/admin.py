from django.contrib import admin
from .models import HomePage, Livro, Pagina, Sobre, Membro, Image
from users.models import User, Profile, Vinculo


admin.site.register(HomePage)
admin.site.register(Livro)
admin.site.register(Pagina)
admin.site.register(Sobre)
admin.site.register(Membro)
admin.site.register(Image)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Vinculo)
