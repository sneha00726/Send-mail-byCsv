#This project automates email sending by reading recipient details from a CSV file and sending emails with attachments using SMTP, 
#while adding time delays between emails to avoid spam blocking.
import csv
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to read data from the CSV file
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Function to send emails with attachments
def send_email(to_email, subject, body, attachment_path):
    from_email = 'com@gmail.com'   # Your email
    password = 'qqhy ujhj xcmj jitc'           # App password (NOT real Gmail password)
    smtp_server = 'smtp.gmail.com'

    # MIME setup
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach body
    message.attach(MIMEText(body, 'plain'))

    # Attach resume
    with open(attachment_path, 'rb') as resume:
        resume_attachment = MIMEApplication(resume.read(), Name='resume.pdf')
        resume_attachment['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        message.attach(resume_attachment)

    # Connect and send
    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
        print(f"✅ Email sent successfully to {to_email}")
    except Exception as e:
        print(f" Failed to send email to {to_email}. Error: {e}")

# Main script
def main():
    csv_file_path = 'HRmail.csv'                 # Your CSV file
    resume_path = 'Resume.pdf'     # Resume file

    # Read contacts
    contacts = read_csv(csv_file_path)

    subject = 'Application for Entry-Level IT Position'
    body = """\
Dear Sir/Madam,

Greetings!

My name is Rahul Verma, and I am reaching out to explore any entry-level or graduate opportunities within your organization.

I have recently completed my Bachelor’s degree in Electronics and Telecommunication Engineering from XYZ Institute of Technology. Along with my academic studies, I have developed skills in Python, basic Machine Learning concepts, and web technologies through coursework and projects.

I am highly motivated to start my career in a challenging and growth-oriented environment where I can apply my knowledge, enhance my skills, and contribute effectively to the organization.

Please find my resume attached for your review. I would welcome the opportunity to discuss my profile in more detail. I am available at your convenience and can be contacted at [rahul.verma.demo@outlook.com](mailto:rahul.verma.demo@outlook.com) or 9876543210.

Thank you for your time and consideration.

Warm regards,
Rahul Verma
9876543210
rahul.verma.demo@outlook.com

"""

    email_count = 0

    for contact in contacts:
        to_email = contact['Email']  # Ensure CSV header is 'Email'
        send_email(to_email, subject, body, resume_path)
        email_count += 1

        # Wait a few seconds between each email (e.g., 5–10 sec)
        time.sleep(5)

        # Pause after every 100 emails
        if email_count % 100 == 0:
            print(f"  Sent {email_count} emails. Pausing for 30 minutes...")
            time.sleep(30 * 60)  # 30 minutes = 1800 seconds

    print(" All emails sent successfully!")

if __name__ == "__main__":
    print("----- AUTOMATION SCRIPT FOR MAIL SENDER -----")
    main()
