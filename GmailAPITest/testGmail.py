import ezgmail

ezgmail.init() 
print(ezgmail.EMAIL_ADDRESS)

ezgmail.send('ahmedhelalragab@gmail.com','Title one','Body one',['ka.png'])

unreadmessages = ezgmail.unread()
print(ezgmail.summary(unreadmessages))
print(unreadmessages[0].messages[0].subject)
print(unreadmessages[0].messages[0].body)
print(unreadmessages[0].messages[0].timestamp)
print(unreadmessages[0].messages[0].sender)
print(unreadmessages[0].messages[0].recipient)

recent_messages = ezgmail.recent(maxResults=50)
print(ezgmail.summary(recent_messages))

searched = ezgmail.search('Duolingo')
print(ezgmail.summary(searched))