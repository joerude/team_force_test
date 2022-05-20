from django.db import models
from django.urls import reverse


class SkillSet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("N", "None"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")
    skill_set = models.ForeignKey(SkillSet, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.user)


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_set = models.ForeignKey(SkillSet, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_id"
    )

    def __str__(self):
        return str(self.skill_name)


class UserSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skill_id")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.skill)
