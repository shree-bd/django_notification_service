# Transaction Notification Microservice

This Django-based microservice handles transaction notifications to customers using asynchronous processing and email delivery.

## Features

- Asynchronous transaction processing using Celery
- Email notifications using SendGrid
- Redis as message broker
- Transaction event handling
- Customer notification management

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
SENDGRID_API_KEY=your_sendgrid_api_key
REDIS_URL=redis://localhost:6379/0
```

4. Run Redis (required for Celery):
```bash
# On macOS with Homebrew:
brew install redis
brew services start redis

# On Linux:
sudo apt-get install redis-server
sudo systemctl start redis
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the Celery worker:
```bash
celery -A transaction_notification worker -l info
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `transaction_notification/` - Main Django project
- `notifications/` - App for handling notifications
- `celery.py` - Celery configuration
- `tasks.py` - Async tasks for processing transactions

## API Endpoints

- `POST /api/transactions/` - Submit a new transaction for processing
- `GET /api/transactions/<id>/` - Get transaction status
- `GET /api/notifications/` - List all notifications

## Testing

Run tests with:
```bash
python manage.py test
``` 