from django.contrib import admin
from .models import Project
from .models import Skill
from .models import Language
from .models import Interest

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Interest)
# Register your models here.
