from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
def all_nontechnical_events(request):
    allevents = non_tech_event.objects.all()
    context = {
        "allevents":allevents
        }
    return render(request,"eventpage/non_technical.html",context)


def non_event_detail_page(request,pk):
    event_detail = non_tech_event.objects.filter(slug = pk)
    context = {
        "event_detail":event_detail
    }
    return render(request,'eventpage/event_details.html',context)

def non_event_register_page(request,pk):
    event_detail = non_tech_event.objects.filter(slug = pk)
    event_detail_instance = non_tech_event.objects.get(slug = pk)

    if request.method == "POST" and request.FILES.get('paymentproof'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        collegename = request.POST.get('collegename')
        collegeid = request.POST.get('collegeid')
        paymentproofsf = request.FILES['paymentproof']

        new_instance = non_tech_event_register(name=name, email=email, ph=phone,collegename=collegename,usn=collegeid,event=event_detail_instance)
        new_instance.paymentproof.save(f'{name}_{email}.png', paymentproofsf, save=True)
        url = "http://techyuva.nexel.in/events/Non-Technical-Events/proof/"+new_instance.slug
        html_message = render_to_string('homepage/mail.html', {'name': name, 'email':email , 'phone':phone, 'collegename':collegename, 'collegeid':collegeid,'id':new_instance.slug,'entryfee':event_detail_instance.name,"url":url}) 
        plain_message = strip_tags(html_message)
        send_mail(
                'Tech Yuva 2024 - Registration Complete',
                plain_message,
                'from@example.com',
                [email],
                html_message=html_message,  # HTML version of the email
                fail_silently=False,
                    )

        return redirect('nonproof', new_instance.slug)



    context = {
        "event_detail":event_detail
    }
    return render(request,'homepage/registerpage.html',context)


def nonproof(request,pk):
    register = non_tech_event_register.objects.filter(slug=pk)
    context = {
        'register':register
    }
    return render(request,'homepage/proof.html',context)