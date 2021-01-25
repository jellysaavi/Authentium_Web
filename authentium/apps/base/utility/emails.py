import logging

from django.core.exceptions import ImproperlyConfigured
from django.core.files import File
from django.template.loader import render_to_string
from mailqueue.models import MailerMessage
from authentium.settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


#  ------------------------------------------------------------------
# send_email
#  ------------------------------------------------------------------
def send_email(subject, to_address, context_data,
               text_template_path, html_template_path, cc_address="",
               bcc_address="", from_address=DEFAULT_FROM_EMAIL,
               file_attachments=[], headers={}):
    """
    http://django-mail-queue.readthedocs.io/en/latest/usage.html
    """
    logger.info(
        'Sending email with subject %s, to %s ... ',
        subject,
        to_address
    )
    
    if not to_address and not bcc_address:
        raise ImproperlyConfigured(
            "you have not set any sender address. "
            "No value found for to address and bcc address")
    
    html_content = render_to_string(html_template_path, context_data)
    text_content = render_to_string(text_template_path, context_data)

    send_mail(
        subject,
        "",
        from_address,
        [to_address],
        html_message = html_content,
        fail_silently=False,
    )
    
    
    # app_name = 'Authentium'
    
    # new_message = MailerMessage()
    # new_message.subject = subject
    # new_message.to_address = to_address
    # new_message.cc_address = cc_address
    # new_message.bcc_address = bcc_address
    # new_message.from_address = from_address
    # new_message.content = text_content
    # new_message.html_content = html_content
    # new_message.app = app_name
    # new_message.headers = headers

    # for file in file_attachments:
    #     file = File(open(file, "rb"))
    #     new_message.add_attachment(file)
    
    # new_message.save()
