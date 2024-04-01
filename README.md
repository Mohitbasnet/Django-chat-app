# Django Chat APP

This is a real-time communication project using  Django Channels to create a dynamic chat website.

## Features

- **Authentication :** This is for security only the authenticated user can access.
- **Chat bubble and join :** While join a chat or a room, there will be bubble while messaging
- **Send messages:** User can send message to admin and admin also can reply to that message in realtime
- **Typing Information:** This functionality will show the user that admin is typing.


## Technologies Used

- **Backend:**
  - Django Channels
  - Python
- **Frontend:**
  - Javascript
  - Tailwind CSS
    


## Getting Started

### Backend

Navigate to the backend folder:

```bash
cd Django-chat-app

python3 -m venv venv

. venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver, run at port 8000

```

