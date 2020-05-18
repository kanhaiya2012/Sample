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
body.mfrom.email = 'htmlTags@pepitest.xyz'
body.mfrom.name = 'check htmlTags-1'
body.subject = 'Hello htmlTags-1'
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html>
<head>
<style>
span.note {
  font-size: 120%;
  color: red;
}
</style>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
}
</style>
<style>
p {
  border: 1px solid powderblue;
}
</style>
</head>
<body>
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
<h1>My First Heading</h1>

<p>My first paragraph.</p>
<address>
Written by John Doe.<br> 
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>

<h2>HTML Buttons</h2>
<p>HTML buttons are defined with the button tag:</p>

<button>Click me</button>
<a href="https://www.w3schools.com">This is a link</a>
<br><br><br>
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">

<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>  

<h2>An Ordered HTML List</h2>

<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol> 
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
<table>
  <tr>
    <td>
      <p>This is a paragraph</p>
      <p>This is another paragraph</p>
    </td>
    <td>This cell contains a table:
      <table>
        <tr>
          <td>A</td>
          <td>B</td>
        </tr>
        <tr>
          <td>C</td>
          <td>D</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td>This cell contains a list
      <ul>
        <li>apples</li>
        <li>bananas</li>
        <li>pineapples</li>
      </ul>
    </td>
    <td>HELLO</td>
  </tr>
</table>

<div style="background-color:black;color:white;padding:20px;">
  <h2>London</h2>
  <p>London is the capital city of England. It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>
  <p>Standing on the River Thames, London has been a major settlement for two millennia, its history going back to its founding by the Romans, who named it Londinium.</p>
</div> 
</body>
</html>
'

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

body.personalizations[0].token_to = '{"token_to": "token_to"}'
body.personalizations[0].token_cc = '{"token_cc": "token_cc"}'
body.personalizations[0].token_bcc = '{"token_bcc": "token_bcc"}'
body.personalizations[0].headers = 'headers only'

body.personalizations.append(Personalizations())
body.personalizations[1].attributes = jsonpickle.decode('{"NAME":"Pri","SURNAME":"Gaikwad","PROFESSION":"QA"}')
body.personalizations[1].attachments = []

body.personalizations[1].attachments.append(Attachments())
body.personalizations[1].attachments[0].content = 'Y3VybCAtWEdFVCAnc3RhZ2U2LnBlcGlwb3N0LmNvbTo5MjAwL3BlcGlwb3N0Ny0yMDIwMDUvX3NlYXJjaD9wcmV0dHknIC1IICdDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL2pzb24nIC1kICcNCnsNCiAgICJxdWVyeSI6ew0KICAgICAgImJvb2wiOnsNCiAgICAgICAgICJtdXN0IjpbDQogICAgICAgICAgICB7DQogICAgICAgICAgICAgICAidGVybSI6ew0KICAgICAgICAgICAgICAgICAgImNsaWVudGlkIjo2MjEwNw0KICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgfQ0KICAgICAgICAgXQ0KICAgICAgfQ0KICAgfQ0KfScNCg0KVG90YWwgY2FzZXM6IDMzNQ0KUGFzc2VkOiAxMTgNCkZhaWxlZDoyNA0KTm90IHRlc3RlZDogMTQ0DQpTY29wZWQgb3V0OiA0OSAoV3JpdHRlbiBhcyBwZXIgQVBJIFY1IHNoZWV0Li5ub3QgYXdhcmUgb2YgY29sb3IgY29kZSBmb2xsb3dlZCBpbiBzaGVldCkNCkV4Y2x1ZGVkIHRlbXBsYXRlIEFQSSBjYXNlcw0KDQoNCg0KYWZ0ZXIgcnVubmluZyBzY3JpcHQgdGhlbiBVSSB1cGRhdGVzDQpzb21ldGltZXMgcXVlcmllcyBkaXNwbGF5DQo='
body.personalizations[1].attachments[0].name = 'txtfile.txt'

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