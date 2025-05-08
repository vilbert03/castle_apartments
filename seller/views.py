from django.shortcuts import render
from django.http import HttpResponse




sellers = [
    {
        'id': 1,
        'name': 'asgeir steini',
        'type_of_seller': 'individual',
        'logo': 'https://www.canva.com/logos/templates/real-estate/',
        'cover_image': 'https://unsplash.com/s/photos/profile',
    },
    {
        'id': 2,
        'name': 'katrin klara',
        'type_of_seller': 'individual',
        'logo': 'https://www.canva.com/logos/templates/real-estate/',
        'cover_image': 'https://unsplash.com/s/photos/profile',
    },
    {
        'id': 3,
        'name': 'hildur afra',
        'age': 26,
        'type_of_seller': 'individual',
        'logo': 'https://www.canva.com/logos/templates/real-estate/',
        'cover_image': 'https://unsplash.com/s/photos/profile',
    },
    {
        'id': 4,
        'name': 'haldor all',
        'type_of_seller': 'individual',
        'logo': 'https://www.canva.com/logos/templates/real-estate/',
        'cover_image': 'https://unsplash.com/s/photos/profile',
    },
]



# Create your views here.
def index(request):
    return render(request, "seller/sellers.html", {
        'sellers': sellers,
    })
