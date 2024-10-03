from django.shortcuts import render


def pagInit(request):
    return render(request, "todo/home.html")
