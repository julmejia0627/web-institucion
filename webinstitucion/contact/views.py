from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    #print("Tipo de petición: {}".format(request.method)) imprime por consola el método
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "I.E. Benjamín Herrera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["julmejia0819@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #Todo ha asalido bien, redireccionamos a Ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha asalido bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
