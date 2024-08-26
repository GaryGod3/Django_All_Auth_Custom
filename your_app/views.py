from django.shortcuts import render

# Create your views here.

def index(request, option='Home'):
    """The home page for Your Site"""
    page_title = option

    if option == 'Option3':
        long_content = "Page filler for testing fixed navbar." * 80
    else:
        long_content = ""

    context = {
        'page_title': page_title,
        'long_content': long_content,
    }
    return render(request, "index.html", context )