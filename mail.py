import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the sender and recipient email addresses
sender_email = "your_email@gmail.com"
recipient_email = "recipient_email@example.com"

# Set up the email server and login credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_email@gmail.com"
smtp_password = "your_email_password"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Subject of the email"

# Attach the message body
body = "This is the body of the email."
message.attach(MIMEText(body, "plain"))

# Set up the SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

# Print a success message
print("Email sent successfully.")
