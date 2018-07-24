from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
class SubjectAdmin(admin.ModelAdmin):
    pass
class TestAdmin(admin.ModelAdmin):
    pass
class TrialAdmin(admin.ModelAdmin):
    pass
class CardAdmin(admin.ModelAdmin):
    pass
class PointAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Trial, TrialAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Point, PointAdmin)
