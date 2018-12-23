from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
import base64
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.send'

RECEIVER_EMAIL = 'jfdezalba89@gmail.com'

ACCEPTED_SUBJECT = 'ACEPTADO - Asistencia Boda de Aupa'
REJECTED_SUBJECT = 'DENEGADO - Asistencia Boda de Aupa'


def send_email(guest_name, guest_email, number_of_guests, is_coming):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    content = """
        Nombre y apellidos: %s
        Email: %s
        Número de asistentes: %s
    """%(guest_name, guest_email, number_of_guests) if is_coming else """
        Nombre y apellidos: %s
        Email: %s
        No asistirá a Boda de Aupa
    """%(guest_name, guest_email)

    message = create_message(
        'admin@bodadeaupa.es',
        RECEIVER_EMAIL,
        ACCEPTED_SUBJECT if is_coming else REJECTED_SUBJECT,
        content
    )
    sent_message = send_message(service, 'me', message)
    return sent_message

def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    return {'raw': raw.decode()}

def send_message(service, user_id, message):
    """Send an email message.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

    Returns:
        Sent Message.
    """
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except HttpError as e:
        print('An error occurred %'%e)
