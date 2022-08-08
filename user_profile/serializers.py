from django.conf import settings
from rest_framework import serializers
from .models import Education, Profile, WorkExperience, Interests, SocialLinks

User = settings.AUTH_USER_MODEL

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic','name','age','gender','admin_type','education','work_experience','interest','social_links')
        depth = 1

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class WorkExperience(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = "__all__"