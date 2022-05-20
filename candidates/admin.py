from django.contrib import admin

from .models import Profile, Skill, SkillSet, UserSkill

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(SkillSet)
admin.site.register(UserSkill)
