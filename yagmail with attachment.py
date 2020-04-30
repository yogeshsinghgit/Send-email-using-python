
import yagmail # pip install yagamil...

sender_email = YOUR_EMAIL
receiver_email = RECEIVER_EMAIL
subject = "Check THIS out"
sender_password = input(f'Please, enter the password for {sender_email}:\n')

yag = yagmail.SMTP(user=sender_email, password=sender_password)

# sending mail with attachment ...
contents = [
  "This is the first paragraph in our email",
  "As you can see, we can send a list of strings,",
  "being this our third one",
  "path\\name of file with extension",
  "path\\name of file with extension"
]

yag.send(receiver_email, subject, contents)