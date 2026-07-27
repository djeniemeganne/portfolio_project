from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def style_view(request):
    return render(request , '/portfolio/static/css/style.css' )
def js_view(request):
    return render(request , '/portfolio/static/js/script.js' )
def static_view(request):
    return render(request , '/portfolio/static/' )
def home_view(request):
    return render(request , 'home.html' )

def about_view(request):
    return render(request , 'about.html' )


def project_view(request):
    return render(request , 'project.html')

# def contact_view(request):pour recupere le message envoyer
#     return render(request , 'contact.html' )

def competence_view(request):
    return render(request, 'competence.html')


def contact_view(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        sujet = request.POST.get("sujet")
        message = request.POST.get("message")

        
        print("MESSAGE RECU :", message)
        
        contenu = f"""
            Nom : {nom}
            Prénom : {prenom}
            Email : {email}

            Message : {message}
        """
        
        print(contenu)
         
        send_mail(
            sujet,
            contenu,
            email,
            ["megannemenekdem@gmail.com"],  
            fail_silently=False,
        )

      
        return render(request, "home.html", {
            "success": "Votre message a bien été envoyé."
        })

    return render(request, "contact.html")
