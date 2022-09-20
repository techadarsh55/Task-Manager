from django.contrib import admin
from .models import CreateTask
from django.utils.html import format_html
# Register your models here.
class CreatedAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['title','report_to','status','start_time','task_in_progress','task_is_finish','user',]
    list_editable =['status',]
    list_filter = ['start_time','task_is_finish',]

    def title(self, obj):
        return format_html(f"<span style='color:#2a96f5;'>{obj.title}</span>")




admin.site.register(CreateTask,CreatedAdmin)