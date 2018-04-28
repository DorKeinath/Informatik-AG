# Python

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib

# Sender-Angaben
sender = 'ich@mail.de'
smtp_server = 'smtp.mail.de'
smtp_benutzername = 'ich@mail.de'
smtp_passwort = '123'
# Empfänger-Angaben
empfaenger = ['jemandanderes@mail.de']
# Nachricht
betreff = 'Betreff'
nachricht = 'Hallo. Das ist eine E-Mail an dich.'
# Eigentliches Programm, das die E-Mail verschickt
msg = MIMEText(nachricht)
msg['From'] = sender
msg['To'] = ', '.join(empfaenger)
msg['Subject'] = betreff
s = smtplib.SMTP(smtp_server)
s.starttls()
s.login(smtp_benutzername,smtp_passwort)
s.sendmail(sender,empfaenger,msg.as_string())
s.quit()
```
