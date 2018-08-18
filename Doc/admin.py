from django.contrib import admin
from django.urls import reverse
from .models import Patient
import datetime
import csv
from django.http import HttpResponse


# Register your models here.
def export_to_csv(modeladmin,request,queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Context-Disposition'] = 'attachment;\ filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many
              and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj,field.name)
            if isinstance(value,datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'



class PatientAdmin(admin.ModelAdmin):
  list_display = ('id','FirstName','LastName','IdNumber',
                  'Disease','Prescription','publish','updated','status')
  list_filter = ('status','publish')
  search_fields = ('IdNumber','FirstName')
  date_hierarchy = 'publish'
  ordering = ['status','publish']
  actions = [export_to_csv]



admin.site.register(Patient,PatientAdmin)




