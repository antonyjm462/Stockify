from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import dataparse


@login_required
def dashboard(request):
    return render(request, "dashboard.html",{"json": dataparse.dataparse()})
