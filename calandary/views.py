from django.shortcuts import render


def calandary(request):
    context = {
        
    }
    return render(request, template_name='calandary.html', context=context)
