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
sender_password = "DevOps!2024#__Team3-new"


body = """
Good day,

For information on facilities that have been automatically deployed in the Zones or Districts, please see the attached auto deployment status.
Three categories have been used to group the facilites;

 * Updated sites - successfully updated sites
 * Failed sites - failed sites where deployment was incomplete
 * Unreachable sites - sites that could not be accessed.

Kind Regards,
HIS DevOps
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


