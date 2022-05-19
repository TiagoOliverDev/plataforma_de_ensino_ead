#from email import message
#import email
from django.template.loader import render_to_string #Renderiza template e gera String
from django.template.defaultfilters import striptags #striptags remove as tags html
from django.core.mail import EmailMultiAlternatives  #Class do core mail que tem várias alternativas, tem conteúdo principal e adiciona conteúdo alternativo
from django.conf import settings


def send_mail_template(subject, template_name, context, recipient_list, 
    from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
    
    message_html = render_to_string(template_name, context)

    message_txt = striptags(message_html)
    
    email = EmailMultiAlternatives(
        subject=subject, body=message_txt, from_email=from_email, 
        to=recipient_list
    )
    email.attach_alternative(message_html, "text/html")
    email.send(fail_silently=fail_silently)
