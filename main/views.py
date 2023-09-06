from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kezia Natalia Theodora N',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
