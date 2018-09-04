# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tweets.models import Tweet, HashTag
#from models import Tweet,Hashtag
    # Register your models here.
admin.site.register(Tweet)
admin.site.register(HashTag)

# Register your models here.
def __str__(self):
    return self.text
