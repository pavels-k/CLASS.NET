from django.contrib import admin
from learning_system.practice.models import PracticeType, PracticeCategory, PracticeTask, PracticeTaskVariation


admin.site.register(PracticeType)
admin.site.register(PracticeCategory)
admin.site.register(PracticeTask)
admin.site.register(PracticeTaskVariation)