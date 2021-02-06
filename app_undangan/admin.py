from django.contrib import admin
from .models import LiveVideo, Galery, TamuUndangan, Pengantin, Pesan

# Register your models here.
admin.site.register(LiveVideo)
admin.site.register(Galery)
admin.site.register(Pengantin)
admin.site.register(TamuUndangan)
admin.site.register(Pesan)
