#### Example of Advance Usage

```python
# -*- coding: utf-8 -*-
from pepipost.pepipost_client import PepipostClient
from pepipost.models.email_body import EmailBody
from pepipost.models.personalizations import Personalizations
from pepipost.models.attachments import Attachments
from pepipost.models.mfrom import From
from pepipost.models.email_body_attachments import EmailBodyAttachments
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
import jsonpickle

client = PepipostClient()
email_controller = client.email
body = EmailBody()
body.personalizations = []

api_key = 'api_key here '
body.personalizations.append(Personalizations())
body.personalizations[0].recipient = 'recipient@your-mail.com'

body.tags = 'tagsPython'
body.mfrom = From()

body.mfrom.from_email = 'example@your-verified-domain'
body.mfrom.from_name = 'Example Pepi'
body.subject = 'Emailing with Pepipost is easy'
body.content = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'
body.settings = Settings()

body.settings.footer = 1
body.settings.clicktrack = 1
body.settings.opentrack = 1
body.settings.unsubscribe = 1

try:
    result = email_controller.create_send_email(api_key, body)
    if not (result.error_info is None):
        print("Reason :: " + str(result.error_info.error_message) + "\n" + "Message :: " + str(result.message))
    else:
        print("Message :: " + result.message)
except APIException as e:
    print(e)

```