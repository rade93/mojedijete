from django.shortcuts import render, get_object_or_404


def ObjavaView(request):
    return render(request, 'pitanja/index.html')
