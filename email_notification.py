import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# send email notification
email_recipients = ["zmwakanema@pedaids.org", "oonions@pedaids.org", "willmbowe@gmail.com", "tlwara@pedaids.org", "domstig248@gmail.com", "mnaboti@pedaids.org"]
subject = "Auto Deployment Status - Pilot Sites"


smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
sender_email = "hisalerts@pedaids.org"
sender_password = "DevOps!2024#__Team3-new1"


body = """
Good day,

Attached is the latest auto deployment status for facilities across the Zones or Districts. The facilities have been categorized as follows:

    *Updated Sites: Deployment completed successfully.
    *Failed Sites: Deployment was incomplete or encountered errors.
    *Unreachable Sites: Sites that could not be accessed during deployment.

Please review the attached report, and let us know if you require further details or assistance.

Kind regards,
HIS DevOps Team

"""  # Replace with your actual email body content

# Attachment files
attachment_file = ["updated_sites.txt", "failed_sites.txt", "unreachable_sites.txt"]  # Replace with the actual file paths



# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(email_recipients)
message["Subject"] = subject
# Add body to the email
message.attach(MIMEText(body, "plain"))

for attachment_file in attachment_file:
    attachment = open(attachment_file, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {attachment_file.split('/')[-1]}")
    message.attach(part)

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)


