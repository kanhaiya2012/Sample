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
body.reply_to = 'you-reply-to-id-address@mydomain.name'

body.mfrom = From()
body.mfrom.email = 'hello@your-register-domain-with-pepipost'
body.mfrom.name = 'Pepipost'

body.subject = 'Pepipost Test Mail through Python SDK'
body.template_id = 122434

body.content = []
body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html><body>Hello [%NAME%], Email testing is successful. <br> Hope you enjoyed this integration. <br></html>'

body.attachments = []
body.attachments.append(Attachments())
body.attachments[0].content = 'SGVsbG8gd2VsY29tZSB0byBQRVBJIHY1IEFQSQ=='
body.attachments[0].name = 'global-text-file.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"NAME":"User"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'SGVsbG8gd2VsY29tZSB0byBQRVBJIHY1IEFQSQ=='
body.personalizations[0].attachments[0].name = 'personalized-test-file.txt'

body.personalizations[0].to = []

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[0].name = 'Pepi Hero'
body.personalizations[0].to[0].email = 'toaddress@mydomain.name'

body.personalizations[0].cc = []

body.personalizations[0].cc.append(EmailStruct())
body.personalizations[0].cc[0].email = 'your-cc-email-address@mydomain.name'

body.personalizations[0].bcc = []

body.personalizations[0].bcc.append(EmailStruct())
body.personalizations[0].bcc[0].email = 'your-bcc-email-address@mydomain.name'

body.personalizations[0].token_to = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[0].token_cc = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[0].token_bcc = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[0].headers = '"{\"Arg1\":\"Value1\"}"'

body.settings = Settings()
body.settings.footer = True
body.settings.click_track = True
body.settings.open_track = True
body.settings.unsubscribe_track = True
body.settings.bcc = []

body.settings.bcc.append(EmailStruct())
body.settings.bcc[0].email = 'your-global-email-address@mydomain.name'

body.tags = ['campaign']
body.lint_payload = True
body.schedule = 1589728985


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