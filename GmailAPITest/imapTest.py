import imapclient # type: ignore
import pprint
import pyzmail # type: ignore
## connect to IMAP
imapObj = imapclient.IMAPClient('imap.gmail.com',ssl = True)

## login
rec = 'ahmedhelalragab@gmail.com'
password = str(input("Please enter the password: "))
imapObj.login(rec,password)

## print folders 
pprint.pprint(imapObj.list_folders())

## select a folder
imapObj.select_folder('INBOX',readonly=True)

## search 

UniqueIDs = imapObj.search(['ALL'])
# print(UniqueIDs)

rawMessages = imapObj.fetch(UniqueIDs,['body[]'])
# pprint.pprint(rawMessages)

message = pyzmail.PyzMessage.factory(rawMessages[3608]["b'BODY[]'"])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))


print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))