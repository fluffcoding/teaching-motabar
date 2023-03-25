from django.shortcuts import render, redirect

from .models import Report
from .forms import ReportForm





def index(request):
    # Gives all the reports
    reports = Report.objects.all().order_by('-id')
    context = {
        'reports': reports
    }
    return render(request, 'index.html', context)


def single_report(request, id):
    report = Report.objects.get(id=id)
    context = {
        'report': report
    }
    return render(request, 'single-report.html', context)


def create_report(request):
    print(request.user)
    form = ReportForm(request.POST or None)
    if form.is_valid():
        # form.save()
        my_report = form.save(commit=False)
        my_report.user = request.user
        my_report.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'create-report.html', context)