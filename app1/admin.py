from django.contrib import admin
from .models import app1
from .resource import app1Resource
from import_export.admin import ImportExportModelAdmin

class app1Admin(ImportExportModelAdmin):
     resource_class = app1Resource      
admin.site.register(app1, app1Admin)



# Register your models here.


