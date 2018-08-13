from django.contrib import admin
from .models import *

class TestAdmin(admin.ModelAdmin):
    pass
class TrialAdmin(admin.ModelAdmin):
    pass
class CardAdmin(admin.ModelAdmin):
    pass
class TargetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test, TestAdmin)
admin.site.register(Trial, TrialAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Target, TargetAdmin)
