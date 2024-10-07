from django.shortcuts import render

def custom_404(request, exception):
#     print("this is req", request.GET)
    return render(request, 'global-views/404.html', status=404)
