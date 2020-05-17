#### Example of Advance Usage

```python
# -*- coding: utf-8 -*-
from pepipost.pepipost_client import PepipostClient
from pepipost.configuration import Configuration
from pepipost.models.send import Send
from pepipost.models.mfrom import From
from pepipost.models.content import Content
from pepipost.models.type_enum import TypeEnum
from pepipost.models.attachments import Attachments
from pepipost.models.personalizations import Personalizations
from pepipost.models.email_struct import EmailStruct
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
import jsonpickle

api_key = 'your api_key here'

client = PepipostClient(api_key)



send_controller = client.send
body = Send()
body.reply_to = 'replay@pdomain.com'
body.mfrom = From()
body.mfrom.email = 'example@your-verified-domain'
body.mfrom.name = 'From pepipost'
body.subject = 'Emailing with Pepipost is easy with attributes [%name%]'
body.template_id = 0
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'

body.attachments = []

body.attachments.append(Attachments())
body.attachments[0].content = 'dGVzdCB0ZXN0DQp0ZXN0IHRlc3Q='
body.attachments[0].name = 'test2.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"name":"test","name1":"test1"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'dGVzdCB0ZXN0DQp0ZXN0IHRlc3Q='
body.personalizations[0].attachments[0].name = 'test.txt'

body.personalizations[0].to = []

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[0].name = 'recipient name'
body.personalizations[0].to[0].email = 'recipient@your-mail.com'

body.personalizations[0].cc = []

body.personalizations[0].cc.append(EmailStruct())
body.personalizations[0].cc[0].name = 'cc name'
body.personalizations[0].cc[0].email = 'cc@your-mail.com'

body.personalizations[0].bcc = []

body.personalizations[0].bcc.append(EmailStruct())
body.personalizations[0].bcc[0].name = 'bcc name'
body.personalizations[0].bcc[0].email = 'bcc@your-mail.com'


body.settings = Settings()
body.settings.footer = True
body.settings.click_track = True
body.settings.open_track = True
body.settings.unsubscribe_track = True
body.tags = ['testtag']

try:
    result = send_controller.create_generate_the_mail_send_request(body)
    if not result.get('status') :
        try:
            print("Reason :: " + str(result.get('error')[0].get('message')) + "\n" + "Message :: " + str(result.get('error')[0].get('help')))
        except Exception as e:
            print(result)    
    else:

        print("Message :: %s | Message id :: %s" %  (result.get('message'), result.get('data').get('message_id')))
except APIException as e: 
    print(e)
```