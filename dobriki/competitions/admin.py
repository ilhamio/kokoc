from django.contrib import admin
from competitions.models import UserTeam, PersonalCompetition

# Register your models here.
admin.site.register(UserTeam)
admin.site.register(PersonalCompetition)
