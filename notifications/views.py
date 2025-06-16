from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from .tasks import send_transaction_email
import json

# Create your views here.

@csrf_exempt
def create_transaction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('customer_email')
        amount = data.get('amount')
        transaction = Transaction.objects.create(customer_email=email, amount=amount, status='pending')
        send_transaction_email.delay(transaction.id)
        return JsonResponse({'message': 'Transaction created and notification will be sent.', 'transaction_id': transaction.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)
