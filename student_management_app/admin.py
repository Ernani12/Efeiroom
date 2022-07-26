from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Administrador, Professor, Disciplina, Assuntos, Aluno, Comparecimento, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs
from .models import Video



admin.site.register(Video)

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(Administrador)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Assuntos)
admin.site.register(Aluno)
admin.site.register(Comparecimento)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)

