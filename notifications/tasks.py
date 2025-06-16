from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Transaction

@shared_task
def send_transaction_email(transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        subject = 'Transaction Successful'
        message = f"Dear Customer,\n\nYour transaction of ${transaction.amount} was successful.\n\nThank you."
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [transaction.customer_email],
            fail_silently=False,
        )
        transaction.status = 'notified'
        transaction.save()
    except Transaction.DoesNotExist:
        pass 