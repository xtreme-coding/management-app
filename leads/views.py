from django.shortcuts import render, HttpResponse
from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    context={
        'leads': leads
    }
    return render(request, 'leads/home_page.html', context)   

def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse('Here is the detail view')  