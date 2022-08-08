from django.db import models
from django.db.models import Q

class UserQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self,query):#,user=None):
        lookup = Q(title__icontains=query)# | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        # if user is not None:
        #     # qs2 = self.filter(user=user).filter(lookup)
        #     qs = qs.filter(user=user)# (qs | qs2).distinct()
        return qs


class UserManager(models.Manager):

    def get_queryset(self,*args,**kwargs):
        return UserQuerySet(self.model,using=self.db)

    def search(self,query):#,user=None):
        return self.get_queryset().search(query)#,user=user)
