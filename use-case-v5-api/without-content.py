
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
body.reply_to = 'qwercom'
body.mfrom = From()
body.mfrom.email = 'test@pepitest.xyz'
body.mfrom.name = 'fromdomain'
body.subject = 'Without token to'
body.template_id = 1
body.content = []

body.attachments = []

body.attachments.append(Attachments())
body.attachments[0].content = 'your base file content is base64 encoded'
body.attachments[0].name = 'Myfilenamaaae.txt'

body.attachments.append(Attachments())
body.attachments[1].content = 'your base file content is base64 encoded'
body.attachments[1].name = 'Myfilenamaaae.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"NAME":"Archana","SURNAME":"Jadhav"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'your base file content is base64 encoded'
body.personalizations[0].attachments[0].name = 'Myfilenamaaaaaae.txt'

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[1].content = 'your base file content is base64 encoded'
body.personalizations[0].attachments[1].name = 'Myfilenameaaaa2.txt'

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

body.personalizations[0].token_cc = '{"token_cc": "token_cc"}'
body.personalizations[0].token_bcc = '{"token_bcc": "token_bcc"}'
body.personalizations[0].headers = 'headers only'

body.personalizations.append(Personalizations())
body.personalizations[1].attributes = jsonpickle.decode('{"NAME":"Archana","SURNAME":"Jadhav"}')
body.personalizations[1].attachments = []

body.personalizations[1].attachments.append(Attachments())
body.personalizations[1].attachments[0].content = 'your base file content is base64 encoded'
body.personalizations[1].attachments[0].name = 'Myfilenamaaaaaae.txt'

body.personalizations[1].attachments.append(Attachments())
body.personalizations[1].attachments[1].content = 'your base file content is base64 encoded'
body.personalizations[1].attachments[1].name = 'Myfilenameaaaa2.txt'

body.personalizations[1].to = []

body.personalizations[1].to.append(EmailStruct())
body.personalizations[1].to[0].name = 'archana1'
body.personalizations[1].to[0].email = 'ttesttry758@gmail.com'

body.personalizations[1].to.append(EmailStruct())
body.personalizations[1].to[1].name = 'archana2'
body.personalizations[1].to[1].email = 'testartstar@gmail.com'

body.personalizations[1].cc = []

body.personalizations[1].cc.append(EmailStruct())
body.personalizations[1].cc[0].name = 'Addye'
body.personalizations[1].cc[0].email = 'testartstar1@gmail.com'

body.personalizations[1].bcc = []

body.personalizations[1].bcc.append(EmailStruct())
body.personalizations[1].bcc[0].name = 'Addye'
body.personalizations[1].bcc[0].email = 'archana.jadhav@netcore.co.in'

body.personalizations[1].token_cc = '{"asdsadasd": "token_cc"}'
body.personalizations[1].token_bcc = '{"token_bcasdasdsc": "token_bcc"}'
body.personalizations[1].headers = 'headers only'

body.settings = Settings()
body.settings.footer = True
body.settings.click_track = True
body.settings.open_track = True
body.settings.unsubscribe_track = True
body.settings.bcc = []

body.settings.bcc.append(EmailStruct())
body.settings.bcc[0].name = 'something'
body.settings.bcc[0].email = 'rcpt1@gmail.com'

body.settings.bcc.append(EmailStruct())
body.settings.bcc[1].name = 'something2'
body.settings.bcc[1].email = 'rcpt2@gmail.com'

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