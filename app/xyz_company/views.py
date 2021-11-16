
   
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
 


def Home(request):
    """this function render the home template"""

    context = {
                "title":"home",
    }
    return render(request, 'xyz_company/home.html', context)
