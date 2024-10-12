def send_email(message, recipient,*, sender):
    if ('@' not in sender or '@' not in recipient or not sender.endswith(('com', 'ru', 'net')) or not
    recipient.endswith(('com', 'ru', 'net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender!="university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса {sender} на адрес {recipient}')
send_email('-', 'vasyok1337@gmail.com', sender = "university.help@gmail.com")
send_email('-', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('-', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('-', "university.help@gmail.com", sender = "university.help@gmail.com")

# = "university.help@gmail.com"
# or ('@' or '.com'or'.ru'or'.net' not in (recipient or sender)
