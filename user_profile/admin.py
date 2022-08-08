from django.contrib import admin
from .models import Education, Interests, Profile, SocialLinks, WorkExperience

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(SocialLinks)
admin.site.register(Interests)