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

api_key = 'SGVsbG8gd2VsY29tZSB0byBQRVB'

client = PepipostClient(api_key)



send_controller = client.send
body = Send()
body.reply_to = 'qwercom@gmail.com'
body.mfrom = From()
body.mfrom.email = 'personalizationValidation@pepitest.xyz'
body.mfrom.name = 'invalid settings'
body.subject = 'invalid settings'
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = 'Without personalization attachment'

body.attachments = []

body.attachments.append(Attachments())
body.attachments[0].content = 'dGVzdCB0ZXN0DQp0ZXN0IHRlc3Q='
body.attachments[0].name = 'tesxt1file.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"NAME":"Archana","SURNAME":"Jadhav","PROFESSION":"QA"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'dGVzdCB0ZXN0DQp0ZXN0IHRlc3Q='
body.personalizations[0].attachments[0].name = 'tesxt2file.txt'

body.personalizations[0].to = []

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[0].name = 'archana1'
body.personalizations[0].to[0].email = 'ttesttry758@gmail.com'

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[1].name = 'archana2'
body.personalizations[0].to[1].email = 'testartstar@gmail.com'

body.personalizations[0].cc = []

body.personalizations[0].cc.append(EmailStruct())
body.personalizations[0].cc[0].name = 'Addye'
body.personalizations[0].cc[0].email = 'testartstar1@gmail.com'

body.personalizations[0].bcc = []

body.personalizations[0].bcc.append(EmailStruct())
body.personalizations[0].bcc[0].name = 'Addye2'
body.personalizations[0].bcc[0].email = 'testartstar2@gmail.com'

body.personalizations[0].token_to = 'abcd'
body.personalizations[0].token_cc = 'frty'
body.personalizations[0].token_bcc = 'vsdnbvsb'
body.personalizations[0].headers = 'headers only'

body.settings = Settings()
body.settings.footer = True
body.settings.click_track = True
body.settings.open_track = True
body.settings.unsubscribe_track = True
body.settings.bcc = []

body.settings.bcc.append(EmailStruct())
body.settings.bcc[0].name = 'something'
body.settings.bcc[0].email = 'archanapan2077@gmail.com'

body.tags = ['Test']
body.lint_payload = True
body.schedule = 0

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