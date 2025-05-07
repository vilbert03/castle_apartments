from django.shortcuts import render
from django.http import HttpResponse

apartments = [
    {
        'id': 1,
        'name': 'fagragrund 12',
        'type': 'house',
        'price': '45.000.000',
        'on_sale': True,
        'seller_id': 1,
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },
    {
        'id': 2,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    },

    {
        'id': 3,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    },

    {
        'id': 4,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    },
    {
        'id': 5,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    },
    {
        'id': 6,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    },
    {
        'id': 7,
        'name': 'hagarland 48',
        'type': 'house',
        'price': '58.000.000',
        'on_sale': True,
        'seller_id': 1,
        'rooms': 8,
        'image': 'https://c.arvakur.is/m2/H5NHUjuJHp5RGZln6cWPvwztwfU=/x867/smart/fs-pool/1e/1e84a28e179fdfab276e5fa8067133809e8a488f.jpg'
    }
]


# Create your views here.
def index(request):
    return render(request, "apartment/apartments.html", {
        "apartments": apartments
    })

def get_apartment_by_id(request, id):
    apartment = [x for x in apartments if x['id'] == id][0]
    return render(request, 'apartment/apartment_detail.html', {
        "apartment": apartment
    })


