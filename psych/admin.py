from django.contrib import admin
from .models import PsychDiagnosis, MedicalDiagnosis, Medication, Subject, Test

class PsychDiagnosisAdmin(admin.ModelAdmin):
    pass
class MedicalDiagnosisAdmin(admin.ModelAdmin):
    pass
class MedicationAdmin(admin.ModelAdmin):
    pass
class SubjectAdmin(admin.ModelAdmin):
    pass
class TestAdmin(admin.ModelAdmin):
    pass

admin.site.register(PsychDiagnosis, PsychDiagnosisAdmin)
admin.site.register(MedicalDiagnosis, MedicalDiagnosisAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test, TestAdmin)