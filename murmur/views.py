from django.shortcuts import render
from handlers.models import *


def index(request):

    msk_contacts = MskContacts.objects.all().first()
    spb_contacts = SpbContacts.objects.all().first()
    main_url = MainUrl.objects.all().first()

    params = {
        'msk_contacts': msk_contacts,
        'spb_contacts': spb_contacts,
        'main_url': main_url
    }
    return render(request, './index.html', params)
