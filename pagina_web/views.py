from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def enviarcorreo(request):
    if request.method == "POST":
        # Obtén los datos del formulario
        subject = request.POST.get('asunto', '').encode('utf-8').decode('utf-8')  # Asegura codificación UTF-8
        message = request.POST.get('mensaje', '').encode('utf-8').decode('utf-8') + \
                  "\nRemitente: " + request.POST.get('correo', '').encode('utf-8').decode('utf-8')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["autopetutt@gmail.com"]

        # Enviar el correo
        send_mail(subject, message, email_from, recipient_list)

        # Redirigir a la sección 1 con un mensaje de éxito
        return redirect('/#section1')
    
    return render(request, 'home.html')  # Asegúrate de que 'home.html' sea tu plantilla principal