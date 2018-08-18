from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


# Create your views here.
@staff_member_required
def admin_doc_pdf(request,doc_id):
    doc = get_object_or_404(Patient,id=doc_id)
    html = render_to_string('Doc/templates/pdf.html',
                            {'Doc':doc})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\ "order_{}.pdf"'.format(doc.id)
    weasyprint.HTML(string=html).write_pdf(response)

    return response