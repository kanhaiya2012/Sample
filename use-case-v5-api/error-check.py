
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
body.mfrom.email = 'checkfields@addonmaster.com'
body.mfrom.name = 'fromdomain'
body.subject = 'Verify fields'
body.template_id = 1
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html><body><p>This Avail FREEBIEES 1. [%NAME%] 2. [%SURNAME%] 3. [% PROFESSION %] Thishis</p><a href=\'https://uatdeveloper.yesbank.in/ibm_apim/activate/x?activationToken=eyJ1cmwiOiJodHRwczovLzEwLjAuNDAuMTc4L3YxL3BvcnRhbC91c2Vycy81YzMwNjZmOGU0YjBmZThmNjgwMTMyYzkvYWN0aXZhdGUiLCJ1c2VybmFtZSI6IiFCQVNFNjRfU0lWX0VOQyFfQWJURXBibHNMdzBsR3NXb2dJRXNZV2pwTnhFQmRpVXljRzdyQXMyZ1dkMS9BQUFBSEd4TldHYXdadGZXTXBMY3dZR3YrUE13elNGZkJyTUlhN0g1T1dGUGNtZDciLCJhdXRoZW50aWNhdGlvbiI6eyJ1c2VybmFtZSI6IjU1ZTAyNzQ0ZTRiMDgwZmMzMzlkOTliMi81NWUwMjQzMWU0YjA4MGZjMzM5ZDk5OTgvTjRnSzNwQjZsUjBsTzRySDRoWDhjQjFhWDZ3TTdnQzhzTjR1VTJxVzdkIiwicGFzc3dvcmQiOiJUZmRic0VoWjd6MXQxQjZhSG02cWxCRXlxWnhiL2ZZbkVNYUNaMjNMZDQifSwicHJvdmlkZXJDb250ZXh0Ijp7Im9yZ0lEIjoiNTVlMDI0MzBlNGIwODBmYzMzOWQ5OTkyIiwiZW52aXJvbm1lbnRJRCI6IjU1ZTAyNzQ0ZTRiMDgwZmMzMzlkOTliMiJ9fQ\'>Click Here</a><br><p>This is link 2</p><a href=\'https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fcard%3Fie%3DUTF8%26ref_%3Dcust_rec_intestitial_signin\'>Click Here</a><p>This is link 3</p><a href=\'http://gadgets.ndtv.com/\'>Click Here</a><br></body></html>'

body.attachments = []

body.attachments.append(Attachments())
body.attachments[0].content = 'your base file content is base64 encoded'
body.attachments[0].name = 'Myfilenamaaae.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"NAME":"Archana","SURNAME":"Jadhav","PROFESSION":"QA"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'dGVzdCB0ZXN0DQp0ZXN0IHRlc3Q='
body.personalizations[0].attachments[0].name = 'tesxt2file'

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

body.personalizations[0].token_to = '{"token_to": "token_to"}'
body.personalizations[0].token_cc = '{"token_cc": "token_cc"}'
body.personalizations[0].token_bcc = '{"token_bcc": "token_bcc"}'
body.personalizations[0].headers = 'headers only'

body.personalizations.append(Personalizations())
body.personalizations[1].attributes = jsonpickle.decode('{"NAME":"Pri","SURNAME":"Gaikwad","PROFESSION":"QA"}')
body.personalizations[1].attachments = []

body.personalizations[1].attachments.append(Attachments())
body.personalizations[1].attachments[0].content = 'Y3VybCAtWEdFVCAnc3RhZ2U2LnBlcGlwb3N0LmNvbTo5MjAwL3BlcGlwb3N0Ny0yMDIwMDUvX3NlYXJjaD9wcmV0dHknIC1IICdDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL2pzb24nIC1kICcNCnsNCiAgICJxdWVyeSI6ew0KICAgICAgImJvb2wiOnsNCiAgICAgICAgICJtdXN0IjpbDQogICAgICAgICAgICB7DQogICAgICAgICAgICAgICAidGVybSI6ew0KICAgICAgICAgICAgICAgICAgImNsaWVudGlkIjo2MjEwNw0KICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgfQ0KICAgICAgICAgXQ0KICAgICAgfQ0KICAgfQ0KfScNCg0KVG90YWwgY2FzZXM6IDMzNQ0KUGFzc2VkOiAxMTgNCkZhaWxlZDoyNA0KTm90IHRlc3RlZDogMTQ0DQpTY29wZWQgb3V0OiA0OSAoV3JpdHRlbiBhcyBwZXIgQVBJIFY1IHNoZWV0Li5ub3QgYXdhcmUgb2YgY29sb3IgY29kZSBmb2xsb3dlZCBpbiBzaGVldCkNCkV4Y2x1ZGVkIHRlbXBsYXRlIEFQSSBjYXNlcw0KDQoNCg0KYWZ0ZXIgcnVubmluZyBzY3JpcHQgdGhlbiBVSSB1cGRhdGVzDQpzb21ldGltZXMgcXVlcmllcyBkaXNwbGF5DQo='
body.personalizations[1].attachments[0].name = 'txtfile'

body.personalizations[1].to = []

body.personalizations[1].to.append(EmailStruct())
body.personalizations[1].to[0].name = 'pri1'
body.personalizations[1].to[0].email = 'ttesttry758@gmail.com'

body.personalizations[1].to.append(EmailStruct())
body.personalizations[1].to[1].name = 'pri2'
body.personalizations[1].to[1].email = 'testartstar@gmail.com'

body.personalizations[1].cc = []

body.personalizations[1].cc.append(EmailStruct())
body.personalizations[1].cc[0].name = 'Addye'
body.personalizations[1].cc[0].email = 'testartstar1@gmail.com'

body.personalizations[1].bcc = []

body.personalizations[1].bcc.append(EmailStruct())
body.personalizations[1].bcc[0].name = 'Addye'
body.personalizations[1].bcc[0].email = 'archana.jadhav@netcore.co.in'

body.personalizations[1].token_to = '{"token_to": "token_to"}'
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