from django.shortcuts import render
from num2words import num2words


def home(request):
    """
    This page responds to 2 HTTP methods
    GET: Load page
    POST: Takes argument to convert number to words (humanize)
    """
    context = {}
    if request.method == "POST":
        number = request.POST.get('number')
        if number:
            words = num2words(number)
            currency = num2words(number, to='currency', currency='INR', lang="en_IN")
            context['words'] = words
            context['currency'] = currency
    return render(request, 'humanize_app/home.html', context=context)
