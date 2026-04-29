import smtplib

def send_email(subject,message):

    sender="soc@company.com"
    receiver="team@company.com"

    mail=f"Subject:{subject}\n\n{message}"

    server=smtplib.SMTP("smtp.server.com")
    server.sendmail(sender,receiver,mail)
    server.quit()


send_email(
"Feed Failure",
"Critical feed is down"
)
