from django.contrib import admin

# Register your models here.
from .models import Post
#from .models import SlNieruchomosci
#from .models import SlAkcja

admin.site.register(Post)
#admin.site.register(SlNieruchomosci)
#admin.site.register(SlAkcja)
