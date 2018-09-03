from django.contrib import admin
from .models import *
# Register your models here.
class TmtTestAdmin(admin.ModelAdmin):
    pass
class TrialAdmin(admin.ModelAdmin):
    pass
class CardAdmin(admin.ModelAdmin):
    pass
class PointAdmin(admin.ModelAdmin):
    pass
admin.site.register(TmtTest, TmtTestAdmin)
admin.site.register(Trial, TrialAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Point, PointAdmin)
