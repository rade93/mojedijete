from django.shortcuts import render, get_object_or_404


def NaslovnaView(request):
    return render(request, 'naslovna/index.html')
