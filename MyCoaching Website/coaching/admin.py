from django.contrib import admin
from . models import Coachings,Query

class CoachingsAdmin(admin.ModelAdmin):
    list_display=['name','price','offer']

class QueryAdmin(admin.ModelAdmin):
    list_display=['your_name','subject']

admin.site.register(Coachings,CoachingsAdmin)
admin.site.register(Query,QueryAdmin)


