from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Skill
from .models import Language
from .models import Interest


def home(request):
	skills = Skill.objects.all()
	languages = Language.objects.all()
	interests = Interest.objects.all()
	return render(request, 'portfolio/home.html', {'skills':skills, 'languages':languages, 'interests':interests})




