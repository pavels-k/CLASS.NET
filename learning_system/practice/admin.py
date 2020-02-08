from django.contrib import admin
from learning_system.practice.models import PracticeCategory, PracticeTask, TaskUserData
#from learning_system.practice.models import PracticeType, PracticeTaskVariation


admin.site.register(PracticeCategory)
admin.site.register(PracticeTask)
admin.site.register(TaskUserData)
'''
admin.site.register(PracticeType)
admin.site.register(PracticeTaskVariation)
'''