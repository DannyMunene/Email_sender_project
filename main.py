import smtplib      #used to connect and interact with the email server
from email.message import EmailMessage  #Makes it easy to build the email message 
from getpass import getpass 

def send_email(sender_email, sender_password, recipient_email, subject, body):
    #step 1: create the email message object
    msg = EmailMessage()
    msg['From'] = sender_email  #Sender's email
    msg['To'] = recipient_email #Recipient's email
    msg['Subject'] = subject    #Email subject
    msg.set_content(body)       #Email body in plain text
    
    #Step2: connect to Gmail SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()     #Identify ourselves with the server
            smtp.starttls() #Secue the connection with TLS encription
            smtp.login(sender_email, sender_password)   #login to the email account
            smtp.send_message(msg)  #Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occured {e}")


if __name__=="__main__":
    print("=== Python Email Sender===")
    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass("enter your Gmail app password: ")
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter subject: ")
    body = input("Enter your message: ")

    send_email(sender_email, sender_password, recipient_email, subject, body)