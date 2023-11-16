from django.shortcuts import render

def custom_access_denied(request, exception):
    return render(request, 'errors/access_denied.html', status=403)

def custom_page_not_found(request, exception):
    return render(request, 'errors/page_not_found.html', status=404)